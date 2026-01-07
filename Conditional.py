# Grade from result
x = int(input("Enter your result: "))
if x >= 80 and x <= 100:
    print("A")
elif x >= 70 and x <= 79:
    print("B")
elif x >= 60 and x <= 69:
    print("C")
elif x >= 50 and x <= 59:
    print("D")
elif x >= 0 and x <= 49:
    print("F")

# Season from month
month = input("Enter month: ").lower()
if month in ['september', 'october', 'november']:
    print("The season is Autumn")
elif month in ['december', 'january', 'february']:
    print("The season is Winter")
elif month in ['march', 'april', 'may']:
    print("The season is Spring")
elif month in ['june', 'july', 'august']:
    print("The season is Summer")

# Fruits update based on provided list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_check = input("Enter fruit name: ").lower()
if fruit_to_check in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit_to_check)
    print("Fruit added to the list")

# Dictonary operations
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    print(person['skills'][int(len(person['skills']) / 2)])  # middle skill
    if 'Python' in person['skills']:
        print("Python is one of the skills")
    else:
        print("Python is not one of the skills")
if 'Javascript' and 'React' in person['skills']:
    print("He is a front end developer")
if 'React' and 'Node' and 'MongoDB' in person['skills']:
    print("He is a fullstack developer")
else:
    print("Unknown Title")

if person['is_married'] and person['country'] == 'Finland':
    print("Asaveneh Yetaueh lives in Finland. He is married.")
