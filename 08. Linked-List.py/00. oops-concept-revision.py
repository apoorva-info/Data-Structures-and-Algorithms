# Object Oriented Programming is a programming paradigm that uses "objects" to design applications and computer programs.
# Allows for modelling real-world scenarios using classes and objects. 
# Classes: Blueprint for creating objects. Consists of attributes and methods.

class Car:
    pass

audi = Car() # Object
bmw = Car() # Object

print(type(audi))

# Defining each attribute separately is not a proper way. We cannot reuse the attribute.
# audi.windows = 4
# print(audi.windows)
# print(bmw.windows) 

