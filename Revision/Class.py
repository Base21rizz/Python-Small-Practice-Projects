class Car:
    # ... (This can be used as a place holder)
    def __init__(self, color: str, horsepower: int) -> None:
        self.color = color
        self.horsepower = horsepower
        # Normally without any return type it will return none
        # but its better practise to use None as return type


volvo: Car = Car('Red', 200)  # Creates a instance of that car
print(volvo.color)
print(volvo.horsepower)

bmw: Car = Car('blue', 250)  # Creates a instance of that car
print(bmw.color)
print(bmw.horsepower)
