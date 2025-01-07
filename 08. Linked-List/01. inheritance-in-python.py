# Inheritance
# Fundamental concept in object oriented programming that allows a class to inherit attributes and methods from another class.


# Parent Class
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    
    def drive(self):
        print(f"The person can drive {self.enginetype} car.")
    
# car1 = Car(4,4,"Petrol")
# car1.drive()

# Child Class --> Wrong way
# class Tesla(Car): # You will writing the parent class within the brackets.
#     def color(self):
#         print(f"The color of the car is blue.")

# car2 = Tesla(4,5,"Petrol")
# car2.color()

# Single Inheritance
# Child Class
class Tesla(Car): # You will writing the parent class within the brackets.
    # Constructor
    def __init__(self, windows, doors, enginetype,is_selfdriving):
        # since car already has these attributes, we don't need to write the self.xyz , instead we can directly use super keyword
        super().__init__(windows,doors,enginetype) # From the parent class, I am calling my init method
        self.is_selfdriving= is_selfdriving
    
    def selfdriving(self):
        print(f"Tesla supports self driving: {self.is_selfdriving}")

# car2 = Tesla(4,5,"Electric",True)
# car2.selfdriving()
# car2.drive()


# Multiple Inheritance
# When a class inherits from more than one base class.

# Base Class 1
class Animal:
    def __init__(self,name):
        self.name=name
    
    def animalname(self):
        print(f"The name of the animal is {self.name}.")

    def speaking(self):
        print(f"The {self.name} says woof.")

class Pet:
    def __init__(self,pet,owner=None):
        self.owner=owner
        self.pet=pet
    
    def is_pet(self):
        print(f"Someone's Pet: {self.pet}")
        print(f"The name of the owner is {self.owner}.")


# Derived Class
class Dog(Animal,Pet):
    def __init__(self,name,pet,owner,speak):
        Animal.__init__(self,name)
        Pet.__init__(self,pet,owner)
        self.speak=speak
    
    def speaking(self):
        print(f"The {self.name} says {self.speak}.") # There are two speaking methods but this will be given more
                                                     # priority as it is in the child class. 
        
dog1=Dog("Little",True,"Apoorva","Bhooobhooo")
dog1.speaking()
dog1.is_pet()
dog1.animalname()
print(dog1.owner)
