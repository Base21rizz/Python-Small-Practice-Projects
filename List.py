lst = []
fruits = ['Lemon', 'Apple', 'Mango', 'Banana', 'Orange']
print(fruits)
print(fruits[0])
print(fruits[2])
print(fruits[-1])
mixed_data_types = ('Shoumik', 21, 6.1, False, 'Bangladesh')
IT_companies = ['facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']
first_item, second_item, third_item, * \
    rest = IT_companies  # Naming for printing List items
print(mixed_data_types)
print(IT_companies)
print(len(IT_companies))
print(IT_companies[0])
print(IT_companies[3])
print(IT_companies[-1])

IT_companies[3] = 'Intel'
print(IT_companies[0:3])
print(IT_companies[3])
print(rest)
print(IT_companies)

IT_companies.append('Twitter')
print(IT_companies)
IT_companies.insert(4, 'Uber')
print(IT_companies)

IT_companies[2] = IT_companies[2].upper()  # upper case
print(IT_companies)

print('Companies:', '# '.join(IT_companies))

print("Is 'IBM' in the list?", 'IBM' in IT_companies)
print("Is 'Meta' in the list?", 'Meta' in IT_companies)

IT_companies.sort()
print(IT_companies)
IT_companies.reverse()
print(IT_companies)


del IT_companies[0:3]
print(IT_companies)

del IT_companies[3:6]
print(IT_companies)

del IT_companies[1]
print(IT_companies)

IT_companies = ['facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']  # reset list
print(IT_companies)
IT_companies.pop(0)
print(IT_companies)  # popped company first

IT_companies = ['facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']  # reset list
IT_companies.pop(3)
print(IT_companies)  # popped company middle

IT_companies = ['facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']  # reset list
IT_companies.pop(-1)
print(IT_companies)  # popped company last

IT_companies.clear()
print(IT_companies)

del IT_companies
print('IT_companies Deleted')

Front_End = ['HTML', 'CSS', 'JS', 'React', 'Redux']
print("Front_End:", Front_End)
Back_End = ['Node', 'Express', 'MongoDB']
print("Back_End:", Back_End)
Joined = Front_End + Back_End
print("Joined:", Joined)

Full_Stack = Joined.copy()
Full_Stack.insert(5, 'Python')
Full_Stack.insert(6, 'SQL')
print("Full_Stack:", Full_Stack)
