import sqlite3

people_values = (
        ('Ron', 'Obvious', 42),
        ('Luigi', 'Vercotti', 43),
        ('Arthur', 'Belling', 28)
        )

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName Text, LastName Text, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)

    c.execute("SELECT FirstName, LastName, Age FROM People WHERE AGE < 30")

    for row in c.fetchall():
        print(row)
