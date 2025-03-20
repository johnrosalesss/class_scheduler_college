import mysql.connector
import sys

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

# **2. Load Data**
# Load sections
cursor.execute("SELECT section_id, program, year_level FROM sections")
sections = cursor.fetchall()

# Load subjects by program and year level
cursor.execute("""
    SELECT subject_id, subject_name, program, year_level
    FROM subjects
""")
subjects = cursor.fetchall()

# Create blocks automatically
print("Generating blocks...")

# Clear old blocks
cursor.execute("DELETE FROM blocks")

block_id = 1
for section_id, section_program, year_level in sections:
    # Filter subjects for the same program and year level
    matching_subjects = [
        (subject_id, subject_name)
        for subject_id, subject_name, subject_program, subject_year_level in subjects
        if (subject_program == section_program or subject_program == 'General') 
        and subject_year_level == year_level
    ]

    if not matching_subjects:
        print(f"⚠ No subjects found for Section {section_id} (Program {section_program}, Year {year_level}).")
        continue

    for subject_id, subject_name in matching_subjects:
        block_name = f"{subject_name} - Year {year_level}"
        cursor.execute("""
            INSERT INTO blocks (block_id, block_name, section_id, subject_id)
            VALUES (%s, %s, %s, %s)
        """, (block_id, block_name, section_id, subject_id))

        print(f"✅ Created block {block_id}: {block_name} for Section {section_id}")
        block_id += 1

# **4. Commit and Close**
conn.commit()
conn.close()

print("✅ Block generation process completed!")
