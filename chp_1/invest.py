def invest(amount, rate, time):
    print("Principal amount", amount)
    print()
    print("annual rate of return:")
    print()
    for year in range(time):
        amount = amount + (amount * rate)
        print("year {}: ${}".format(year+1, amount))
    print()

print(invest(100, .05, 8))
print(invest(2000, .025, 5))
