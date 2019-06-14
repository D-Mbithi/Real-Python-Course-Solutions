import sqlite3

with sqlite3.connect('new.db') as conn:
    cursor = conn.cursor()

    sql = {
        'average': "SELECT avg(population) FROM population",
        'maximum': "SELECT max(population) FROM population",
        'minimux': "SELECT min(population) FROM population",
        'sum': "SELECT sum(population) FROM population",
        'count': "SELECT count(population) FROM population",
        }

    for keys, values in sql.items():
        cursor.execute(values)

        result = cursor.fetchone()

        print(keys,':',result[0])
