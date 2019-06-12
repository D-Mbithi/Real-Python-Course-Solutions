import sqlite3

conn = sqlite3.connect('new.db')

cursor = conn.cursor()

cursor.execute(
        "INSERT INTO population VALUES('New York City', 'NY', 8400000)"
        )
cursor.execute(
        "INSERT INTO population VALUES('San Francisco', 'CA', 8000000)"
        )

conn.commit()

cursor.close()
