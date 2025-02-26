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
cursor.execute("SELECT subject_code, subject_name, program, year_level, lecture_hours FROM subjects")
subjects = cursor.fetchall()

print("Loading teachers...")
cursor.execute("SELECT id_num, teacher_id, teacher_name, subject_code, type FROM teachers")
teachers = cursor.fetchall()

print("Loading rooms...")
cursor.execute("SELECT room_id, room_name, capacity FROM rooms")
rooms = cursor.fetchall()

print("Loading time slots...")
cursor.execute("SELECT time_slot_id, day, start_time, end_time FROM time_slots")
time_slots = cursor.fetchall()

print("Loading students...")
cursor.execute("SELECT id, school_aide_id, last_name, first_name, rfid, section FROM student")
students = cursor.fetchall()

print("Loading student groups...")
cursor.execute("SELECT block_id, course, year_level, num_students, section_name FROM students")
student_groups = cursor.fetchall()

# **3. Clear Old Schedule**
print("Clearing old schedule...")
cursor.execute("DELETE FROM schedule")

# **4. Define Constraints**
LUNCH_START = "12:00:00"
LUNCH_END = "13:00:00"
DAY_START = "08:00:00"
DAY_END = "17:00:00"

# **5. Initialize Tracking Structures**
assigned_slots = set()
teacher_schedules = {}  # {teacher_id: [(day, start_time, end_time)]}
room_schedules = {}     # {room_id: [(day, start_time, end_time)]}
student_schedules = {}  # {program-year: [(day, start_time, end_time)]}

# **6. Function to Check Schedule Validity**
def is_valid_slot(teacher_id, room_id, students, day, start_time, end_time):
    start_time_str = str(start_time) if isinstance(start_time, timedelta) else start_time
    end_time_str = str(end_time) if isinstance(end_time, timedelta) else end_time

    # Lunch break restriction
    if LUNCH_START <= start_time_str <= LUNCH_END or LUNCH_START <= end_time_str <= LUNCH_END:
        return False

    # School hours restriction
    if start_time_str < DAY_START or end_time_str > DAY_END:
        return False

    # Check teacher schedule conflicts
    if teacher_id in teacher_schedules:
        if any(d == day and not (str(e) <= start_time_str or str(s) >= end_time_str) for d, s, e in teacher_schedules[teacher_id]):
            return False

    # Check room schedule conflicts
    if room_id in room_schedules:
        if any(d == day and not (str(e) <= start_time_str or str(s) >= end_time_str) for d, s, e in room_schedules[room_id]):
            return False

    # Check student group conflicts
    if students in student_schedules:
        if any(d == day and not (str(e) <= start_time_str or str(s) >= end_time_str) for d, s, e in student_schedules[students]):
            return False

    return True

# **7. Assign Subjects While Following Constraints**
unassigned_subjects = []

for subject in subjects:
    subject_code, subject_name, program, year_level, lecture_hours = subject
    students_group = f"{program}-{year_level}"  # Unique student group key

    available_teachers = [t for t in teachers if t[3] == subject_code]
    if not available_teachers:
        print(f"⚠ No teacher available for {subject_code}, skipping...")
        unassigned_subjects.append((subject_code, "No available teacher"))
        continue

    hours_scheduled = 0
    max_attempts = 10
    attempts = 0

    while hours_scheduled < lecture_hours and attempts < max_attempts:
        teacher = random.choice(available_teachers)
        room = random.choice(rooms)

        # **Special Condition for Part-Time Teachers**
        if teacher[4] == "Part-Time" and "Saturday" not in [slot[1] for slot in time_slots]:
            print(f"⚠ Part-time teacher {teacher[1]} must be scheduled on Saturday, skipping...")
            attempts += 1
            continue

        # **Randomly Select a Time Slot**
        time_slot = random.choice(time_slots)
        slot_id, day, start_time, end_time = time_slot

        # **Check If Slot is Valid**
        if is_valid_slot(teacher[1], room[0], students_group, day, start_time, end_time):
            # Assign slot
            assigned_slots.add(slot_id)
            teacher_schedules.setdefault(teacher[0], []).append((day, start_time, end_time))
            room_schedules.setdefault(room[0], []).append((day, start_time, end_time))
            student_schedules.setdefault(f"{students_group}", []).append((day, start_time, end_time))
            hours_scheduled += 1

            print(f"Inserting: {subject_code} - {teacher[1]} in {room[1]} at {day} {start_time}-{end_time}")
            cursor.execute(
                "INSERT INTO schedule (block_id, subject_code, teacher_name, room_name, day, start_time, end_time) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (students_group, subject_code, teacher[1], room[1], day, start_time, end_time)
            )

        else:
            print(f"⚠ Slot {slot_id} conflicts with existing schedule, retrying...")

        attempts += 1

    if hours_scheduled < lecture_hours:
        print(f"❌ Failed to schedule all hours for {subject_code} after {attempts} attempts.")
        unassigned_subjects.append((subject_code, "Failed to schedule all hours"))

# **8. Commit Schedule to Database**
conn.commit()

# **9. Export Weekly Schedule to CSV**
def export_to_csv(cursor, filename):
    cursor.execute("SELECT * FROM schedule")
    rows = cursor.fetchall()

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Block ID', 'Subject Code', 'Teacher Name', 'Room Name', 'Day', 'Start Time', 'End Time'])
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
