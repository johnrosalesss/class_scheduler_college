import mysql.connector 
import random
import csv
import sys
from datetime import timedelta
from collections import defaultdict
from datetime import datetime

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
teacher_schedules = defaultdict(list)  
room_schedules = defaultdict(list)    
student_schedules = defaultdict(list)  

# **6. Log File Setup**
log_file = "schedule_log.csv"

# Open CSV file and write headers
with open(log_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Message Type", "Course", "Teacher", "Room", "Day", "Time"])

# Function to log messages dynamically
def log_message(message_type, course, teacher, room, day, time):
    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([message_type, course, teacher, room, day, time])

# **Function to Check Schedule Validity**
def is_valid_slot(teacher_id, room_id, block_id, day, start_time, end_time, teacher_type, subject_type, room_type):
    start_time_str = str(start_time)
    end_time_str = str(end_time)

    # **Lunch Break Restriction**
    if LUNCH_START <= start_time_str < LUNCH_END or LUNCH_START < end_time_str <= LUNCH_END:
        return False

    # **School Hours Restriction**
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
day_counts = defaultdict(int)

for subject in subjects:
    subject_code, subject_name, program, year_level, lecture_hours, subject_type = subject
    student_group_key = f"{program}-{year_level}"

    if student_group_key not in student_groups:
        print(f"⚠ No block found for {student_group_key}, skipping...")
        log_message("Failed", subject_code, "No matching block", "N/A", "N/A", "N/A")
        unassigned_subjects.append((subject_code, "No matching block found"))
        continue

    block_id = student_groups[student_group_key]
    available_teachers = [t for t in teachers if t[3] == subject_code]
    
    if not available_teachers:
        print(f"⚠ No teacher available for {subject_code}, skipping...")
        log_message("Failed", subject_code, "No Teacher", "N/A", "N/A", "N/A")
        unassigned_subjects.append((subject_code, "No available teacher"))
        continue

    hours_scheduled = 0
    sorted_days = sorted(set(slot[1] for slot in time_slots), key=lambda d: day_counts[d])

    while hours_scheduled < lecture_hours:
        teacher = random.choice(available_teachers)
        teacher_id = teacher[1]
        teacher_name = teacher[2]  
        teacher_type = teacher[4]  

        suitable_rooms = [r for r in rooms if subject_type == "Lecture" or (subject_type == "Laboratory" and r[3] == "Laboratory")]
        if not suitable_rooms:
            print(f"⚠ No suitable room for {subject_code}, skipping...")
            log_message("Failed", subject_code, "No suitable room", "N/A", "N/A", "N/A")
            unassigned_subjects.append((subject_code, "No suitable room"))
            break

        room = random.choice(suitable_rooms)
        room_id = room[0]
        room_name = room[1]
        room_type = room[3]  

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
                        log_message("Success", subject_code, teacher_name, room_name, slot_day, f"{start_time}-{end_time}")

                        cursor.execute(
                            "INSERT INTO schedule (block_id, subject_code, teacher_name, room_name, day, time_slot_id) VALUES (%s, %s, %s, %s, %s, %s)",
                            (block_id, subject_code, teacher_name, room_name, slot_day, slot_id)
                        )
                    break

def merge_time_slots(time_slots):
    """ Merge overlapping and consecutive time slots into a single duration """
    if not time_slots:
        return []

    # **Sort by start time**
    time_slots.sort()

    merged = []
    start_time, end_time = time_slots[0]

    for current_start, current_end in time_slots[1:]:
        # **If current slot overlaps or is consecutive, extend the end time**
        if current_start <= end_time:  # Overlapping or consecutive
            end_time = max(end_time, current_end)
        else:
            merged.append(f"{start_time} - {end_time}")  # Save previous slot
            start_time, end_time = current_start, current_end  # Start new slot

    merged.append(f"{start_time} - {end_time}")  # Add last slot
    return merged

def export_teacher_schedule(cursor, filename):
    """ Export teacher schedule with merged time slots """
    
    # **Fetch schedule data**
    cursor.execute("""
        SELECT t.teacher_id, t.teacher_name, s.subject_name, s.subject_code, 
               r.room_id, sc.day, ts.start_time, ts.end_time
        FROM schedule sc
        JOIN teachers t ON sc.teacher_name = t.teacher_name
        JOIN subjects s ON sc.subject_code = s.subject_code
        JOIN rooms r ON sc.room_name = r.room_name
        JOIN time_slots ts ON sc.time_slot_id = ts.time_slot_id
        ORDER BY t.teacher_id, sc.day, ts.start_time
    """)
    
    rows = cursor.fetchall()
    teacher_schedule = {}

    # **Group by (teacher, subject, day, room)**
    for teacher_id, teacher_name, subject_name, subject_code, room_id, day, start_time, end_time in rows:
        key = (teacher_id, teacher_name, subject_name, subject_code, room_id, day)
        
        if key not in teacher_schedule:
            teacher_schedule[key] = []
        
        teacher_schedule[key].append((start_time, end_time))

    # **Write to CSV**
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Teacher ID', 'Teacher Name', 'Subject', 'Subject Code', 'Room ID', 'Day', 'Time Duration'])

        for (teacher_id, teacher_name, subject_name, subject_code, room_id, day), time_slots in teacher_schedule.items():
            merged_time = merge_time_slots(time_slots)  # **Now defined!**
            writer.writerow([teacher_id, teacher_name, subject_name, subject_code, room_id, day, "; ".join(merged_time)])

    print(f"📄 Teacher schedule exported successfully to {filename}.")

# **✅ Call the function**
export_teacher_schedule(cursor, 'teacher_schedule.csv')

def merge_time_slots(time_slots):
    """ Merge overlapping and consecutive time slots into a single duration. """
    if not time_slots:
        return []
    
    # Convert time to datetime objects for easier comparison
    time_slots = sorted(time_slots, key=lambda x: x[0])
    merged = [time_slots[0]]

    for start, end in time_slots[1:]:
        last_start, last_end = merged[-1]

        # **Check if the new slot overlaps or is consecutive**
        if start <= last_end:  
            # Merge by extending the end time
            merged[-1] = (last_start, max(last_end, end))
        else:
            # Otherwise, start a new time block
            merged.append((start, end))

    # Convert back to string format
    return [f"{s} - {e}" for s, e in merged]

def export_block_schedule(cursor, filename):
    cursor.execute("""
        SELECT st.block_id, st.course, st.year_level, s.subject_name, s.subject_code, 
               t.teacher_name, r.room_id, sc.day, ts.start_time, ts.end_time
        FROM schedule sc
        JOIN students st ON sc.block_id = st.block_id
        JOIN subjects s ON sc.subject_code = s.subject_code
        JOIN teachers t ON sc.teacher_name = t.teacher_name
        JOIN rooms r ON sc.room_name = r.room_name
        JOIN time_slots ts ON sc.time_slot_id = ts.time_slot_id
        ORDER BY st.block_id, sc.day, ts.start_time
    """)
    
    rows = cursor.fetchall()
    block_schedule = {}

    # **Group schedules by block, subject, and day**
    for block_id, course, year_level, subject_name, subject_code, teacher_name, room_id, day, start_time, end_time in rows:
        key = (block_id, course, year_level, subject_name, subject_code, teacher_name, room_id, day)
        
        if key not in block_schedule:
            block_schedule[key] = []
        
        block_schedule[key].append((start_time, end_time))

    # **Write to CSV**
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Block ID', 'Course', 'Year Level', 'Subject', 'Subject Code', 'Teacher', 'Room ID', 'Day', 'Time Duration'])
        
        for (block_id, course, year_level, subject_name, subject_code, teacher_name, room_id, day), time_slots in block_schedule.items():
            merged_time = merge_time_slots(time_slots)  # **Fix merging**
            writer.writerow([block_id, course, year_level, subject_name, subject_code, teacher_name, room_id, day, "; ".join(merged_time)])

    print(f"📄 Block schedule exported successfully to {filename}.")

# **✅ Call the function**
export_block_schedule(cursor, 'block_schedule.csv')

# **Function to Merge Overlapping Time Slots**
def merge_time_slots(time_slots):
    """ Merge overlapping and consecutive time slots into a single duration. """
    if not time_slots:
        return []
    
    # Convert time to datetime objects for easier comparison
    time_slots = sorted(time_slots, key=lambda x: x[0])
    merged = [time_slots[0]]

    for start, end in time_slots[1:]:
        last_start, last_end = merged[-1]

        # **Check if the new slot overlaps or is consecutive**
        if start <= last_end:  
            # Merge by extending the end time
            merged[-1] = (last_start, max(last_end, end))
        else:
            # Otherwise, start a new time block
            merged.append((start, end))

    # Convert back to string format
    return [f"{s} - {e}" for s, e in merged]

# **Export Weekly Schedule Function**
def export_weekly_schedule(cursor, filename):
    """ Exports the weekly schedule grouped by day and time. """

    cursor.execute("""
        SELECT sc.day, ts.start_time, ts.end_time, s.subject_name, t.teacher_name, st.section_name, r.room_name
        FROM schedule sc
        JOIN students st ON sc.block_id = st.block_id
        JOIN subjects s ON sc.subject_code = s.subject_code
        JOIN teachers t ON sc.teacher_name = t.teacher_name
        JOIN rooms r ON sc.room_name = r.room_name
        JOIN time_slots ts ON sc.time_slot_id = ts.time_slot_id
        ORDER BY FIELD(sc.day, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'), ts.start_time
    """)

    rows = cursor.fetchall()
    weekly_schedule = defaultdict(list)

    for day, start_time, end_time, subject_name, teacher_name, section_name, room_name in rows:
        key = (day, subject_name, teacher_name, section_name, room_name)
        weekly_schedule[key].append((start_time, end_time))

    # **Write to CSV**
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Day", "Time", "Subject Name", "Teacher Name", "Section Name", "Room Name"])

        for (day, subject_name, teacher_name, section_name, room_name), time_slots in weekly_schedule.items():
            merged_time = merge_time_slots(time_slots)  
            writer.writerow([day, "; ".join(merged_time), subject_name, teacher_name, section_name, room_name])

    print(f"📄 Weekly schedule exported successfully to {filename}.")

# **✅ Call the function**
export_weekly_schedule(cursor, 'weekly_schedule.csv')

# **8. Commit Schedule to Database**
conn.commit()

# **9. Close MySQL Connection**
conn.close()
print("✅ Schedule generation process completed!")
