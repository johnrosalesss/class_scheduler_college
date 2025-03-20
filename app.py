from flask import Flask, render_template, request, jsonify
from datetime import timedelta
import mysql.connector
import pandas as pd
import subprocess

app = Flask(__name__)

def get_schedule(filter_by=""):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="class_scheduler_undergrad")
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT sc.id, bl.block_name, s.subject_name, sc.subject_code, 
               CONCAT(t.teacher_first_name, ' ', t.teacher_last_name) AS teacher_name,
               r.room_name, sc.day, ts.start_time, ts.end_time, sc.semester
        FROM schedule sc
        JOIN blocks bl ON sc.block_id = bl.block_id
        JOIN subjects s ON sc.subject_code = s.subject_code
        JOIN teachers t ON sc.teacher_name = CONCAT(t.teacher_first_name, ' ', t.teacher_last_name)
        JOIN rooms r ON sc.room_name = r.room_name
        JOIN time_slots ts ON sc.time_slot_id = ts.time_slot_id
    """

    params = []
    if filter_by:
        query += " WHERE sc.day = %s OR CONCAT(t.teacher_first_name, ' ', t.teacher_last_name) = %s"
        params = [filter_by, filter_by]

    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()

    return pd.DataFrame(data) if data else pd.DataFrame()

@app.route('/', methods=['GET', 'POST'])
def index():
    filter_by = request.form.get("filter", "")
    schedule_df = get_schedule(filter_by)

    return render_template("index.html", 
                           tables=[schedule_df.to_html(classes="data", index=False)] if not schedule_df.empty else [],
                           filter_by=filter_by)

@app.route('/get_schedule', methods=['GET'])
def get_schedule_json():
    day_filter = request.args.get('day', '')

    conn = mysql.connector.connect(host="localhost", user="root", password="", database="class_scheduler_undergrad")
    cursor = conn.cursor(dictionary=True)

    # Fetch schedule data
    query = """
        SELECT sc.id, sc.block_id, sc.subject_code, sc.teacher_name, sc.room_name, 
               sc.day, ts.start_time, ts.end_time, sc.semester
        FROM schedule sc
        JOIN time_slots ts ON sc.time_slot_id = ts.time_slot_id
    """

    params = []
    if day_filter:
        query += " WHERE sc.day = %s"
        params = [day_filter]

    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()

    # 🔹 Convert `timedelta` to a string format (HH:MM:SS)
    for row in data:
        if isinstance(row["start_time"], timedelta):
            row["start_time"] = str(row["start_time"])
        if isinstance(row["end_time"], timedelta):
            row["end_time"] = str(row["end_time"])

    if not data:
        return jsonify({"columns": ["ID", "Block ID", "Subject Code", "Teacher", "Room", "Day", "Start Time", "End Time", "Semester"], "data": []})

    return jsonify({"columns": list(data[0].keys()), "data": data})


@app.route('/run_scheduler', methods=['POST'])
def run_scheduler():
    try:
        # Run scheduler.py and capture output
        result = subprocess.run(["python3", "scheduler.py"], capture_output=True, text=True)

        if result.returncode == 0:
            return jsonify({"message": "Scheduling completed successfully!"})
        else:
            print("Scheduler Error:", result.stderr)
            return jsonify({"error": "Scheduling failed!", "details": result.stderr}), 500
    except Exception as e:
        print("Exception:", str(e))
        return jsonify({"error": "An error occurred while running the scheduler.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
