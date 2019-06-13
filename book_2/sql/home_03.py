import sqlite3

with sqlite3.connect('cars.db') as conn:
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM cars WHERE make='Ford'"
        )
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)
