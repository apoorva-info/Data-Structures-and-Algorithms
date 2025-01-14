# Encapsulation:
# Concept of wrapping data(variables) and methods(functions) together as a single unit.
# Restricts direct access to some of the object's components, which is a means of preventing accidental interference and misuse of data.


# Encapsulation with Getter and Setter Methods
# Public, Private, Protected or access modifiers

class Person:
    def __init__(self,name,age):
        self.name = name # public variable
        self.age = age # public variable

def get_name(person): # Accessing the variable outside the class
    return person.name

# These instance variables might hold important data, so I want them to be initialized properly and only modified through a 
# specific function, which is why we use encapsulation.

person1 = Person("Jack",23)
# print(person.name)

print(get_name(person1))

# Private variables cannot be used outside the class. However, we can access the private variables inside the class using getter and setter
# method
class Animal:
    def __init__(self,name,age,gender):
        self.__name=name # private variable
        self.__age=age # private variable
        self.gender=gender

animal = Animal("Carrie",1,"Female")
print(animal.gender)

# def get_name_animal(animal):
#     return animal.__name
# print(get_name(animal.__name))
# print(dir(Animal))
# print(dir(Person))

# Protected : Cannot access outside the class but can access the variable from derived class.
class Vehicles:
    def __init__(self,name,age):
        self._name=name # protected variable
        self._age=age # protected variable
        

vehicle=Vehicles("Audi",1)
print(vehicle._name)

class Company(Vehicles):
    def __init__(self,name,age):
        super().__init__(name,age)

company=Company("BMW",2)
print(company._name)
