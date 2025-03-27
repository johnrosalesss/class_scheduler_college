import mysql.connector
import random
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

# **1. Run Blocks & Breaks File First**
import subprocess
print("Running breaks.py first...")
subprocess.run(["python", "breaks.py"])

print("Running blocks.py first...")
subprocess.run(["python", "blocks.py"])

# **2. Connect to MySQL**
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

# **3. Load Data from Tables**
print("Loading break times...")
cursor.execute("SELECT time_slot_id, day, start_time, end_time, section_id FROM break")
break_times = defaultdict(lambda: defaultdict(list))

for time_slot_id, day, start_time, end_time, section_id in cursor.fetchall():
    break_times[section_id][day].append((start_time, end_time))

print("Loading teacher availability...")
cursor.execute("SELECT teacher_id, day, time_start, time_end FROM teacher_availability")
teacher_availability = defaultdict(lambda: defaultdict(list))

for teacher_id, day, time_start, time_end in cursor.fetchall():
    teacher_availability[teacher_id][day].append((time_start, time_end))

print("Loading sections...")
cursor.execute("SELECT section_id, year_level FROM sections")
sections = {row[0]: row[1] for row in cursor.fetchall()}

print("Loading blocks...")
cursor.execute("SELECT block_id, block_name, section_id, subject_id FROM blocks")
blocks = defaultdict(list)
for block_id, block_name, section_id, subject_id in cursor.fetchall():
    blocks[section_id].append((block_id, block_name, subject_id))

print("Loading teachers...")
cursor.execute("SELECT teacher_id, teacher_first_name, teacher_last_name, subject_name FROM teachers")
teachers = [(t[0], f"{t[1]} {t[2]}", t[3]) for t in cursor.fetchall()]

print("Loading rooms...")
cursor.execute("SELECT room_id, room_name, room_type FROM rooms")
rooms = {room[0]: {"name": room[1], "type": room[2]} for room in cursor.fetchall()}

print("Loading time slots...")
cursor.execute("SELECT time_slot_id, day, start_time, end_time, minutes FROM time_slots ORDER BY day, start_time")
time_slots = defaultdict(list)
for time_slot_id, day, start_time, end_time, minutes in cursor.fetchall():
    time_slots[day].append({"id": time_slot_id, "start": start_time, "end": end_time, "minutes": minutes})

print("Loading subjects...")
cursor.execute("SELECT subject_id, subject_code, subject_name, semester, max_daily_mins, minutes_per_week, subject_type FROM subjects")
subject_info = {
    row[0]: {
        "subject_code": row[1],
        "subject_name": row[2],
        "semester": row[3],
        "max_daily_mins": int(row[4]) if row[4] else 30,
        "minutes_per_week": int(row[5]),
        "subject_type": row[6]
    }
    for row in cursor.fetchall()
}

print("Loading subject preferences...")
cursor.execute("SELECT subject_id, preferred_day, preferred_start_time, preferred_end_time FROM subject_preferences")
subject_preferences = {}

for subject_id, preferred_day, preferred_start_time, preferred_end_time in cursor.fetchall():
    subject_preferences[subject_id] = {
        "day": preferred_day,
        "start_time": preferred_start_time,
        "end_time": preferred_end_time
    }

print(f"✅ Loaded {len(subject_preferences)} subject preferences.")

print("Loading section preferences...")
cursor.execute("SELECT section_id, preferred_mode, preferred_day, preferred_start_time, preferred_end_time FROM section_preferences")
section_preferences = defaultdict(lambda: {"day": None, "start_time": None, "end_time": None})

for section_id, preferred_mode, preferred_day, preferred_start_time, preferred_end_time in cursor.fetchall():
    section_preferences[section_id] = {
        "mode": preferred_mode,
        "day": preferred_day,
        "start_time": preferred_start_time,
        "end_time": preferred_end_time
    }

print(f"✅ Loaded {len(section_preferences)} section preferences.")

# **4. Clear Old Schedule**
print("Clearing old schedule entries...")
cursor.execute("DELETE FROM schedule")

# **5. Initialize Tracking Structures**
teacher_schedules = defaultdict(lambda: defaultdict(list))
room_schedules = defaultdict(lambda: defaultdict(list))
section_schedules = defaultdict(lambda: defaultdict(list))
section_subject_weekly_minutes = defaultdict(lambda: defaultdict(int))
block_scheduled_days = defaultdict(lambda: defaultdict(set))

