import sqlite3

with sqlite3.connect('cars.db') as conn:
    cursor = conn.cursor()

    cursor.execute(
        "select make, model, count(*) from orders group by model"
        )
    rows = cursor.fetchall()

    for row in rows:
        print("Make:", row[0], '-', 'Model:', row[1])
        print("Quantity:", row[2])
