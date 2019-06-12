# insert data from cvs
import os
import csv
import sqlite3

with sqlite3.connect('new.db') as connection:
    cursor = connection.cursor()

    employee_file =  os.path.join(os.getcwd(), 'employees.csv') 
     
    employees = csv.reader(open(employee_file, 'r'))

    try:
        cursor.execute(
            "CREATE TABLE employees(firstname TEXT, lastname TEXT)"
            )
    except sqlite3.OperationalError:
        print("Database table already exist")

    cursor.executemany("INSERT INTO employees VALUES(?, ?)", employees)
