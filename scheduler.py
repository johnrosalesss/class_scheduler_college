import mysql.connector
import random
import sys
import subprocess  # For running blocks.py
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

# **Run blocks.py before proceeding**
print("Running blocks.py to generate blocks...")
subprocess.run(["python", "blocks.py"], check=True)
print("✅ blocks.py executed successfully!")

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
print("Loading sections...")
cursor.execute("SELECT section_id, year_level FROM sections")
sections = {row[0]: row[1] for row in cursor.fetchall()}

print("Loading blocks for each section...")
cursor.execute("SELECT block_id, block_name, section_id, subject_id FROM blocks")
blocks = defaultdict(list)
for block_id, block_name, section_id, subject_id in cursor.fetchall():
    blocks[section_id].append((block_id, block_name, subject_id))

print(f"✅ Loaded {sum(len(b) for b in blocks.values())} blocks across {len(sections)} sections.")

print("Loading teachers...")
cursor.execute("SELECT teacher_id, teacher_first_name, teacher_last_name, subject_name FROM teachers")
teachers = [(t[0], f"{t[1]} {t[2]}", t[3]) for t in cursor.fetchall()]

print("Loading rooms with types...")
cursor.execute("SELECT room_id, room_name, room_type FROM rooms")
rooms = {room[0]: {"name": room[1], "type": room[2]} for room in cursor.fetchall()}

print("Loading time slots...")
cursor.execute("SELECT time_slot_id, day, start_time, end_time FROM time_slots ORDER BY day, start_time")
time_slots = cursor.fetchall()

print("Loading subjects with semester, max daily minutes, and subject types...")
cursor.execute("SELECT subject_id, subject_code, subject_name, semester, max_daily_mins, subject_type FROM subjects")
subject_info = {
    row[0]: {
        "subject_code": row[1],
        "subject_name": row[2],
        "semester": row[3],
        "max_daily_mins": int(row[4]) if row[4] else 30,
        "subject_type": row[5]  
    }
    for row in cursor.fetchall()
}

print("Loading hours per week for each section and subject...")
cursor.execute("SELECT b.section_id, b.subject_id, s.hours_per_week FROM blocks b JOIN subjects s ON b.subject_id = s.subject_id")
section_subject_hours = defaultdict(dict)
for section_id, subject_id, hours_per_week in cursor.fetchall():
    section_subject_hours[section_id][subject_id] = hours_per_week * 60

# **3. Clear Old Schedule**
print("Clearing old schedule entries...")
cursor.execute("DELETE FROM schedule")

# **4. Initialize Tracking Structures**
teacher_schedules = defaultdict(lambda: defaultdict(list))
room_schedules = defaultdict(lambda: defaultdict(list))
section_schedules = defaultdict(lambda: defaultdict(list))
section_subject_weekly_hours = defaultdict(lambda: defaultdict(int))
scheduled_blocks = set()  # Tracks scheduled blocks

# **5. Conflict Checking Function**
def is_valid_slot(teacher_id, room_id, section_id, semester, day, start_time, end_time):
    for d, s, e in teacher_schedules[semester][teacher_id]:
        if d == day and not (e <= start_time or s >= end_time):
            return False
    for d, s, e in room_schedules[semester][room_id]:
        if d == day and not (e <= start_time or s >= end_time):
            return False
    for d, s, e in section_schedules[semester][section_id]:
        if d == day and not (e <= start_time or s >= end_time):
            return False
    return True

# **6. Assign Blocks to Schedule**
for section_id, section_blocks in blocks.items():
    section_year_level = sections[section_id]

    for block_id, block_name, subject_id in section_blocks:
        if block_id in scheduled_blocks:
            print(f"⚠ Block {block_id} already scheduled, skipping...")
            continue

        if subject_id not in subject_info:
            print(f"⚠ No subject data found for block {block_id}, skipping...")
            continue

        subject_data = subject_info[subject_id]
        subject_code = subject_data["subject_code"]
        subject_name = subject_data["subject_name"]
        semester = subject_data["semester"]
        max_mins = subject_data["max_daily_mins"]
        subject_type = subject_data["subject_type"]

        if subject_id not in section_subject_hours[section_id]:
            print(f"⚠ No weekly hours assigned for subject {subject_name} in Section {section_id}, skipping...")
            continue

        weekly_mins_limit = section_subject_hours[section_id][subject_id]
        num_slots_needed = max_mins // 30

        if section_subject_weekly_hours[semester][(section_id, subject_id)] >= weekly_mins_limit:
            print(f"⚠ Subject {subject_name} (Semester {semester}) in Section {section_id} already reached weekly limit, skipping...")
            continue

        matching_teachers = [t for t in teachers if t[2] == subject_name]
        print(f"Checking teachers for subject {subject_name} (Semester {semester}) in block {block_id}: Found {len(matching_teachers)} available.")

        if not matching_teachers:
            print(f"⚠ No teacher available for {subject_name} (Semester {semester}), skipping...")
            continue

        teacher = random.choice(matching_teachers)
        teacher_id, teacher_name, _ = teacher

        available_rooms = [
            room_id for room_id, room in rooms.items() if room["type"] == subject_type
        ]

        if not available_rooms:
            print(f"⚠ No suitable room found for {subject_name} (Type: {subject_type}), skipping...")
            continue

        random.shuffle(available_rooms)

        for room_id in available_rooms:
            room_name = rooms[room_id]["name"]

            available_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            random.shuffle(available_days)

            for day in available_days:
                for i in range(len(time_slots) - num_slots_needed + 1):
                    selected_slots = time_slots[i : i + num_slots_needed]

                    if len(selected_slots) < num_slots_needed:
                        continue

                    time_slot_ids, days, start_times, end_times = zip(*selected_slots)

                    total_mins_scheduled = section_subject_weekly_hours[semester][(section_id, subject_id)] + max_mins
                    if total_mins_scheduled > weekly_mins_limit:
                        continue

                    if is_valid_slot(teacher_id, room_id, section_id, semester, days[0], start_times[0], end_times[-1]):
                        cursor.execute("""
                            INSERT INTO schedule (section_id, block_id, subject_code, teacher_name, room_name, day, time_slot_id, start_time, end_time, semester)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, (section_id, block_id, subject_code, teacher_name, room_name, days[0], time_slot_ids[0], start_times[0], end_times[-1], semester))

                        teacher_schedules[semester][teacher_id].append((days[0], start_times[0], end_times[-1]))
                        room_schedules[semester][room_id].append((days[0], start_times[0], end_times[-1]))
                        section_schedules[semester][section_id].append((days[0], start_times[0], end_times[-1]))

                        section_subject_weekly_hours[semester][(section_id, subject_id)] += max_mins
                        scheduled_blocks.add(block_id)  # Track scheduled block
                        break

# **7. Commit Schedule to Database**
conn.commit()
conn.close()
print("✅ Schedule generation process completed!")
