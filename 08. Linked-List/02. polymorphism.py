# Polymorphism
# Core concept in object oriented programming that allows objects of different classes to be treated as objects of a common superclass.
# It provides a way to perform a single action in different forms.
# Polymorphism is typically achieved through method overriding and interfaces. 

# Method Overriding:
# It allows a child class to provide a specific implementation of a method that is already defined in its parent class.

# Base Class
class Animal:
    def speak(self):
        return "Sound of the animal."

# Derived Class 1 
class Dog(Animal):
    def speak(self):
        return "Dog says woof!"
    
# Derived Class 2
class Cat(Animal):
    def speak(self):
        return "Cat says meow!"
    
# Function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())

# dog=Dog()
# print(dog.speak())

# cat=Cat()
# print(cat.speak())

# lion=Animal()
# print(lion.speak())

# animal_speak(dog)
# animal_speak(lion)
# animal_speak(cat)


# Polymorphism with Functions and Methods
# Base Class
class Shape:
    def area(self):
        return "The area of the figure."

# Derived Class 1
class Rectangle(Shape):
    def __init__(self,length, breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length * self.breadth

# Derived Class 2
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
        
# Function that demonstrates polymorphism
def figure_area(shape):
    print(shape.area())

# shape1=Circle(10)
# figure_area(shape1)

# shape2=Rectangle(2,3)
# figure_area(shape2)

# Polymorphism with Abstract Base Classes(ABCs)
# Abstract Base Classes are used to define common methods for a group of related objects. 
# They can enforce that derived classes implement particular methods, promoting consistency across different implementations.

from abc import ABC,abstractmethod

# Define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass 

# Derived Class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

# Derived Class 2   
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started."
    
# Function that demonstrates polymorphism
def vehicle_engine(vehicle_type):
    print(vehicle_type.start_engine())
    
# Create objects of car and bike
vehicle1 = Car()
vehicle_engine(vehicle1)

vehicle2 = Bike()
vehicle_engine(vehicle2 )