import sqlite3

with sqlite3.connect('cars.db') as conn:
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)
            """)
    except sqlite3.OperationalError:
        print("Table already exist.")

    orders = [
        ('Ford', 'range', '2019-06-12'),
        ('Ford', 'range', '2019-04-05'),
        ('Ford', 'range', '2019-01-22'),
        ('Ford', 'ka', '2019-04-10'),
        ('Ford', 'ka', '2019-07-23'),
        ('Ford', 'ka', '2019-01-11'),
        ('Ford', 'fiesta', '2019-03-19'),
        ('Ford', 'fiesta', '2019-05-20'),
        ('Ford', 'fiesta', '2019-04-21'),
        ('Honda', 'civic', '2019-06-01'),
        ('Honda', 'civic', '2019-02-01'),
        ('Honda', 'civic', '2019-11-21'),
        ('Honda', 'jazz', '2019-04-13'),
        ('Honda', 'jazz', '2019-10-15'),
        ('Honda', 'jazz', '2019-03-27')
        ]

    cursor.executemany("INSERT INTO orders VALUES(?,?,?)", orders)
