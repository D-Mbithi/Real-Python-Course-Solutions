from capitals import capitals_dict
import random

state = random.choice(list(capitals_dict.keys()))

# print(state)

city = capitals_dict[state]
city = city.lower()

# print(city)

flag = True
while flag:
    user = input("Enter the capital city of {}:".format(state))
    user = user.lower()

    if user  == city:
        print("Correct")
        flag = False
    elif user == 'exit':
        print("GoodBye")
        break
    else:
        print("Try again")
