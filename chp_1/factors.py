def factor(num):
    for i in range(1, num+1):
        if num % i == 0:
            print("{} is a divisor of {}".format(i, num))

num = int(input("Enter a number: "))


factor(num)
