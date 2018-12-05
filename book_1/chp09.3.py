poem = open("poem.txt", "r")

output = open("output.txt", "w")

for line in poem.readlines():
    output.writelines(line)

poem.close()
output.close()
