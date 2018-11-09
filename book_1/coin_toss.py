from random import randint


trials = 10000

flips = 0


for trial in range(0, trials):
    flips += 1

    if randint(0,1) == 1:
        while randint(0,1) == 1:
            flips += 1
    else:
        while randint(0,1) == 0:
            flips += 0

print(f"Flips average: {flips}/10000")

