def celcius(temp):
    fahrenheit = temp * (9/5) + 32

    return fahrenheit


def fahrenheit(temp):

    celcius = (temp - 32) * (5/9)

    return celcius


print(celcius(50), "celcius")
print(fahrenheit(50), "fahrenheit")
