import mysql.connector
import random

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="class_scheduler_undergrad"
)
cursor = conn.cursor()

# List of valid sections
sections = [
    'Computer Science - 1', 'Computer Science - 2', 'Computer Science - 3', 'Computer Science - 4',
    'Information Technology - 1', 'Information Technology - 2', 'Information Technology - 3', 'Information Technology - 4',
    'Nursing - 1', 'Nursing - 2', 'Nursing - 3', 'Nursing - 4',
    'Hospitality Management - 1', 'Hospitality Management - 2', 'Hospitality Management - 3', 'Hospitality Management - 4',
    'Business Administration - 1', 'Business Administration - 2', 'Business Administration - 3', 'Business Administration - 4',
    'Accounting - 1', 'Accounting - 2', 'Accounting - 3', 'Accounting - 4',
    'Psychology - 1', 'Psychology - 2', 'Psychology - 3', 'Psychology - 4',
    'Engineering - 1', 'Engineering - 2', 'Engineering - 3', 'Engineering - 4',
    'Education - 1', 'Education - 2', 'Education - 3', 'Education - 4'
]

# Select students with NULL section
cursor.execute("SELECT id FROM student WHERE section IS NULL")
students = cursor.fetchall()

# Assign random sections
for student in students:
    random_section = random.choice(sections)
    cursor.execute("UPDATE student SET section = %s WHERE id = %s", (random_section, student[0]))

# Commit changes
conn.commit()
print("✅ Random sections assigned successfully!")

# Close connection
cursor.close()
conn.close()
