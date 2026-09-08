class Car:
    def __init__(self, Brand: str, horsepower: int) -> None:
        self.Brand = Brand
        self.horsepower = horsepower

    def drive(self) -> None:
        print(f'{self.Brand} is driving!')

    def get_info(self) -> None:
        print(f'Brand = {self.Brand}, Horsepower = {self.horsepower}')


volvo: Car = Car('Volvo', 200)
volvo.get_info()
volvo.drive()

bmw: Car = Car('bmw', 250)
bmw.get_info()
bmw.drive()
