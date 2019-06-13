"""Insert the inventory data."""

import sqlite3

with sqlite3.connect('cars.db') as conn:
    cursor = conn.cursor()

    cars = [
        ('Ford', 'range', 5),
        ('Ford', 'ka', 4),
        ('Ford', 'fiesta', 3),
        ('Honda', 'civic', 7),
        ('Honda', 'jazz', 6)
    ]

    cursor.executemany(
        "INSERT INTO cars VALUES(?, ?, ?)", cars
        )
