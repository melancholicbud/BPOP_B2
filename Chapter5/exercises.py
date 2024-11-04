# ex. 1: Class for forming unique subsets
class SubsetGenerator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def get_unique_subsets(self):
        subsets = [[]]
        for num in self.numbers:
            subsets += [curr + [num] for curr in subsets]
        # unique subsets
        unique_subsets = {tuple(sorted(sub)) for sub in subsets}
        return [list(sub) for sub in unique_subsets]

# ex. 2: Class for arithmetic operations 
class ArithmeticOperations:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"

# ex. 3: class for Auto
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def drive(self, distance):
        self.odometer += distance
        print(f"The car drove {distance} km. Odometer: {self.odometer} km")
    
    def display_info(self):
        print(f"Car: {self.make} {self.model} ({self.year}), Odometer: {self.odometer} km")

# ex. 4: Class for rectangle with overloading of comparison methods
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __str__(self):
        return f"Rectangle ({self.width} x {self.height}), Area: {self.area()}"

# ex. 5: Vehicle class with listing of states
from enum import Enum

class CarState(Enum):
    STOPPED = "Stopped"
    MOVING = "Moving"
    TURNING_LEFT = "Turning Left"
    TURNING_RIGHT = "Turning Right"

class CarWithState:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.state = CarState.STOPPED
    
    def change_state(self, new_state):
        if isinstance(new_state, CarState):
            self.state = new_state
            print(f"Car state changed to: {self.state.value}")

# ex. 6: class with a count of the number of copies
class InstanceCounter:
    instances_count = 0

    def __init__(self):
        InstanceCounter.instances_count += 1
    
    def __del__(self):
        InstanceCounter.instances_count -= 1

# ex. 7: Base class and derived classes for geometric shapes, cars, stores and animals
from abc import ABC, abstractmethod

# Base class for objects
class Entity(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_info(self):
        pass

# Figures
class Shape(Entity):
    def __init__(self, name):
        super().__init__(name)

    @abstractmethod
    def area(self):
        pass

# Vehicle
class Vehicle(Entity):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

# Store
class Store(Entity):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location

# Animal
class Animal(Entity):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

# Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2

class Sedan(Vehicle):
    def display_info(self):
        print(f"{self.name} - Type: Sedan, Speed: {self.speed} km/h")

class Truck(Vehicle):
    def display_info(self):
        print(f"{self.name} - Type: Truck, Speed: {self.speed} km/h")

class Kiosk(Store):
    def display_info(self):
        print(f"{self.name} - Type: Kiosk, Location: {self.location}")

class Supermarket(Store):
    def display_info(self):
        print(f"{self.name} - Type: Supermarket, Location: {self.location}")

class Horse(Animal):
    def display_info(self):
        print(f"{self.name} - Species: Horse")

class Tiger(Animal):
    def display_info(self):
        print(f"{self.name} - Species: Tiger")

# ex. 8: Class with access to attributes via @property
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("The price can't be negative")

# ex. 9: Class with arithmetic operations methods overloading
class IntegerValue:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return IntegerValue(self.value + other.value)

    def __sub__(self, other):
        return IntegerValue(self.value - other.value)

    def __mul__(self, other):
        return IntegerValue(self.value * other.value)

    def __str__(self):
        return str(self.value)

# ex. 10: Class for a working with JSON-file
import json

class JSONHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_json(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def write_json(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def update_json(self, key, value):
        data = self.read_json()
        data[key] = value
        self.write_json(data)
    
    def delete_key(self, key):
        data = self.read_json()
        if key in data:
            del data[key]
        self.write_json(data)

# ex. 11: A class for finding the rectangle with maximum area
class MaxRectangleFinder:
    @staticmethod
    def find_max_rectangle(rectangles):
        return max(rectangles, key=lambda r: r.area())

# ex. 12: A class for converting numbers to binary and vice versa
class BinaryConverter:
    @staticmethod
    def to_binary(number):
        return bin(number)[2:]

    @staticmethod
    def from_binary(binary_str):
        return int(binary_str, 2)

# ex. 13: class for counting GCD
class GCD:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    @property
    def numbers(self):
        return self.num1, self.num2

    @numbers.setter
    def numbers(self, values):
        self.num1, self.num2 = values

    def calculate_gcd(self):
        a, b = self.num1, self.num2
        while b:
            a, b = b, a % b
        return a

# ex. 14: class for Quadratic Equation
import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_roots(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant > 0:
            root1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            return root1, root2
        elif discriminant == 0:
            root = -self.b / (2 * self.a)
            return root
        else:
            return "Complex Roots"


# ex. 15: class for employee
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def to_dict(self):
        return {"Name": self.name, "Position": self.position, "Salary": self.salary}

# ex. 16: class for Contact
class Contact:
    def __init__(self, name, phone, email, birthday):
        self.name = name
        self.phone = phone
        self.email = email
        self.birthday = birthday

    def to_dict(self):
        return {"Name": self.name, "Phone": self.phone, "Email": self.email, "Birthday": self.birthday}

import json

class AddressBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def load_from_file(self):
        with open(self.filename, 'r') as file:
            self.contacts = [Contact(**data) for data in json.load(file)]

