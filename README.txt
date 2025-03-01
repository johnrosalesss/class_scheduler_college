# Class Scheduler Web Application

## Project Overview
The **Class Scheduling System** is designed for a **university registrar** to automate and optimize class schedules while ensuring no conflicts in teacher assignments, subject hours, room availability, and predefined break periods.

## Features
- **Automated Schedule Generation**: Ensures teachers, subjects, and rooms are assigned without conflicts.
- **Time Slot Management**: Allocates periods efficiently within **8:00 AM - 5:00 PM**.
- **Constraint Handling**:
  - Teachers are assigned subjects based on specialization.
  - Advisory teachers remain with their assigned sections.
  - Homeroom, recess, and lunch breaks are scheduled correctly.
  - Subjects are evenly distributed among teachers.
- **Data Export & Filtering**: Export schedules to **Excel** and filter by teacher, section, or room.
- **Dynamic Room Assignment**: Ensures room availability while considering student capacity.

## Technologies Used
- **Backend**: Python
- **Database**: MySQL (PhpMyAdmin)
- **Frontend**: HTML, CSS, JavaScript (if applicable)
- **Data Manipulation**: CSV/Excel

## Hard Constraints (Must Be Satisfied)
1. **No Teacher Conflicts** – A teacher cannot be scheduled to teach multiple subjects at the same time.
2. **No Room Conflicts** – A room can only have one class at a time.
3. **No Student Group Conflicts** – A student group can only attend one subject at a time.
4. **Correct Room Type** – Laboratory subjects must be assigned to laboratory rooms. Lecture subjects can be in any room.
5. **Part-Time Teacher Restriction** – Part-time teachers can only teach on Saturdays.
6. **School Hours Restriction** – Classes must be scheduled between **8:00 AM and 5:00 PM**.
7. **Lunch Break Restriction** – No classes between **12:00 PM and 1:00 PM**.
8. **Course-Year Level Match** – A student group must take only subjects that match their course and year level.
9. **Teacher Subject Specialization** – Teachers can only teach subjects they are assigned to.
10. **Required Weekly Lecture Hours** – Each subject has a required number of lecture hours per week, which must be scheduled.
11. **Continuous Lesson Slots** – Subjects requiring multiple hours should have continuous time slots where possible.
12. **All Subjects Must Be Scheduled** – If a subject cannot be scheduled due to constraints, it is flagged as "unassigned" and reported.

## Soft Constraints (Preferable but Can Be Violated)
1. **Balanced Schedule Distribution** – Avoid scheduling all hours of a subject on the same day. Spread subjects across multiple days where possible.
2. **Evenly Distribute Classes Across Days** – Prioritize underutilized days (e.g., Tuesday and Wednesday) over heavily scheduled ones (e.g., Monday and Friday).
3. **Teacher Room Stability** – Teachers prefer to teach in the same room whenever possible.
4. **Teacher Time Efficiency** – Teachers prefer sequential lessons with minimal gaps between their classes.
5. **Student Group Subject Variety** – Avoid scheduling the same subject multiple times in a row to increase variety in student learning.
6. **Minimize Teacher Gaps** – Reduce the number of free periods between a teacher’s lessons to optimize their schedule.

## Database Schema

### Tables
- **rooms** (`room_id`, `room_name`, `capacity`)
- **schedule_table** (`schedule_id`, `subject_name`, `teacher_name`, `room_name`, `day`, `start_time`, `end_time`, `section`, `semester`)
- **sections** (`section_id`, `program`, `year_level`, `num_students`, `section_name`, `adviser_last_name`, `adviser_first_name`)
- **subjects** (`subject_code`, `year_level`, `program`, `hours_per_week`, `semester`)
- **teachers** (`teacher_id`, `teacher_first_name`, `teacher_last_name`, `subject_name`, `section_advisory`, `teacher_type`)
- **time_slots** (`timeslot_id`, `day`, `start_time`, `end_time`)

## Installation & Setup

### Prerequisites
1. Install **Python** and required libraries.
2. Set up **MySQL** and import the provided database schema.
3. Configure the database connection in the Python script.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/class-scheduler.git
   cd class-scheduler
