from random import randint

dice = randint(1,6)

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for role in range(10000):
    if randint(1,6) == 1:
        one += 1
    elif randint(1,6) == 2:
        two += 1
    elif randint(1,6) == 3:
        three += 1
    elif randint(1,6) == 4:
        four += 1
    elif randint(1,6) == 5:
        five += 1
    elif randint(1,6):
        six += 1


print("One {}/10000".format(one))
print(f"two {two}/10000")
print(f"three {three}/10000")
print(f"four {four}/10000")
print(f"five {five}/10000")
print(f"six {six}/10000")
