empty_dictonary_dog = {}
dog = {'name': 'tommy', 'color': 'white',
       'breed': 'poodle', 'legs': '4', 'age': '5'}
print(dog)
student = {'first_name': 'John', 'last_name': 'Doe', 'gender': 'Male', 'age': 25, 'marital_status': 'Single',
           'skills': ['Python', 'JavaScript', 'C++'], 'country': 'USA', 'city': 'New York', 'address': '123, 5th Avenue'}
print(student)
print(len(student))
print(type(student['skills']))  # List

student['skills'].append('Java')
student['skills'].append('Rust')
print(student['skills'])

print(student.keys())  # Changing dictonary_keys to list
print(student.values())  # Changing dictonary_values to list
print(student.items())  # Changing dictonary_items to list of tuples

print("Before Deleting marital status:")
print(student)
del student['marital_status']
print("After Deleting marital status:")
print(student)

del student
print("After deleting the dictonaries:")
# print(student) NameError: name 'student' is not defined
