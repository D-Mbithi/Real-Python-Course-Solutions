birthday = {}

print(birthday, '\n')

birthday['Luke Skywalker'] = '5/24/19'
birthday['Obbi-Wan Kenobbi'] = '3/11/57'
birthday['Darth Vader'] = '4/1/41'

print(birthday, '\n')

names = ['Yoda', 'Darth Vader']

for name in names:
    if name in birthday:
        print(name, birthday[name], '\n')
    else:
        birthday[name] = 'unknow'
        print(name, 'birthday unknow', '\n')

print(birthday, '\n')

for name in birthday:
    print(name, birthday[name])

del(birthday['Yoda'])

print(birthday)


birthday = dict([('Luke Skywalker', '5/24/19'),('Obbi-wan Kenobi', '3/11/54'),('Darth Vader', '4/1/41')])

print(birthday)
