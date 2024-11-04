from enum import Enum

class Color(Enum):
    BLACK = 0
    WHITE = 1
    RED = 2
    BLUE = 3

class CarBrand(Enum):
    HYUNDAI = 0
    FORD = 1
    SCANIA = 2

class Car(Enum):
    MY_WORK_CAR = ("BH 70xx AA", Color.BLUE, CarBrand.SCANIA)
    MY_HOME_CAR = ("HH 23xx KO", Color.WHITE, CarBrand.FORD)
    MY_WIFE_CAR = ("HH 23xx MK", Color.BLACK, CarBrand.HYUNDAI)

    def __init__(self, number, color, brand):
        self.number = number
        self.color = color
        self.brand = brand
    
if __name__ == "__main__":
    for it in Car:
        print(repr(it))

    print(Car.MY_HOME_CAR.number)
    print(Car.MY_HOME_CAR.brand.name)
    print(Car.MY_HOME_CAR.brand.value)
    print(Car.MY_HOME_CAR.color.name)
    print(Car.MY_HOME_CAR.color.value)
    print(Car.MY_HOME_CAR.color is Color.BLUE)
    print(Car.MY_HOME_CAR.color is Color.RED)