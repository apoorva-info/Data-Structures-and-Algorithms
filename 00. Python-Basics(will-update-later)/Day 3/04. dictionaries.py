# Dictionaries are unordered collections of items.
# They store data in key-value pairs.
# Keys must be unique and immutable, while values can be of any type.

##Creating Dictionaries
# empty_dict = {}
# print(type(empty_dict))

# empty_dict = dict()
# print(empty_dict)

## Accessing dictionary elements
student={"name":"Jack","family name":"Williams","age":22,"grade":"A"}

# 1. Directly calling the key
# print(student["age"])

# 2. Accessing dictionary elements using get() method
# print(student.get('family name'))
# print(student.get("name","Sam"))
# print(student.get("mobile number","not available"))

## Modifying the dictionary elements 
# Dictionaries are mutable so you can add, update or delete elements.
student["age"] = 34 # Updated a key value
# print(student)
student["country"] = "Germany" # Added a new key value
# print(student)
del student["family name"] # Deleted a key value
# print(student)

## Dictionary Methods 
# Keys Method
keys = student.keys()
# print(keys)

# Values Method
values = student.values()
# print(values)

# Items Method
items = student.items()
# print(items)

## Shallow copy
# print(student)
# student_copy1 = student # It will change the value.
# student["age"] = 78
# print(student)
# print(student_copy1)

# student_copy2 = student.copy() # It will not change the value.
# student["age"] = 54
# print(student)
# print(student_copy2)


## Iterating over the dictionaries
# You can use loops to iterate over keys, values, dictionaries or items.

# Iterating over keys
# for key in student.keys():
#     print(key)

# Iterating over values
# for value in student.values():
#     print(value)

# Iterating over dictionary
# for item in student.items():
#     print(item)

## Nested Dictionaries
students = {"student1":{"name":"Peter","age":34},
            "student2":{"name":"John","age":56}}
# print(students)

## Accessing the nested dictionaries elements
# print(students["student2"]["age"])

## Iterating over nested dictionaries
# for id,info in students.items():
#     print(f"{id}:{info}")
#     for key,value in info.items():
#         print(f"{key}:{value}")

## Dictionary Comprehension
# squares = {i:i**2 for i in range(10)}
# print(squares)

## Condition Dictionary Comprehension
squares = {i:i**2 for i in range(10) if i%2==0}
print(squares)
