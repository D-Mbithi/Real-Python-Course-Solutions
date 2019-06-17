import sys
import pdb
from random import choice

random1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while True:
    print("To exit the game type 'exit'. ")
    num1 = choice(random1)
    num2 = choice(random2)
    answer = input("What is {} times {} ?".format(num1, num2))


    if answer == 'exit':
        print('Game exiting now ....')
        sys.exit()
    elif int(answer) == num1 * num2:
        print("Corect")
    else:
        print("Wrong answer!")
