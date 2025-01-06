## Object Oriented Programming is a programming paradigm that uses "objects" to design applications and computer programs.
## Allows for modelling real-world scenarios using classes and objects. 
## Classes: Blueprint for creating objects. Consists of attributes and methods.

class Car:
    pass

audi = Car() # Object
bmw = Car() # Object

print(type(audi))

## Defining each attribute separately is not a proper way. We cannot reuse the attribute.
# audi.windows = 4
# print(audi.windows)
# print(bmw.windows) 

## Instance Variable and Methods
# print(dir(audi))
## Output:['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
## You can see that there are many inbuilt methods. We will talk about ___init__ method. 


class Dog:
    def __init__(self, name, age): # 1. __init__ --> Defines all the attributes that will be inside the class at the first hand. 
                                   # 2. name, age --> Parameter
                                   # 3. self --> Responsible for accessing the instance variable inside the class itself.
                                    
        self.name = name # self.name ---> This "name" is the instance variable available in the class Dog.
        self.age = age
        self.breed = 'German Shepherd' # Fixed attribute value
        # breed = 'German Shepherd' # Will be considered a local variable without self keyword 
    
## creating objects
Dog1 = Dog('Little', 10)
print(Dog1.breed)