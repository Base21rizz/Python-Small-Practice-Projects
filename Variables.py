first_name = "John"
last_name = "Doe"
full_name = "Lemon Soda"
Country = "USA"
city = "New York"
age = 30
year = 2024
is_married = False
is_true = True
is_light_on = True
a, b, c = 5, 10.5, 15.7


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(Country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))


print("First name length:", len(first_name))
print("Last name length:", len(last_name))
if len(first_name) > len(last_name):
    print("First name is longer than last name")
else:
    print("Last name is longer than first name")
Num_one = 5
Num_two = 4
total = Num_one + Num_two
divide = Num_one / Num_two
remainder = Num_two % Num_one
exp = Num_one ** Num_two
floor_div = Num_one // Num_two

radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

r = input("Enter Radius: ")
area = 3.14 * float(r) ** 2
print("Area of circle with radius", r, "is:", area)
circumference = 2 * 3.14 * float(r)
print("Circumference of circle with radius", r, "is:", circumference)
