string = 'Курс про "Python"'
print(string)

dir = r"Файл на диске C://"
print(dir)

long_string = "Начало " \
    "Середина " \
    "Конец"

print(long_string)

new_string = """Строка 
с абзацами
"""

print(new_string)

print(string[5::])
print(string[::-1])

print(string.count("р"))

print("Файл" in dir)

for letter in string:
    print(letter)

template = "%s %s"
print(template % ("Привет,", "мир"))

print("{}, {}".format("Привет", "мир"))

print(f"{string}")

name = input("Введите имя: ")
print(f"{name}")