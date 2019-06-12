import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE cars(
        make TEXT,
        model TEXT,
        quantity INT
        )
        """)

cursor.close()
