from datetime import datetime


def show_date() -> None:
    print('This is the current date and time: ')
    print(datetime.now())


def greet(name: str) -> None:
    print(f'Hello, {name}!')


# Easily changable to something close to the original one
def greet_chinese(name: str) -> None:
    print(f'Nihao, {name}!')

# With return type we can also not use the return type its just a better for debugging


def add(a: float, b: float) -> float:
    return a+b


show_date()
greet('bob')
greet('marley')

greet_chinese('bob')
greet_chinese('marley')

print(add(1, 4))
