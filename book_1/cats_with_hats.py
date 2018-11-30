cats_without_hats = list(range(1,100+1))
cats_with_hats = []

for i in cats_without_hats:
    for j in cats_without_hats:
        if j % i == 0:
            if j not in cats_with_hats:
                cats_with_hats.append(j)
            else:
                cats_with_hats.remove(j)

print(cats_with_hats)