# **6. Conflict Checking Function**
def is_valid_slot(teacher_id, room_id, section_id, block_id, semester, subject_id, day, start_time, end_time):
    """Ensure no room, teacher, section, block, or break conflicts, and apply section and subject preferences if they exist."""

    # ✅ Check section preferences if they exist
    if section_id in section_preferences:
        pref = section_preferences[section_id]

        if pref["day"] and day != pref["day"]:
            return False  # ❌ Section prefers a specific day
        
        if pref["start_time"] and pref["end_time"]:
            if not (pref["start_time"] <= start_time and pref["end_time"] >= end_time):
                return False  # ❌ Section prefers a specific time range

    # ✅ Apply subject preferences if they exist
    if subject_id in subject_preferences:
        pref = subject_preferences[subject_id]

        if pref["day"] and day != pref["day"]:
            return False  # ❌ Subject must be scheduled on a specific day
        
        if pref["start_time"] and pref["end_time"]:
            if not (pref["start_time"] <= start_time and pref["end_time"] >= end_time):
                return False  # ❌ Subject must be scheduled in preferred time range

    # ✅ Check if this block is already scheduled on this day
    if day in block_scheduled_days[semester][block_id]:
        return False  # ❌ Block already scheduled on this day

    # ✅ Check for teacher conflicts
    for d, s, e in teacher_schedules[semester][teacher_id]:
        if d == day and not (e <= start_time or s >= end_time):
            return False

    # ✅ Check for room conflicts
    for d, s, e in room_schedules[semester][room_id]:
        if d == day and not (e <= start_time or s >= end_time):
            return False

    # ✅ Check for section conflicts
    for d, s, e in section_schedules[semester][section_id]:
        if d == day and not (e <= start_time or s >= end_time):
            return False

    # ✅ Check for break conflicts
    if section_id in break_times and day in break_times[section_id]:
        for b_start, b_end in break_times[section_id][day]:
            if not (end_time <= b_start or start_time >= b_end):  # ❌ Overlap detected
                return False  

    return True

# **7. Assign Blocks to Schedule**
for section_id, section_blocks in blocks.items():
    section_year_level = sections[section_id]

    for block_id, block_name, subject_id in section_blocks:
        if subject_id not in subject_info:
            print(f"⚠ No subject data found for block {block_id}, skipping...")
            continue

        subject_data = subject_info[subject_id]
        subject_code = subject_data["subject_code"]
        subject_name = subject_data["subject_name"]
        semester = subject_data["semester"]
        max_daily_mins = subject_data["max_daily_mins"]
        minutes_per_week = subject_data["minutes_per_week"]
        subject_type = subject_data["subject_type"]

        if section_subject_weekly_minutes[semester][(section_id, subject_id)] >= minutes_per_week:
            print(f"⚠ Subject {subject_name} (Semester {semester}) in Section {section_id} already reached weekly limit, skipping...")
            continue

        matching_teachers = [t for t in teachers if t[2] == subject_name]
        if not matching_teachers:
            print(f"⚠ No teacher available for {subject_name} (Semester {semester}), skipping...")
            continue

        teacher = random.choice(matching_teachers)
        teacher_id, teacher_name, _ = teacher

        available_rooms = [room_id for room_id, room in rooms.items() if room["type"] == subject_type]
        if not available_rooms:
            print(f"⚠ No suitable room found for {subject_name} (Type: {subject_type}), skipping...")
            continue

        random.shuffle(available_rooms)

        available_days = list(time_slots.keys())
        random.shuffle(available_days)

        for day in available_days:
            for room_id in available_rooms:
                for slot in time_slots[day]:
                    if is_valid_slot(teacher_id, room_id, section_id, block_id, semester, subject_id, day, slot["start"], slot["end"]):
                        cursor.execute("""
                            INSERT INTO schedule (section_id, block_id, subject_code, teacher_name, room_name, day, time_slot_id, start_time, end_time, semester)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, (section_id, block_id, subject_code, teacher_name, rooms[room_id]["name"], day, slot["id"], slot["start"], slot["end"], semester))

                        block_scheduled_days[semester][block_id].add(day)
                        section_schedules[semester][section_id].append((day, slot["start"], slot["end"]))
                        break

# **8. Commit and Close**
conn.commit()
conn.close()
print("✅ Schedule generation process completed!")