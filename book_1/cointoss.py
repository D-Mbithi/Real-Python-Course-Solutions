from random import randint

toss = randint(0,1)

head = 0
tail = 0

if toss == 0:
    head += 1
else:
    tail += 1

print(f"Heads {head}")
print(f"Tails {tail}")
