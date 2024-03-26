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
python3 manage.py loaddata dummy_data.json

# Run the server
python3 manage.py runserver