# Lists are ordered, mutable collections of items.
# They can contain items of different types.
lst = []
# print(type(lst))

## Creating a list
mixed_list = ["Apoorva", 1 , True, 7.8]
# print(mixed_list)

## Accessing List Elements 
# print(mixed_list[1])

## Slicing
d = mixed_list[1:3]
# print(d)

## Modifying the elements 
mixed_list[3] = "Star"
# print(mixed_list)

mixed_list[3:] = "Flight" # Not considering the entire word instead considering character by character
# print(mixed_list)

## List Methods
mixed_list = ["Apoorva", 1 , True, 7.8]

# Append Method 
mixed_list.append(False) # Add an item to the end 
# print(mixed_list)

# Insert Method
mixed_list.insert(2,"Ja") # Add an element at a specific location
# print(mixed_list)

# Remove Method
mixed_list.remove("Apoorva") # Removes the first occurrence of an item
# print(mixed_list)

# Pop Method 
popped_item = mixed_list.pop() # Removes and return the last element
# print(popped_item)
# print(mixed_list)

# Index Method
index = mixed_list.index("Ja") # To get the index of an element
# print(index)

# Count Method 
mixed_list.insert(3,"Apple")
mixed_list.insert(5,"Apple")
# print(mixed_list.count("Apple"))

# Sort Method
fruits = ["Apple" , "Banana" , "Cherry" , "Grapes" , "Watermelon" , "Orange" , "Kiwi"] 
fruits.sort() # Sort the list in ascending order
# print(fruits)

# Reverse Method 
mixed_list.reverse()
# print(mixed_list)

# Clear Method
# fruits.clear() # Removes all the items from the list
# print(fruits)

## Slicing List 
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[2:5])
# print(numbers[:5])
# print(numbers[5:])
# print(numbers[::2])
# print(numbers[::-1])

## Iterating Over List 
# for i in mixed_list:
#     print(i)

## Iterating Over Index
# for index,item in enumerate(mixed_list):
#     print(index,item)

## List Comprehension
# lst = []
# for i in range(10):
#     lst.append(i**2)
# print(lst)

# square = [i**2 for i in range(10)] # Using list comprehension, we can perform operations in a single line of code.
# print(square)

# Basic Syntax: [expression for item in iterable]
# With conditional logic: [expression for item in iterable if condition]
# Nested List Comprehension

square = [i**2 if i%2 == 0 else 0 for i in range(10)]
print(square)

# lst1 = [1,2,3,4]
# lst2 = ['a','b','c']
# pair = [[i,j] for i in lst1 for j in lst2]
# print(pair)

## List Comprehension with Function Calls
# lengths = [[i,len(i)] for i in fruits]
# print(lengths)

## Conclusion: 
# List Comprehensions are a powerful and concise way to create lists in python.
# They are syntactically compact and can replace more verbose looping constructs.