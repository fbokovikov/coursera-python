import random

empty_list = []

empty_list = list()

none_list = [None] * 10

print(len(none_list))

collections = ['list', 'tuple', 'dict', 'set']
print(collections)

print(collections[0])
print(collections[-1])

collections[3] = 'frozenSet'

print(collections)

if 'tuple' in collections:
    print(True)

print(collections[0:3])

for idx, collection in enumerate(collections):
    print(idx, collection)

collections.append('Map')

collections += 'None'

del collections[4]

print(max(collections))

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 100))

print(sorted(numbers))

numbers.sort(reverse=True)

print(numbers)

#неизменяемый список
empty_tuple = tuple()

one_element_tuple = (1,)

print(type(one_element_tuple))