# Sets are built in data type in python used to store collections of unique items.
# They are unordered, meaning that they do not follow a specific order, and they do not allow duplicate elements.
# Sets are useful for membership tests, eliminating duplicate entries, and performing mathematical set operations like union, 
# intersection, difference and symmetric difference.

# Creating a set
my_set = {1,2,3,4,5}
# print(my_set)
# print(type(my_set))

# Creating an empty set
empty_set = set()
# print(empty_set)
# print(type(empty_set))

# Typecasting
mixed_set = set([1,"Apple",True,89.3,"Apple",1,1,2])
# print(mixed_set)

# Basic Set Operations
# Adding an element
my_set.add(8)
# print(my_set)
# Removing an element
# my_set.remove(1) # If the element is not present in the set, it would display a keyerror 
# print(my_set)

# Discarding an element -> If the element is present, it should remove it and if the element is not present in the set, 
# it should not show any error.
# my_set.discard(10)

# Pop Method
# popped_set = my_set.pop()
# print(popped_set) # FIFO
# print(my_set) 

# Clear all the elements
# my_set.clear()
# print(my_set)

# Set Membership Test
# print(5 in my_set)
# print(11 in my_set)

# Mathematical Operations
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,4,5}

# Union
# union_set = set1.union(set2)
# print(union_set)

# Intersection
# intersection_set = set1.intersection(set2)
# print(intersection_set)

# set1.intersection_update(set2) # Updates the common elements of set1 and set2 in set1.
# print(set1)

# Difference 
# difference_set = set1.difference(set2)
# print(difference_set)

# Symmetric Difference
# Common elements from both the sets are removed and unique elements from both the sets are combined.
# symmetric_set = set1.symmetric_difference(set2)
# print(symmetric_set)

# Sets Methods
# issubset
# print(set1.issubset(set2))
# issuperset
# print(set1.issuperset(set2))

# Counting unique words in a text
text = "Today we are discussing about sets."
a = text.split()
unique_words = set(a)
print(unique_words)
print(len(unique_words))


