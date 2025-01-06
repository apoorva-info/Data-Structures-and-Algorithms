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
dog1 = Dog('Little', 10)
print(dog1.breed)

dog2 = Dog('Suku', 9)
print(dog2.name )

## Defining a class with Instance Methods

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof.")

# Creating objects
dog1 = Dog("Little", 10)
dog1.bark()

dog2 = Dog("Lucy", 4)
dog2.bark()


## Modelling a Bank Account

# Tasks: 1. Deposit 2. Withdraw 3. Balance Amount

class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} is deposited. New balance = {self.balance}")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"{amount} is withdrawn. New balance = {self.balance} ")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.balance


# creating object
customer1 = BankAccount("Alice")
customer1.deposit(1000)
customer1.withdraw(200)
print(customer1.get_balance())        
