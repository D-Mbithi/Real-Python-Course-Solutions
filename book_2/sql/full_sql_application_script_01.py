import sqlite3
import random


with sqlite3.connect('nums.db') as conn:
    cursor = conn.cursor()

    cursor.execute(
        "DROP TABLE if exists numbers"
        )

    cursor.execute(
        "CREATE TABLE numbers(num INT)"
        )

    for num in range(0,100):
        cursor.execute(
            "INSERT INTO numbers VALUES(?)", (random.randint(0,100),))
