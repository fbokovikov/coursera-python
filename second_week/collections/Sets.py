import random

number_set = {1, 2, 3, 4, 5, 3}

print(set)

odd_set = set()
even_set = set()

for number in range(10):
    if number % 2 == 1:
        odd_set.add(number)
    else:
        even_set.add(number)

print(odd_set | even_set)
print(odd_set - even_set)

random_set = set()

while True:
    new_number = random.randint(1, 10)
    if new_number in random_set:
        break

    random_set.add(new_number)

print(len(random_set) + 1)

