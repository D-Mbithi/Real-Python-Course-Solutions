import sqlite3

with sqlite3.connect('new.db') as conn:
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT population.city, population.population, regions.region
        FROM population, regions
        WHERE population.city = regions.city
        """
    )

    rows = cursor.fetchall()

    for row in rows:
        print("City:", row[0])
        print("Population:", row[1])
        print("Region:", row[2])
        print("---------------------------")
