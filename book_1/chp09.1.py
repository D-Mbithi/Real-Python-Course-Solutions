poem = open('./poem.txt', 'r')

for line in poem.readlines():
    print(line)

poem.close()

print("\n\nEnd of Poem")
