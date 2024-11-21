# Allows us to define a class that can inherit all the properties and methods from another class
# Parent Class: Class being inherited from
# Child Class: Class that inherits from another class

class Person:
    def __init__(self,first_name,last_name):
        self.firstname = first_name
        self.lastname = last_name

    
    def printname(self):
        print(f"The name is {self.firstname} {self.lastname}.")
    
x = Person("xyz","abc")
x.printname()
