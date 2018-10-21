import csv
from os.path import splitext


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        """Получить расширение файла"""
        _, ext = splitext(self.photo_file_name)
        return ext

    def __str__(self):
        return "type = {0}, brand = {1}, photo = {2}, carry = {3}".format(
            self.car_type,
            self.brand,
            self.photo_file_name,
            self.carrying
        )

    def __repr__(self):
        return str(self)


class Car(CarBase):
    car_type = "car"

    def __init__(
            self,
            brand,
            photo_file_name,
            carrying,
            seats_count
    ):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = seats_count

    def __str__(self):
        return super().__str__() + ", seats_count={0}".format(self.passenger_seats_count)


class Truck(CarBase):
    car_type = "truck"

    def __init__(self, brand, photo_file_name, carrying, whl):
        super().__init__(brand, photo_file_name, carrying)
        # обрабатываем поле body_whl
        try:
            length, width, height = (float(c) for c in whl.split("x", 2))
        except ValueError:
            length, width, height = .0, .0, .0

        self.body_length = length
        self.body_width = width
        self.body_height = height

    def __str__(self):
        return super().__str__() + ", width={0}, height={1}, length={2}".format(
            self.body_width,
            self.body_height,
            self.body_length
        )

    def get_body_volume(self):
        """Получить объем кузова"""
        return self.body_length * self.body_height * self.body_width


class SpecMachine(CarBase):
    car_type = "spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    def __str__(self):
        return super().__str__() + ", extra={0}".format(self.extra)


def get_car_list(csv_file_name):
    car_list = []
    with open(csv_file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        next(reader)  # пропускаем заголовок
        for row in reader:
            # car_type;brand;passenger_seats_count;photo_file_name;body_whl;carrying;extra
            car_type = row[0]
            if car_type:
                brand = row[1]
                photo = row[3]
                carrying = float(row[5])
                if car_type == 'truck':
                    body_whl= row[4]
                    car_list.append(Truck(brand, photo, carrying, body_whl))
                elif car_type == 'car':
                    seats_count = int(row[2])
                    car_list.append(Car(brand, photo, carrying, seats_count))
                elif car_type == 'spec_machine':
                    extra = row[6]
                    car_list.append(SpecMachine(brand, photo, carrying, extra))

    return car_list


if __name__ == "__main__":
    print(get_car_list("./cars.csv"))
