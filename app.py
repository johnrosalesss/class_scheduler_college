from flask import Flask, render_template, request, jsonify
from datetime import timedelta
import mysql.connector
import pandas as pd
import subprocess

app = Flask(__name__)

def get_schedule(filter_by=""):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="class_scheduler_undergrad")  # UPDATED
    cursor = conn.cursor(dictionary=True)  # Fetch results as dictionaries
    
    query = "SELECT * FROM schedule"
    if filter_by:
        query += " WHERE day = %s OR teacher_name = %s"
        cursor.execute(query, (filter_by, filter_by))
    else:
        cursor.execute(query)
    
    data = cursor.fetchall()
    conn.close()
    
    # Handle empty results
    if not data:
        return pd.DataFrame()

    return pd.DataFrame(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    filter_by = request.form.get("filter", "")
    schedule_df = get_schedule(filter_by)

    return render_template("index.html", 
                           tables=[schedule_df.to_html(classes="data", index=False)] if not schedule_df.empty else [],
                           filter_by=filter_by)

@app.route('/get_schedule', methods=['GET'])
def get_schedule_json():
    day_filter = request.args.get('day', '')  # Get selected day from request

    conn = mysql.connector.connect(host="localhost", user="root", password="", database="class_scheduler_undergrad") 
    cursor = conn.cursor(dictionary=True)

    # Fetch schedule based on selected day
    if day_filter:
        cursor.execute("SELECT * FROM schedule WHERE day = %s", (day_filter,))
    else:
        cursor.execute("SELECT * FROM schedule")
    
    data = cursor.fetchall()
    conn.close()

    if not data:
        return jsonify({"columns": [], "data": []})

    columns = list(data[0].keys())

    for row in data:
        for key, value in row.items():
            if isinstance(value, timedelta):
                row[key] = str(value)

    return jsonify({"columns": columns, "data": data})

@app.route('/run_scheduler', methods=['POST'])
def run_scheduler():
    try:
        # Run scheduler.py and capture output
        result = subprocess.run(["python", "scheduler.py"], capture_output=True, text=True)

        if result.returncode == 0:
            return jsonify({"message": "Scheduling completed successfully!"})
        else:
            print("Scheduler Error:", result.stderr)  # 🔍 Log error to Flask console
            return jsonify({"error": "Scheduling failed!", "details": result.stderr}), 500
    except Exception as e:
        print("Exception:", str(e))  # 🔍 Log unexpected errors
        return jsonify({"error": "An error occurred while running the scheduler.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
