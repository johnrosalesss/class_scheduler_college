import mysql.connector
import random

# Debug message
print("Connecting to MySQL...")

# Connect to MySQL
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

# Load data from tables
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

# Prepare to track assigned slots and unassigned subjects
assigned_slots = set()
unassigned_subjects = []

# Schedule each subject for 3 hours a week
for subject in subjects:
    subject_code, subject_name, program, year_level, lecture_hours = subject  # Ignore subject_name

    available_teachers = [t for t in teachers if t[2] == subject_code]
    if not available_teachers:
        print(f"⚠ No teacher available for {subject_code}, skipping...")
        unassigned_subjects.append((subject_code, "No available teacher"))
        continue

    # Schedule 3 hours for each subject
    hours_scheduled = 0
    max_attempts = 10  # Maximum attempts to find a slot
    attempts = 0

    while hours_scheduled < 3 and attempts < max_attempts:
        teacher = random.choice(available_teachers)
        room = random.choice(rooms)

        # Randomly select a time slot
        time_slot = random.choice(time_slots)
        slot_id, day, start_time, end_time = time_slot

        # Check if the slot is already assigned
        if slot_id not in assigned_slots:
            assigned_slots.add(slot_id)
            hours_scheduled += 1  # Increment scheduled hours

            # Insert into schedule
            print(f"Inserting: {subject_code} - {teacher[1]} in {room[1]} at {day} {start_time}-{end_time}")
            cursor.execute(
                "INSERT INTO schedule (subject_code, teacher_name, room_name, day, start_time, end_time) VALUES (%s, %s, %s, %s, %s, %s)",
                (subject_code, teacher[1], room[1], day, start_time, end_time)
            )
        else:
            print(f"⚠ Slot {slot_id} already assigned, trying another slot...")

        attempts += 1

    if hours_scheduled < 3:
        print(f"❌ Failed to schedule all hours for {subject_code} after {attempts} attempts.")
        unassigned_subjects.append((subject_code, "Failed to schedule all hours after maximum attempts"))

# Commit and close connection
conn.commit()
conn.close()

# Summary of unassigned subjects
print("\n=== Summary of Unassigned Subjects ===")
if unassigned_subjects:
    for subject_code, reason in unassigned_subjects:
        print(f"Subject Code: {subject_code} - Reason: {reason}")
else:
    print("All subjects were successfully scheduled.")

print("✅ Schedule generation process completed!")