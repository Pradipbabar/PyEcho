# Dive into OOP

## Advanced OOP Concepts

### Abstract Classes

In object-oriented programming (OOP), abstract classes are classes that cannot be instantiated on their own and often serve as a blueprint for other classes. They may contain abstract methods, which must be implemented by any concrete (non-abstract) subclasses.

```python
# Example: Abstract class with an abstract method
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2
```

### Interfaces

Interfaces in OOP define a contract that classes must adhere to. Unlike abstract classes, interfaces cannot contain implementation details. Python doesn't have a strict concept of interfaces, but they can be simulated using abstract base classes or documentation conventions.

```python
# Example: Interface simulation using abstract base class
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def __init__(self, title):
        self.title = title

    def print_info(self):
        print(f"Book Title: {self.title}")
```

## Design Patterns

### Singleton Pattern

The singleton pattern ensures that a class has only one instance and provides a global point of access to it.

```python
# Example: Singleton pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
singleton_instance1 = Singleton()
singleton_instance2 = Singleton()
print(singleton_instance1 == singleton_instance2)  # Output: True
```

### Factory Pattern

The factory pattern is a creational pattern that provides an interface for creating objects but allows subclasses to alter the type of objects that will be created.

```python
# Example: Factory pattern
class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'rectangle':
            return Rectangle()

class Circle:
    def draw(self):
        print("Drawing Circle")

class Rectangle:
    def draw(self):
        print("Drawing Rectangle")

# Usage
factory = ShapeFactory()
circle = factory.create_shape('circle')
rectangle = factory.create_shape('rectangle')
```

### Observer Pattern

The observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

```python
# Example: Observer pattern
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, data):
        for observer in self._observers:
            observer.update(data)

class Observer:
    def update(self, data):
        print(f"Received update: {data}")

# Usage
subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("Data Updated")  # Both observers receive the update
```

These examples illustrate advanced OOP concepts such as abstract classes and interfaces, as well as design patterns including the singleton, factory, and observer patterns. They provide a foundation for building more scalable, maintainable, and flexible software using object-oriented principles.