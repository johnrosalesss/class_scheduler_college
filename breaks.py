import mysql.connector

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
cursor = conn.cursor(buffered=True)  # ✅ Use a buffered cursor
print("Connected successfully!")

# **2. Fetch Sections & Year Levels**
print("Fetching sections and their year levels...")
cursor.execute("SELECT section_id, year_level FROM sections")
sections = cursor.fetchall()

if not sections:
    print("⚠ No sections found in the database.")
    conn.close()
    exit()

# **3. Define Break Durations**
BREAKS = {
    "recess": "00:30:00",  # 30-minute break
    "lunch": "01:00:00"    # 1-hour break
}

break_times = {
    "recess": ("09:30:00", "10:00:00"),
    "lunch": ("12:00:00", "13:00:00")
}

# **4. Fetch Time Slot IDs for Each Day, Start Time, and End Time**
print("Fetching time slot IDs for breaks...")
time_slot_ids = {}

for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
    for break_name, (start_time, end_time) in break_times.items():
        cursor.execute(
            "SELECT time_slot_id FROM time_slots WHERE day = %s AND start_time = %s AND end_time = %s",
            (day, start_time, end_time)
        )
        result = cursor.fetchone()
        if result:
            time_slot_ids[(day, break_name)] = result[0]
        else:
            print(f"⚠ Warning: No time slot found for {break_name} on {day} ({start_time} - {end_time})")
            time_slot_ids[(day, break_name)] = None

# **5. Clear Old Break Entries**
print("Clearing old break entries...")
cursor.execute("DELETE FROM break")
conn.commit()  # ✅ Commit to avoid unread results issue

# **6. Insert Breaks for Each Section Every Day**
print("Generating break schedules...")

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for section_id, year_level in sections:
    if year_level in (11, 12):  # Year levels 11 and 12 get both recess and lunch
        breaks_to_insert = [("Recess", "recess"), ("Lunch Break", "lunch")]
    else:  # All other year levels get only a 1-hour lunch break
        breaks_to_insert = [("Lunch Break", "lunch")]

    for day in DAYS:  # ✅ Assign breaks for every day
        for break_name, break_key in breaks_to_insert:
            time_slot_id = time_slot_ids.get((day, break_key))
            start_time, end_time = break_times[break_key]

            if time_slot_id is None:
                print(f"⚠ Skipping {break_name} for Section {section_id} on {day} (Missing time slot ID)")
                continue

            cursor.execute(
                "INSERT INTO break (name, time_slot_id, day, start_time, end_time, section_id) VALUES (%s, %s, %s, %s, %s, %s)",
                (break_name, time_slot_id, day, start_time, end_time, section_id)
            )
            print(f"✔ Inserted {break_name} for Section {section_id} on {day} ({start_time} - {end_time})")

# **7. Commit and Close**
conn.commit()
conn.close()
print("✅ Break time generation completed successfully for all sections and days!")
