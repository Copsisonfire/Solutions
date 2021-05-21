 import csv
import os

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
    
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        self.body_whl = str(body_whl)
        if set(self.body_whl) <= {"0","1","2","3","4","5","6","7","8","9","0", ".", "x"} and len(self.body_whl.split("x")) == 3:
            self.body_whl = str(body_whl)
        else:
            self.body_whl = "0.0x0.0x0.0"
        self.body_length = float(self.body_whl.split("x")[0])
        self.body_width = float(self.body_whl.split("x")[1])
        self.body_height = float(self.body_whl.split("x")[2])
    
    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row[0] == "car":
                if isinstance(row[1], str) and len(str(row[1])) >= 1:
                    car_brand = row[1]
                else:
                    continue
                if row[3].endswith((".jpg", ".jpeg", ".png", ".gif")) and row[3].split(".")[0]:
                    car_photo_file_name = row[3]
                else:
                    continue
                try:
                    car_carrying = float(row[5])
                except:
                    continue
                try:
                    car_passenger_seats_count = int(row[2])
                except:
                    continue
                car = Car(car_brand, car_photo_file_name, car_carrying, car_passenger_seats_count)
                car_list.append(car)
            if row[0] == "truck":
                if isinstance(row[1], str) and len(str(row[1])) >= 1:
                    car_brand = row[1]
                else:
                    continue
                if row[3].endswith((".jpg", ".jpeg", ".png", ".gif")) and row[3].split(".")[0]:
                    car_photo_file_name = row[3]
                else:
                    continue
                try:
                    car_carrying = float(row[5])
                except:
                    continue
                car_body_whl = row[4]
                car = Truck(car_brand, car_photo_file_name, car_carrying, car_body_whl)
                car_list.append(car)
            if row[0] == "spec_machine":
                if isinstance(row[1], str) and len(str(row[1])) >= 1:
                    car_brand = row[1]
                else:
                    continue
                if row[3].endswith((".jpg", ".jpeg", ".png", ".gif")) and row[3].split(".")[0]:
                    car_photo_file_name = row[3]
                else:
                    continue
                try:
                    car_carrying = float(row[5])
                except:
                    continue
                if isinstance(row[6], str) and len(row[6]) >= 1:
                    car_extra = row[6]
                else:
                    continue
                car = SpecMachine(car_brand, car_photo_file_name, car_carrying, car_extra)
                car_list.append(car)
    return car_list



