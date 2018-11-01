from random import random

trials = 10000

canditate_A_wins = 0
canditate_B_wins = 0

# loop throught the set number of trials
for trial in range(0,trials):
    A_win = 0
    B_win = 0

    # check winner of region 1
    if random() < 0.87:
        A_win += 1
    else:
        B_win += 1

    # check winner of region 2
    if random() < 0.65:
        A_win += 1
    else:
        B_win += 1

    # check winner of region 3
    if random() < 0.17:
        A_win += 1
    else:
        B_win += 1


    # check the overall winner
    if A_win < B_win:
        canditate_B_wins += 1
    else:
        canditate_A_wins += 1

print("Canditate A average wins: {}/10000".format( canditate_A_wins))
print("Canditate B average wins: {}/10000".format(canditate_B_wins))

