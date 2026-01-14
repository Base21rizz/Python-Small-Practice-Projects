# Functions
def sum_numbers(nums):
    return sum(nums)


def sum_using_HOF(f, lst):
    summation = f(lst)
    return summation


def square(x):
    return x**2


def cube(x):
    return x**3


def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)


def Function_as_return_value(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


# Main Part
""" result1 = sum_numbers(1, 2, 3, 4, 5) = 15
    print(result1)
    This is wrong it is here just to understand """

result2 = sum_using_HOF(sum_numbers, [1, 2, 3, 4, 5])
print(result2)

result_FARV = Function_as_return_value('square')
print(result_FARV(3))
result_FARV = Function_as_return_value('cube')
print(result_FARV(3))
result_FARV = Function_as_return_value('absolute')
print(result_FARV(-3))
