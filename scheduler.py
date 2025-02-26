import mysql.connector 
import random
import csv
import sys
from datetime import timedelta

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
cursor.execute("SELECT room_id, room_name, capacity, room_type FROM rooms")  # Added room_type
rooms = cursor.fetchall()

print("Loading time slots...")
cursor.execute("SELECT time_slot_id, day, start_time, end_time FROM time_slots")
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
teacher_schedules = {}  # {teacher_id: [(day, start_time, end_time)]}
room_schedules = {}     # {room_id: [(day, start_time, end_time)]}
student_schedules = {}  # {block_id: [(day, start_time, end_time)]}

# **6. Function to Check Schedule Validity**
def is_valid_slot(teacher_id, room_id, block_id, day, start_time, end_time, teacher_type, subject_type, room_type):
    start_time_str = str(start_time) if isinstance(start_time, timedelta) else start_time
    end_time_str = str(end_time) if isinstance(end_time, timedelta) else end_time

    # **Lunch break restriction**
    if LUNCH_START <= start_time_str <= LUNCH_END or LUNCH_START <= end_time_str <= LUNCH_END:
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
    if teacher_id in teacher_schedules:
        if any(d == day and not (str(e) <= start_time_str or str(s) >= end_time_str) for d, s, e in teacher_schedules[teacher_id]):
            return False

    # **Room Schedule Conflict**
    if room_id in room_schedules:
        if any(d == day and not (str(e) <= start_time_str or str(s) >= end_time_str) for d, s, e in room_schedules[room_id]):
            return False

    # **Student Group Conflict**
    if block_id in student_schedules:
        if any(d == day and not (str(e) <= start_time_str or str(s) >= end_time_str) for d, s, e in student_schedules[block_id]):
            return False

    return True

# **7. Assign Subjects While Following Constraints**
unassigned_subjects = []

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

        # **Find a Valid Time Slot**
        random.shuffle(time_slots)  # Shuffle to increase variety
        for slot_id, day, start_time, end_time in time_slots:
            if is_valid_slot(teacher_id, room_id, block_id, day, start_time, end_time, teacher_type, subject_type, room_type):
                teacher_schedules.setdefault(teacher_id, []).append((day, start_time, end_time))
                room_schedules.setdefault(room_id, []).append((day, start_time, end_time))
                student_schedules.setdefault(block_id, []).append((day, start_time, end_time))
                hours_scheduled += 1

                print(f"Inserting: {subject_code} - {teacher_name} in {room_name} at {day} {start_time}-{end_time}")
                cursor.execute(
                    "INSERT INTO schedule (block_id, subject_code, teacher_name, room_name, day, time_slot_id) VALUES (%s, %s, %s, %s, %s, %s)",
                    (block_id, subject_code, teacher_name, room_name, day, slot_id)
                )
                break  # Move to the next lecture hour requirement if one slot is assigned

    if hours_scheduled < lecture_hours:
        print(f"❌ Failed to schedule all hours for {subject_code}.")
        unassigned_subjects.append((subject_code, "Insufficient time slots"))

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

# **10. Summary of Unassigned Subjects**
print("\n=== Unassigned Subjects ===")
if unassigned_subjects:
    for subject_code, reason in unassigned_subjects:
        print(f"Subject Code: {subject_code} - Reason: {reason}")
else:
    print("All subjects were successfully scheduled.")

# **11. Close MySQL Connection**
conn.close()
print("✅ Schedule generation process completed!")
