from abc import ABC, abstractmethod


# Advanced OOP Concepts

# Abstract Class Example
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# Interface Simulation Example
class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


# Concrete Classes
class Dog(Animal, Swimmable):
    def make_sound(self):
        return "Woof!"

    def swim(self):
        return "Dog is swimming"


class Fish(Animal, Swimmable):
    def make_sound(self):
        return "Blub!"

    def swim(self):
        return "Fish is swimming"


# Design Patterns

# Singleton Pattern Example
class SingletonDatabase:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SingletonDatabase, cls).__new__(cls)
            cls._instance.data = {"example": "data"}
        return cls._instance

# Factory Pattern Example
class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'bike':
            return Bike()

class Car:
    def drive(self):
        return "Driving a car"

class Bike:
    def drive(self):
        return "Riding a bike"

# Observer Pattern Example
class NewsAgency:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, news):
        for observer in self._observers:
            observer.update(news)


class NewsChannel:
    def update(self, news):
        print(f"Breaking News: {news}")


# Usage
if __name__ == "__main__":
    # Advanced OOP Concepts
    dog = Dog()
    print("Dog Sound:", dog.make_sound())
    print("Dog Swim:", dog.swim())

    fish = Fish()
    print("Fish Sound:", fish.make_sound())
    print("Fish Swim:", fish.swim())

    # Design Patterns
    # Singleton Pattern
    db_instance1 = SingletonDatabase()
    db_instance2 = SingletonDatabase()
    print(db_instance1 == db_instance2)  # Output: True

    # Factory Pattern
    vehicle_factory = VehicleFactory()
    car = vehicle_factory.create_vehicle('car')
    bike = vehicle_factory.create_vehicle('bike')
    print(car.drive())
    print(bike.drive())

    # Observer Pattern
    news_agency = NewsAgency()
    news_channel1 = NewsChannel()
    news_channel2 = NewsChannel()

    news_agency.add_observer(news_channel1)
    news_agency.add_observer(news_channel2)

    news_agency.notify_observers("Important News!")
