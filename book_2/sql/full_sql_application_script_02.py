import sqlite3

with sqlite3.connect('nums.db') as conn:
    cursor = conn.cursor()

    while True:
        print(
            """
            Select number of operation:
            1. Avg
            2. Max
            3. Min
            4. Sum
            5. Count
            """
            )
        num = input("Enter Number:")

        if num in set(['1', '2', '3', '4']):

            operation = {1: 'avg', 2: 'max', 3: 'min', 4: 'sum', 5: 'count'}[int(num)]

            cursor.execute(f"SELECT {operation}(num) FROM numbers")

            get = cursor.fetchone()

            print(operation, ": %f" % get[0])

        elif num == '5':
            print('Exit')

            break





        



