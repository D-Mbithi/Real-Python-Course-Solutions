import sqlite3

with sqlite3.connect('cars.db') as conn:
    cursor = conn.cursor()

    cursor.execute(
        "SELECT cars.make, cars.model, cars.quantity, orders.order_date FROM cars INNER JOIN orders ON cars.model = orders.model"
    )

    rows = cursor.fetchall()

    for row in rows:
        print("Make:",row[0],' - ',"Model:",row[1])
        print("Quanity:",row[2])
        print("Order Date:", row[3])
        print()
