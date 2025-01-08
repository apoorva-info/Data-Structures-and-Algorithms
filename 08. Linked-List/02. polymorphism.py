# Polymorphism
# Core concept in object oriented programming that allows objects of different classes to be treated as objects of a common superclass.
# It provides a way to perform a single action in different forms.


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
    print(animal_speak())

dog=Dog()
print(dog.speak())

cat=Cat()
print(cat.speak())

lion=Animal()
print(lion.speak())

animal_speak(dog)