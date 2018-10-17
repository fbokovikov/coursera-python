def even_range(start, end):
    current = start;
    while current < end:
        yield current
        current += 2


for number in even_range(0, 10):
    print(number)


ranger = even_range(0, 4)

print(next(ranger))


def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b


print(list(fibonacci(25)))


def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value


generator = accumulator()

next(generator) # 0

generator.send(1)