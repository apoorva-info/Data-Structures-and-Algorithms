# Encapsulation:
# Concept of wrapping data(variables) and methods(functions) together as a single unit.
# Restricts direct access to some of the object's components, which is a means of preventing accidental interference and misuse of data.


# Encapsulation with Getter and Setter Methods
# Public, Private, Protected or access modifiers

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def get_name(person):
    return person.name


person = Person("Jack",23)
# print(person.name)

get_name(person)