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
    
car1 = Car(4,4,"Petrol")
car1.drive()

        