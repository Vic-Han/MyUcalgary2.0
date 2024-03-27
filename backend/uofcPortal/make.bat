@echo off

rem Delete the SQLite database file
del db.sqlite3
del migrations\0001_initial.py

rem Make migrations
python manage.py makemigrations

rem Apply migrations
python manage.py migrate

rem Load data
rem Replace 'your_fixture.json' with the actual name of your fixture file
rem python manage.py loaddata dummy_data.json

python manage.py loaddata 01_users.json
python manage.py loaddata 02_faculty.json
python manage.py loaddata 03_departments.json
python manage.py loaddata 04_program.json
python manage.py loaddata 05_term.json
python manage.py loaddata 06_emergency_contact.json
python manage.py loaddata 07_address.json
python manage.py loaddata 08_student.json
python manage.py loaddata 09_course.json
python manage.py loaddata 10_instructor.json
python manage.py loaddata 11_lecture.json
python manage.py loaddata 12_tutorial.json
python manage.py loaddata 13_enrollment.json
python manage.py loaddata 14_grade.json
python manage.py loaddata 15_transaction.json
python manage.py loaddata 16_application.json
python manage.py loaddata 17_requirement.json

rem Run the server
python manage.py runserver