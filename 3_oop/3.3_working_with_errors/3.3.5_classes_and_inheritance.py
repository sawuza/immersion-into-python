import os
import csv

class ExtNotValid(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

class SeatsNotValid(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

        photo_file_ext = self.get_photo_file_ext()
        if photo_file_ext not in [".jpg", ".jpeg", ".png", ".gif"]:
            raise ExtNotValid()

    def get_photo_file_ext(self):
        path = self.photo_file_name
        path_split = os.path.splitext(path)
        return path_split[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count, car_type="car"):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = car_type

        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except SeatsNotValid:
            pass

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl="", car_type="truck"):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = car_type
        body_whl_parts = body_whl.split("x")

        whl_parts = [float(0), float(0), float(0)]
        try:
            if len(body_whl_parts) == 3:
                whl_parts = [float(body_whl_parts[0]), float(body_whl_parts[1]), float(body_whl_parts[2])]
        except ValueError:
            pass

        self.body_length = whl_parts[0]
        self.body_width = whl_parts[1]
        self.body_height = whl_parts[2]

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra, car_type="spec_machine"):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = car_type


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)

        for row in csv_reader:
            if len(row) == 7:
                car_type = row[0] if len(row[0]) > 0 else False
                brand = row[1] if len(row[1]) > 0 else False
                passenger_seats_count = row[2] if len(row[2]) > 0 else False
                photo_file_name = row[3] if len(row[3]) > 0 else False
                body_whl = row[4]
                carrying = row[5] if len(row[5]) > 0 else False
                extra = row[6] if len(row[6]) > 0 else False

                vehicle = None
                try:
                    if car_type == 'car' and car_type and photo_file_name and brand and carrying and passenger_seats_count:
                        vehicle = Car(brand, photo_file_name, carrying, passenger_seats_count, car_type)

                    if car_type == 'truck' and car_type and photo_file_name and brand and carrying:
                        vehicle = Truck(brand, photo_file_name, carrying, body_whl, car_type)

                    if car_type == 'spec_machine' and car_type and photo_file_name and brand and carrying and extra:
                        vehicle = SpecMachine(brand, photo_file_name, carrying, extra, car_type)
                except ExtNotValid:
                    pass
                finally:
                    if vehicle is not None:
                        car_list.append(vehicle)

        return car_list


# test 1
# car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
# print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')

# test 2
# truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
# print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, truck.get_body_volume(), sep='\n')

# test 3
# spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
# print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')

# ext = spec_machine.get_photo_file_ext()
# print(ext)

# cars = get_car_list('cars_week3.csv')
# len(cars)
# for car in cars:
#     print(type(car))
