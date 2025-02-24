import mysql.connector
import random
import csv
import sys
from datetime import timedelta

sys.stdout.reconfigure(encoding='utf-8')

# Connect to MySQL
print("Connecting to MySQL...")
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="class_scheduler",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)
cursor = conn.cursor()
print("Connected successfully!")

# Load data
print("Loading subjects...")
cursor.execute("SELECT * FROM subjects")
subjects = cursor.fetchall()

print("Loading teachers...")
cursor.execute("SELECT * FROM teachers")
teachers = cursor.fetchall()

print("Loading rooms...")
cursor.execute("SELECT * FROM rooms")
rooms = cursor.fetchall()

print("Loading time slots...")
cursor.execute("SELECT * FROM time_slots")
time_slots = cursor.fetchall()

# Clear old schedule
print("Clearing old schedule...")
cursor.execute("DELETE FROM schedule")

# Track assigned slots and conflicts
assigned_slots = set()
teacher_schedules = {}  # {teacher_name: [(day, start_time, end_time)]}
room_schedules = {}     # {room_name: [(day, start_time, end_time)]}
student_schedules = {}  # {program_year: [(day, start_time, end_time)]}

# Time Constraints
LUNCH_START = "11:00:00"
LUNCH_END = "13:00:00"
DAY_START = "08:00:00"
DAY_END = "17:00:00"

# Function to check if a time slot is valid


def is_valid_slot(teacher, room, students, day, start_time, end_time):
    # Convert `timedelta` objects to strings
    start_time_str = str(start_time) if isinstance(start_time, timedelta) else start_time
    end_time_str = str(end_time) if isinstance(end_time, timedelta) else end_time

    # Lunch break restriction
    if LUNCH_START <= start_time_str <= LUNCH_END or LUNCH_START <= end_time_str <= LUNCH_END:
        return False

    # School hours restriction
    if start_time_str < DAY_START or end_time_str > DAY_END:
        return False

    # Convert teacher schedules to string format before checking
    if teacher in teacher_schedules:
        if any(d == day and not (str(e) <= start_time_str or str(s) >= end_time_str) for d, s, e in teacher_schedules[teacher]):
            return False

    # Convert room schedules to string format before checking
    if room in room_schedules:
        if any(d == day and not (str(e) <= start_time_str or str(s) >= end_time_str) for d, s, e in room_schedules[room]):
            return False

    # Convert student schedules to string format before checking
    if students in student_schedules:
        if any(d == day and not (str(e) <= start_time_str or str(s) >= end_time_str) for d, s, e in student_schedules[students]):
            return False

    return True


# Assign subjects while following constraints
unassigned_subjects = []

for subject in subjects:
    subject_code, subject_name, program, year_level, lecture_hours = subject
    students_group = f"{program}-{year_level}"  # Unique student group key
    
    available_teachers = [t for t in teachers if t[2] == subject_code]
    if not available_teachers:
        print(f"⚠ No teacher available for {subject_code}, skipping...")
        unassigned_subjects.append((subject_code, "No available teacher"))
        continue

    hours_scheduled = 0
    max_attempts = 10
    attempts = 0

    while hours_scheduled < 3 and attempts < max_attempts:
        teacher = random.choice(available_teachers)
        room = random.choice(rooms)

        # Assign only on Saturdays if teacher is part-time
        if teacher[3] == "Part-Time" and "Saturday" not in [slot[1] for slot in time_slots]:
            print(f"⚠ Part-time teacher {teacher[1]} must be scheduled on Saturday, skipping...")
            attempts += 1
            continue

        # Randomly select a time slot
        time_slot = random.choice(time_slots)
        slot_id, day, start_time, end_time = time_slot

        # Check if the slot is valid
        if is_valid_slot(teacher[1], room[1], students_group, day, start_time, end_time):
            # Assign slot
            assigned_slots.add(slot_id)
            teacher_schedules.setdefault(teacher[1], []).append((day, start_time, end_time))
            room_schedules.setdefault(room[1], []).append((day, start_time, end_time))
            student_schedules.setdefault(students_group, []).append((day, start_time, end_time))
            hours_scheduled += 1

            print(f"Inserting: {subject_code} - {teacher[1]} in {room[1]} at {day} {start_time}-{end_time}")
            cursor.execute(
                "INSERT INTO schedule (subject_code, teacher_name, room_name, day, start_time, end_time) VALUES (%s, %s, %s, %s, %s, %s)",
                (subject_code, teacher[1], room[1], day, start_time, end_time)
            )
        else:
            print(f"⚠ Slot {slot_id} conflicts with existing schedule, retrying...")

        attempts += 1

    if hours_scheduled < 3:
        print(f"❌ Failed to schedule all hours for {subject_code} after {attempts} attempts.")
        unassigned_subjects.append((subject_code, "Failed to schedule all hours"))

# Commit schedule to database
conn.commit()

# Export the schedule to a CSV file
def export_to_csv(cursor, filename):
    cursor.execute("SELECT * FROM schedule")
    rows = cursor.fetchall()

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject Code', 'Teacher Name', 'Room Name', 'Day', 'Start Time', 'End Time'])
        for row in rows:
            writer.writerow(row)

    print(f"Data exported to {filename} successfully.")

export_to_csv(cursor, 'weekly_schedule.csv')

# Summary of unassigned subjects
print("\n=== Unassigned Subjects ===")
if unassigned_subjects:
    for subject_code, reason in unassigned_subjects:
        print(f"Subject Code: {subject_code} - Reason: {reason}")
else:
    print("All subjects were successfully scheduled.")

# Close MySQL connection
conn.close()
print("✅ Schedule generation process completed!")
