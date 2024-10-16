# Tuples are ordered collections of items that are immutable. 
# They are similar to lists, but their immutability makes them different.

## Creating Tuple
# empty_tuple = ()
# print(empty_tuple)
# print(type(empty_tuple))

## Type Conversion
numbers = tuple([1,2,3,4,5,6])
# print(numbers)

mixed_tuple = (1, "Apple", True, 5.77)
# print(mixed_tuple)

## Accessing Tuple Elements
# print(numbers[4])

## Tuples Operations

# Concatenation
# concatenation_tuple = mixed_tuple + numbers
# print(concatenation_tuple)

# Repetition
# print(mixed_tuple * 3)

## Immutable Nature of Tuples
## Meaning that their elements cannot be changed once assigned.
# numbers[2] = "ja"
# print(numbers)

## Tuple Methods 
# Count Method 
# print(numbers.count(10))
# Index Method
# print(numbers.index(4))

## Packing and Unpacking Tuples

# Packing
# packed_tuple = 1,4,"Area", False
# print(packed_tuple)

# Unpacking
# a,b,c,d=packed_tuple
# print(a)
# print(b)
# print(c)
# print(d)

# Unpacking with *
# first, *middle, last = numbers
# print(first)
# print(middle)
# print(last)

## Nested Tuples
# lst = [[1,2,3],[4,5,6,7],(True,"Apple",4,8.99)] # We can have tuples inside a list.
# print(lst[2][0:2])

nested_tuple = ((1,2,3),("Apple",True,False),(True,False))
## Accessing the elements inside a tuple
# print(nested_tuple[1])
# print(nested_tuple[1][2])

# Iterating over nested tuples
for items in nested_tuple:
    for item in items:
        print(item,end=" ")
    print()