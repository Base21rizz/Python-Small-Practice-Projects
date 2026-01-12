language = 'pyhton'
lst = [i for i in language]
print(type(lst))
print(lst)

# generate number from 1-19
number = [i for i in range(19)]
print(number)

# generating squares in range using list comprehension 1^2-10^2
squares = [i*i for i in range(11)]
print(squares)

# Making list of tuples using using list comprehension
numbers = [(i, i * i) for i in range(11)]
print(numbers)
