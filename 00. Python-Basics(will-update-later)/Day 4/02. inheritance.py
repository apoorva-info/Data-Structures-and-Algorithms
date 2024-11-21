# Allows us to define a class that can inherit all the properties and methods from another class
# Parent Class: Class being inherited from
# Child Class: Class that inherits from another class

# Parent Class
class Person:
    def __init__(self,first_name,last_name):
        self.firstname = first_name
        self.lastname = last_name

    
    def printname(self):
        print(f"The name is {self.firstname} {self.lastname}.")
    
# x = Person("xyz","abc")
# x.printname()

# Child Class
class Student(Person):
    # def __init__(self, first_name, last_name): 
    # The child class will not inherit the properties from parent class
    # It would override the inheritance of the parent's init function 
    def __init__(self, first_name, last_name,year):
        Person.__init__(self,first_name, last_name) # super function can also be used
        self.graduationyear = year
    
    def printyear(self):
        print(f"The year of graduation is {self.graduationyear}.")
        


        

y = Student("John","String", 2009)
y.printname()
y.printyear()