import sqlite3

with sqlite3.connect('new.db') as connect:
    cursor = connect.cursor()
    
    try:
        cursor.execute(
            "CREATE TABLE regions (city TEXT, region TEXT)"
            )
    except sqlite3.OperationalError:
        print("Table already exist.")
        print("--------------------------")

    cities = [
        ('New York City', 'Northeast'),
        ('San Francisco', 'West'),
        ('Chicago', 'Midwest'),
        ('Houston', 'South'),
        ('Phoenix', 'West'),
        ('Boston', 'Northeast'),
        ('Los Angeles', 'West'),
        ('Houston', 'South'),
        ('Philadelphia', 'Northeast'),
        ('San Antonio', 'South'),
        ('San Diego', 'West'),
        ('Dallas', 'South'),
        ('San Jose', 'West'),
        ('Jacksonville', 'South'),
        ('Indianapolis', 'Midwest'),
        ('Austin', 'South'),
        ('Detroit', 'Midwest')
    ]

    cursor.executemany("INSERT INTO regions VALUES(?,?)", cities)

    cursor.execute('SELECT * FROM regions ORDER BY region ASC')

    rows = cursor.fetchall()

    for row in rows:
        print(row[0], row[1])
