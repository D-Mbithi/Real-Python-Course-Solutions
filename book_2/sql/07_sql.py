import sqlite3

with sqlite3.connect('new.db') as conn:
    cursor = conn.cursor()

    for row in cursor.execute('SELECT firstname, lastname from employees'):
        print(row)
