import sqlite3

with sqlite3.connect('new.db') as conn:
    cursor = conn.cursor()

    cities = [
            ('Huston', 'TX', 2100000),
            ('Phoenix', 'AZ', 1500000)
            ]

    cursor.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
