import sqlite3

data = (
        ('Jean-Baptiste Zorg', 'Human', 122),
        ('Korben Dallas', 'Meat Popsicle', 100),
        ("Ak'not", 'Magalore', -5)
        )

with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()

    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster('Name', 'Species', 'IQ')")
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", data)

    c.execute("SELECT * FROM Roster")

    for row in c.fetchall():
        print(row)

    print()

    c.execute("UPDATE Roster SET Species=? WHERE NAME=?", ('Human', 'Korben Dallas'))
    c.execute("SELECT * FROM Roster")

    for row in c.fetchall():
        print(row)
