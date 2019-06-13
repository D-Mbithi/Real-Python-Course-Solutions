import sqlite3

with sqlite3.connect('new.db') as conn:

    cursor = conn.cursor()

    cursor.execute('SELECT firstname, lastname FROM employees')

    data = cursor.fetchall()

    for row in data:
        print(row[0], row[1])
