Brothers = ("Lamor", "Shoumik", "Ktiz")
Sisters = ("Shamima", "Shila", "Fariha")
Siblings = Brothers + Sisters
print("No of siblings:", len(Siblings))
Family_members = Siblings + ("Ashik", "Lema")
print("Number of Family Members:", len(Family_members))
del Family_members
Fruits = ("Banana", "Orange", "Mango", "Kiwi", "Lichi")
Vegitables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
Animal_products = ("Milk", "Meat", "Egg")
Food_stuff_tp = Fruits + Vegitables + Animal_products
Food_stuff_It = Food_stuff_tp
del Food_stuff_tp
Slice_1 = Food_stuff_It[:3]
Slice_2 = Food_stuff_It[:-3]
for item in Slice_1:
    print(item)
for item in Slice_2:
    print(item)
x = input("Enter a Nordic Country name: ")
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
if x in nordic_countries:
    print(x, " is a nordic country")
else:
    print("Is not a nordic country")
