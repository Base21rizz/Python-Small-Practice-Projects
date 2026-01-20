try:
    name = input('Enter your name: ')
    year_born = input('year you born: ')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}')
except:
    print(e)
