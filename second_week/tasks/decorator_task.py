import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if args and kwargs:
            return json.dumps(func(args, kwargs))
        elif args:
            return json.dumps(func(args))
        elif kwargs:
            return json.dumps(func(kwargs))
        else:
            return json.dumps(func())

    return wrapped


@to_json
def get_data():
    return None


get_data()  # вернёт '{"data": 42}'