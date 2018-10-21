import random

x, y, z = (random.randint(0, 1000) % 10 for _ in range(3))

print(type((random.randint(0, 1000) % 10 for _ in range(3))))

print(type({random.randint(0, 1000) % 10 for _ in range(3)}))

print(type([random.randint(0, 1000) % 10 for _ in range(3)]))


def generate_rand(i):
    return random.randint(0, 25)


for idx, val in enumerate((generate_rand(0) for _ in range(3))):
    print(f"{idx}={val}")

list = list(map(generate_rand, range(10)))
print(list)