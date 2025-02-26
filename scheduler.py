import mysql.connector 
import random
import csv
import sys
from datetime import timedelta
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

# **1. Connect to MySQL**
print("Connecting to MySQL...")
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="class_scheduler_undergrad",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)
cursor = conn.cursor()
print("Connected successfully!")

# **2. Load Data from Tables**
print("Loading subjects...")
cursor.execute("SELECT subject_code, subject_name, program, year_level, lecture_hours, subject_type FROM subjects")
subjects = cursor.fetchall()

print("Loading teachers...")
cursor.execute("SELECT id_num, teacher_id, teacher_name, subject_code, teacher_type FROM teachers")
teachers = cursor.fetchall()

print("Loading rooms...")
cursor.execute("SELECT room_id, room_name, capacity, room_type FROM rooms")
rooms = cursor.fetchall()

print("Loading time slots...")
cursor.execute("SELECT time_slot_id, day, start_time, end_time FROM time_slots ORDER BY day, start_time")
time_slots = cursor.fetchall()

print("Loading student groups (blocks)...")
cursor.execute("SELECT block_id, course, year_level, num_students FROM students")
student_groups = {f"{course}-{year_level}": block_id for block_id, course, year_level, _ in cursor.fetchall()}

# **3. Clear Old Schedule**
print("Clearing old schedule...")
cursor.execute("DELETE FROM schedule")

# **4. Define Constraints**
LUNCH_START = "12:00:00"
LUNCH_END = "13:00:00"
DAY_START = "08:00:00"
DAY_END = "17:00:00"

# **5. Initialize Tracking Structures**
teacher_schedules = defaultdict(list)  # {teacher_id: [(day, start_time, end_time)]}
room_schedules = defaultdict(list)     # {room_id: [(day, start_time, end_time)]}
student_schedules = defaultdict(list)  # {block_id: [(day, start_time, end_time)]}

# **6. Function to Check Schedule Validity**
def is_valid_slot(teacher_id, room_id, block_id, day, start_time, end_time, teacher_type, subject_type, room_type):
    start_time_str = str(start_time)
    end_time_str = str(end_time)

    # **Lunch break restriction**
    if LUNCH_START <= start_time_str < LUNCH_END or LUNCH_START < end_time_str <= LUNCH_END:
        return False

    # **School hours restriction**
    if start_time_str < DAY_START or end_time_str > DAY_END:
        return False

    # **Room Type Constraint**
    if subject_type == "Laboratory" and room_type != "Laboratory":
        return False  # Lab subjects must be in laboratory rooms

    # **Part-Time Teacher Constraint**
    if teacher_type == "Part-Time" and day != "Saturday":
        return False  # Part-time teachers can only teach on Saturdays

    # **Teacher Schedule Conflict**
    for d, s, e in teacher_schedules[teacher_id]:
        if d == day and not (e <= start_time or s >= end_time):
            return False

    # **Room Schedule Conflict**
    for d, s, e in room_schedules[room_id]:
        if d == day and not (e <= start_time or s >= end_time):
            return False

    # **Student Group Conflict**
    for d, s, e in student_schedules[block_id]:
        if d == day and not (e <= start_time or s >= end_time):
            return False

    return True

# **7. Assign Subjects While Distributing Across the Week**
unassigned_subjects = []

# **Track scheduled hours per day to balance days**
day_counts = defaultdict(int)

for subject in subjects:
    subject_code, subject_name, program, year_level, lecture_hours, subject_type = subject
    student_group_key = f"{program}-{year_level}"

    if student_group_key not in student_groups:
        print(f"⚠ No block found for {student_group_key}, skipping...")
        unassigned_subjects.append((subject_code, "No matching block found"))
        continue

    block_id = student_groups[student_group_key]
    available_teachers = [t for t in teachers if t[3] == subject_code]
    
    if not available_teachers:
        print(f"⚠ No teacher available for {subject_code}, skipping...")
        unassigned_subjects.append((subject_code, "No available teacher"))
        continue

    hours_scheduled = 0

    # **Prioritize days with fewer scheduled hours**
    sorted_days = sorted(set(slot[1] for slot in time_slots), key=lambda d: day_counts[d])

    while hours_scheduled < lecture_hours:
        teacher = random.choice(available_teachers)
        teacher_id = teacher[1]
        teacher_name = teacher[2]  
        teacher_type = teacher[4]  

        # **Select Room Based on Subject Type**
        suitable_rooms = [r for r in rooms if subject_type == "Lecture" or (subject_type == "Laboratory" and r[3] == "Laboratory")]
        if not suitable_rooms:
            print(f"⚠ No suitable room for {subject_code}, skipping...")
            unassigned_subjects.append((subject_code, "No suitable room"))
            break

        room = random.choice(suitable_rooms)
        room_id = room[0]
        room_name = room[1]
        room_type = room[3]  

        # **Find Continuous Valid Time Slots on Least Used Days**
        for day in sorted_days:
            valid_slots = [slot for slot in time_slots if slot[1] == day]
            for i in range(len(valid_slots) - (lecture_hours - hours_scheduled)):
                continuous_slots = []
                for j in range(lecture_hours - hours_scheduled):
                    slot = valid_slots[i + j]
                    slot_id, slot_day, start_time, end_time = slot

                    if is_valid_slot(teacher_id, room_id, block_id, slot_day, start_time, end_time, teacher_type, subject_type, room_type):
                        continuous_slots.append(slot)
                    else:
                        break  

                if len(continuous_slots) == (lecture_hours - hours_scheduled):  
                    for slot_id, slot_day, start_time, end_time in continuous_slots:
                        teacher_schedules[teacher_id].append((slot_day, start_time, end_time))
                        room_schedules[room_id].append((slot_day, start_time, end_time))
                        student_schedules[block_id].append((slot_day, start_time, end_time))
                        day_counts[slot_day] += 1  
                        hours_scheduled += 1

                        print(f"Inserting: {subject_code} - {teacher_name} in {room_name} at {slot_day} {start_time}-{end_time}")
                        cursor.execute(
                            "INSERT INTO schedule (block_id, subject_code, teacher_name, room_name, day, time_slot_id) VALUES (%s, %s, %s, %s, %s, %s)",
                            (block_id, subject_code, teacher_name, room_name, slot_day, slot_id)
                        )
                    break

    if hours_scheduled < lecture_hours:
        print(f"❌ Failed to schedule all hours for {subject_code}.")
        unassigned_subjects.append((subject_code, "Insufficient continuous time slots"))

# **8. Commit Schedule to Database**
conn.commit()

# **9. Export Weekly Schedule to CSV**
def export_to_csv(cursor, filename):
    cursor.execute("SELECT * FROM schedule")
    rows = cursor.fetchall()

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Block ID', 'Subject Code', 'Teacher Name', 'Room Name', 'Day', 'Time Slot ID'])
        for row in rows:
            writer.writerow(row)

    print(f"Data exported to {filename} successfully.")

export_to_csv(cursor, 'weekly_schedule.csv')

# **10. Close MySQL Connection**
conn.close()
print("✅ Schedule generation process completed!")
