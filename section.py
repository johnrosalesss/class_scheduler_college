import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="class_scheduler_undergrad"
)
cursor = conn.cursor()

# Fetch all sections with their program, year level, and section name
cursor.execute("SELECT section_id, section_name, program, year_level FROM sections")
sections = cursor.fetchall()  # List of tuples (section_id, section_name, program, year_level)

# Fetch all subjects with their program, year level, and name
cursor.execute("SELECT subject_id, subject_name, program, year_level FROM subjects")
subjects = cursor.fetchall()  # List of tuples (subject_id, subject_name, program, year_level)

# Fetch all general subjects (applicable to all programs)
cursor.execute("SELECT subject_id, subject_name FROM subjects WHERE program = 'General'")
general_subjects = {row[0]: row[1] for row in cursor.fetchall()}  # Dictionary {subject_id: subject_name}

# Assign subjects to sections
blocks = []
for section_id, section_name, section_program, section_year in sections:
    for subject_id, subject_name, subject_program, subject_year in subjects:
        # Assign if the subject matches the section's program and year level
        if (subject_program == section_program and subject_year == section_year) or subject_id in general_subjects:
            block_name = f"{section_name} - {subject_name}"
            blocks.append((block_name, section_id, subject_id))

# Insert into blocks table
if blocks:
    cursor.executemany("INSERT INTO blocks (block_name, section_id, subject_id) VALUES (%s, %s, %s)", blocks)
    conn.commit()
    print(f"✅ {len(blocks)} blocks assigned successfully!")

# Close connection
cursor.close()
conn.close()
