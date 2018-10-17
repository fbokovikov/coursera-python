from datetime import datetime


def get_seconds():
    """Return current seconds"""
    return datetime.now().second


print(get_seconds())

print(get_seconds.__name__)
print(get_seconds.__doc__)


def add(x: int, y: int) -> int:
    return x * 2 + y * 3


print(add(15, 10))

print(add('qw', 'erty'))

print(add(y=15, x=10))

print(add.__defaults__)


def printer(*args):
    print(type(args))

    for arg in args:
        print(arg)


def printer2(**args):
    print(type(args))

    for k, v in args.items():
        print(k, v)


printer(1, 2, 3)
printer()
printer2(a=1, b=2)
printer2()
