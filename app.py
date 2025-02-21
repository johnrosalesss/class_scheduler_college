from flask import Flask, render_template, request
import mysql.connector
import pandas as pd

app = Flask(__name__)

def get_schedule(filter_by=""):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="class_scheduler")
    cursor = conn.cursor()
    
    query = "SELECT * FROM schedule"
    if filter_by:
        query += " WHERE day = %s OR teacher_name = %s"
        cursor.execute(query, (filter_by, filter_by))
    else:
        cursor.execute(query)
    
    data = cursor.fetchall()
    conn.close()
    
    return pd.DataFrame(data, columns=["ID", "Subject", "Teacher", "Room", "Day", "Start Time", "End Time"])

@app.route('/', methods=['GET', 'POST'])
def index():
    filter_by = request.form.get("filter", "")
    schedule_df = get_schedule(filter_by)
    return render_template("schedule.html", tables=[schedule_df.to_html(classes="data", index=False)], filter_by=filter_by)

if __name__ == '__main__':
    app.run(debug=True)
