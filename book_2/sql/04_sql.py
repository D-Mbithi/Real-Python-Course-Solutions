import sqlite3

with sqlite3.connect('new.db') as connection:

    cursor = connection.cursor()

    cursor.execute(
            "INSERT INTO population VALUES('Boston', 'MA', 6000000)"
            )
    cursor.execute(
            "INSERT INTO population VALUES('Chicago', 'IL', 2700000)"
            )
