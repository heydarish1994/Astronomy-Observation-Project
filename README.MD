# Astronomy Observation Project

A Python project for recording and analyzing astronomical observations.

## Project Structure

Astronomy Observation Project
│
├── main.py
├── observation.py
├── database.py
├── visual.py
└── README.md
Features
Add astronomical observations
Show observations
Search observations
Update observations
Delete observations
Store data in SQLite
Export data to CSV
Analyze data with Pandas
Calculate statistics with NumPy
Create charts with Matplotlib
Filter and sort observations
Group observations by observer and target
File Responsibilities
main.py

Contains the main menu, input handling, and program flow.

observation.py

Contains the Observation class and the function:

observation_from_row()
database.py

Handles SQLite database operations:

Create table
Add observation
Get observations
Search observations
Update observations
Delete observations
Export data to CSV
visual.py

Uses Pandas, NumPy and Matplotlib for:

DataFrame creation
Data inspection
Searching
Filtering
Sorting
Sum and mean calculations
Grouping
Charts
README.md

Contains information about the project.

Libraries

The project uses:

Python
SQLite
Pandas
NumPy
Matplotlib
CSV
Run the Project

Open the project folder in VS Code and run:

python main.py

The SQLite database is created automatically.

Python Concepts Used

This project uses concepts learned in the Python course:

Variables
Input and output
Conditions
Loops
Functions
Parameters
Return values
Strings
Lists
Dictionaries
Exception handling
Classes
Objects
Methods
SQLite and SQL
Pandas
NumPy
Matplotlib
CSV