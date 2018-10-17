from functools import reduce
from functools import partial


def caller(func, params):
    return func(*params)


def printer(name, origin):
    print(name, origin)


caller(printer, ['1', 2])


def get_multiplier():
    def inner(a, b):
        return a * b
    return inner


multiplier = get_multiplier()
multiplier(10, 11)

print(multiplier.__name__)


def squarify(a):
    return a ** 2


print(list(map(squarify, range(5))))


def is_positive(a):
    return a > 0


print(list(filter(is_positive, range(-2, 3))))


print(list(map(lambda x: x ** 2, range(5))))


def to_string_list(numbers):
    return list(map(str, numbers))


print(to_string_list([1, 3, 5]))


def multiply(a, b):
    return a * b


print(reduce(multiply, [1, 2, 3, 4, 5]))


multiply_10 = partial(multiply, b = 10)

print(multiply_10(10))


square_list = [number ** 2 for number in range(10) if number % 2 == 0]
print(square_list)


square_map = {number: number ** 2 for number in range(10)}
print(square_map)


reminders_set = {number % 10 for number in range(50, 100)}
print(reminders_set)


num_list = range(7)
squared_list = [x ** 2 for x in num_list]

print(list(zip(num_list, square_list)))