class Car:
    # ... (This can be used as a place holder)
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower
        # Normally without any return type it will return none
        # but its better practise to use None as return type

    # Methods that start and end with double underscores in short dunder methods aka magic methods
    def __str__(self) -> str:
        return f'{self.brand}, {self.horsepower}hp'

    def __add__(self, other) -> str:
        return f'{self.brand} & {other.brand}'


volvo: Car = Car('volvo', 200)  # Creates a instance of that car
print(volvo)
bmw: Car = Car('bmw', 250)
print(bmw)
print(volvo + bmw)
