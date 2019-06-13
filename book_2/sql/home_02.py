import sqlite3

with sqlite3.connect('cars.db') as conn:
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE cars SET quantity=9 WHERE model='ka'")
    cursor.execute(
        "UPDATE cars SET quantity=11 WHERE model='jazz'"
        )

    rows = cursor.fetchall()

    for row in rows:
        print(row)
