empty_dict = {}
empty_dict = dict()

collections_map = {
    'mutable': ['list', 'set', 'dict'],
    'immutable': ['tuple', 'frozenset']
}

print(collections_map)

print(collections_map.get('bad', 'not_found'))

mutable = collections_map.pop('mutable')

print(mutable)

for key in collections_map:
    print(key)

for key, value in collections_map.values():
    print(f"{key}, {value}")

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

for row in matrix:
    print(row)