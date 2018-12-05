with open("poem.txt", "r") as poem , open("output2.txt", "w") as output:
    for line in poem.readlines():
        output.writelines(line)
