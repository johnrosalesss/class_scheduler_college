import mysql.connector
import csv
import os

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

# **2. Fetch Schedule Data**
print("Fetching schedule data...")
cursor.execute("""
    SELECT section_id, block_id, subject_code, teacher_name, room_name, day, start_time, end_time, semester
    FROM schedule
    ORDER BY section_id, day, start_time
""")
schedule_data = cursor.fetchall()

# **3. Define Folder Paths**
report_folder = "reports"
section_folder = os.path.join(report_folder, "sections")
teacher_folder = os.path.join(report_folder, "teachers")
room_folder = os.path.join(report_folder, "rooms")

# **Create directories if they don’t exist**
os.makedirs(section_folder, exist_ok=True)
os.makedirs(teacher_folder, exist_ok=True)
os.makedirs(room_folder, exist_ok=True)

# **4. Generate Main Report**
main_report_filename = os.path.join(report_folder, "schedule_report.csv")
print(f"Generating main CSV report: {main_report_filename}...")

with open(main_report_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # **Write Header Row**
    writer.writerow(["Section ID", "Block ID", "Subject Code", "Teacher Name", "Room Name", "Day", "Start Time", "End Time", "Semester"])

    # **Write Data Rows**
    for row in schedule_data:
        writer.writerow(row)

print(f"✅ Main report saved at: {os.path.abspath(main_report_filename)}")

# **5. Generate Section-Wise Reports**
print("Generating section-wise reports...")

# **Dictionary to store data per section**
sections = {}

for row in schedule_data:
    section_id = row[0]
    if section_id not in sections:
        sections[section_id] = []
    sections[section_id].append(row)

# **Write each section’s data into its own CSV file**
for section_id, rows in sections.items():
    section_filename = os.path.join(section_folder, f"section_{section_id}.csv")
    
    with open(section_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # **Write Header Row**
        writer.writerow(["Section ID", "Block ID", "Subject Code", "Teacher Name", "Room Name", "Day", "Start Time", "End Time", "Semester"])

        # **Write Data Rows**
        writer.writerows(rows)

    print(f"✅ Section {section_id} report saved at: {os.path.abspath(section_filename)}")

# **6. Generate Teacher-Wise Reports**
print("Generating teacher-wise reports...")

# **Dictionary to store data per teacher**
teachers = {}

for row in schedule_data:
    teacher_name = row[3]  # Get teacher name
    if teacher_name and teacher_name.strip():  # Ensure it's not empty
        if teacher_name not in teachers:
            teachers[teacher_name] = []
        teachers[teacher_name].append(row)

# **Write each teacher’s data into their own CSV file**
for teacher_name, rows in teachers.items():
    teacher_filename = os.path.join(teacher_folder, f"{teacher_name.replace(' ', '_')}.csv")

    with open(teacher_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # **Write Header Row**
        writer.writerow(["Section ID", "Block ID", "Subject Code", "Room Name", "Day", "Start Time", "End Time", "Semester"])

        # **Write Data Rows (Exclude Teacher Name to avoid redundancy)**
        for row in rows:
            writer.writerow([row[0], row[1], row[2], row[4], row[5], row[6], row[7], row[8]])

    print(f"✅ Teacher {teacher_name} report saved at: {os.path.abspath(teacher_filename)}")

# **7. Generate Room-Wise Reports**
print("Generating room-wise reports...")

# **Dictionary to store data per room**
rooms = {}

for row in schedule_data:
    room_name = row[4]  # Get room name
    if room_name and room_name.strip():  # Ensure it's not empty
        if room_name not in rooms:
            rooms[room_name] = []
        rooms[room_name].append(row)

# **Write each room’s data into its own CSV file**
for room_name, rows in rooms.items():
    room_filename = os.path.join(room_folder, f"room_{room_name.replace(' ', '_')}.csv")

    with open(room_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # **Write Header Row**
        writer.writerow(["Section ID", "Block ID", "Subject Code", "Teacher Name", "Day", "Start Time", "End Time", "Semester"])

        # **Write Data Rows (Exclude Room Name to avoid redundancy)**
        for row in rows:
            writer.writerow([row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8]])

    print(f"✅ Room {room_name} report saved at: {os.path.abspath(room_filename)}")

# **8. Close Connection**
conn.close()
print("✅ All reports generated successfully!")
