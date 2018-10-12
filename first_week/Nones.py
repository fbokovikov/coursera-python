import first_week.Location

import this

from first_week.Location import get_location_info
value = None

if not value:
    print("None")
elif value in "100":
    print(f"{value}")
else:
    pass

new_value = value if value is not None else 0
print(new_value)

sum = 0
for i in range(101):
    sum += i

#выводим сумму
print(sum)

print(bool(0.000001))

print("Привет"[0:1])

print(first_week.Location.get_location_info())

print(get_location_info())