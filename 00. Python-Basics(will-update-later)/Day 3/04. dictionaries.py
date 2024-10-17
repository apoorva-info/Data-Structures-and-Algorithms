# Dictionaries are unordered collections of items.
# They store data in key-value pairs.
# Keys must be unique and immutable, while values can be of any type.

# Creating Dictionaries
# empty_dict = {}
# print(type(empty_dict))

# empty_dict = dict()
# print(empty_dict)

# Accessing dictionary elements
student={"name":"Jack","family name":"Williams","age":22,"grade":"A"}
# print(student["age"])

# Accessing dictionary elements using get() method
print(student.get('family name'))
print(student.get("name","Sam"))
print(student.get("mobile number","not available"))