import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as conn:

    c = conn.cursor()
 
    c.execute("DROP TABLE IF EXISTS tasks")

    c.execute(
        """
        CREATE TABLE tasks(
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            due_date TEXT NOT NULL,
            priority INTEGER NOT NULL,
            status INTEGER NOT NULL)
        """
        )

    tasks = [
        ('website design', '25/03/2019', 10, 1),
        ('wireframe design', '11/06/2019', 8, 1),
        ('django development', '12/01/2019', 9, 1),
        ('website development', '05/09/2019', 4, 1)
        ]

    c.executemany("INSERT INTO tasks(name, due_date, priority, status) VALUES(?,?,?,?)", tasks)
