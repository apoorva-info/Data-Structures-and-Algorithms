# Class is like an object constructor or a "blueprint" for creating objects.

class MyClass: # Class
    x = "Hello world!" # x is the property.
    
p1 = MyClass() # p1 is the object.
print(p1.x)

# __init__() Function:
# Magic Method 
# Used to initialize object attributes
# Automatically called when you create an instance of a class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
person1 = Person("xyz",22)
person2 = Person("abc",24)

print(person1.name)
print(person2.age)

        