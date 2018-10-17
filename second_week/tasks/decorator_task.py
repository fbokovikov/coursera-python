import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped


@to_json
def get_data(a, b):
    return {
        "a" : 42
    }


print(get_data(10, b=16))  # вернёт '{"data": 42}'