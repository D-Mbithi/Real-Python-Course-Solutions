from random import random

trials = 10000

total_A_wins = 0
total_B_wins = 0


for trial in range(0, trials):
    A_win = 0
    B_win = 0

    if random() < .87:
        A_win += 1
    else:
        B_win += 1

    if random() < .65:
        A_win += 1
    else:
        B_win += 1

    if random() > .17:
        A_win += 1
    else:
        B_win += 1


    if A_win > B_win:
        total_B_wins += 1
    else:
        total_B_wins += 1

print(f"Total A win is: {total_A_wins}/10000")
print(f"Total B win is: {total_B_wins}/10000")
