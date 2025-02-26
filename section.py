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

# Fetch all rooms
cursor.execute("SELECT room_id FROM rooms")
rooms = cursor.fetchall()

# Assign random type (Lecture or Laboratory) to each room
for room in rooms:
    random_type = random.choice(["Lecture", "Laboratory"])
    cursor.execute("UPDATE rooms SET type = %s WHERE room_id = %s", (random_type, room[0]))

# Commit changes
conn.commit()
print("✅ Random room types assigned successfully!")

# Close connection
cursor.close()
conn.close()
