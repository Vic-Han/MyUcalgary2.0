#!/bin/bash

# Delete the SQLite database file
rm -f db.sqlite3
rm -f migrations/0001_initial.py

# Make migrations
python3 manage.py makemigrations

# Apply migrations
python3 manage.py migrate

# Load data
# Replace 'your_fixture.json' with the actual name of your fixture file
#python3 manage.py loaddata dummy_data.json

python3 manage.py loaddata 01_users.json
python3 manage.py loaddata 02_faculty.json
python3 manage.py loaddata 03_departments.json
python3 manage.py loaddata 04_program.json
python3 manage.py loaddata 05_term.json
python3 manage.py loaddata 06_emergency_contact.json
python3 manage.py loaddata 07_address.json
python3 manage.py loaddata 08_student.json
python3 manage.py loaddata 09_course.json
python3 manage.py loaddata 10_instructor.json
python3 manage.py loaddata 11_lecture.json
python3 manage.py loaddata 12_tutorial.json
python3 manage.py loaddata 13_enrollment.json
python3 manage.py loaddata 14_grade.json
python3 manage.py loaddata 15_transaction.json
python3 manage.py loaddata 16_application.json
python3 manage.py loaddata 17_requirement.json

# Run the server
python3 manage.py runserver