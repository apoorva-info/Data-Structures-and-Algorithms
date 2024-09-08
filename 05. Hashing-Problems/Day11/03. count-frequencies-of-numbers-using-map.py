# This code demonstrates the use of a map (dictionary) to store the frequency of elements in an array.
# A map is preferred because it efficiently manages memory and provides fast lookups compared to array hashing.
# Example:
# Input:
# Enter the size of array: 5
# Enter the number at array[0]: 3
# Hash code of 3 is 3.
# Enter the number at array[1]: 5
# Hash code of 5 is 5.
# Enter the number at array[2]: 3
# Hash code of 3 is 3.
# Enter the number at array[3]: 7
# Hash code of 7 is 7.
# Enter the number at array[4]: 5
# Hash code of 5 is 5.
# How many numbers would you like to check? 2
# Enter the number whose frequency is to be fetched: 3
# Output:
# The frequency of 3 is 2.
# Enter the number whose frequency is to be fetched: 8
# Output:
# 8 is not present in the array.

# Prompt the user to enter the size of the array
size = int(input("Enter the size of array: "))
array = []

# Loop to take array elements as input from the user and display their hash codes
for i in range(size):
    element = int(input(f"Enter the number at array[{i}]: "))
    hash_code = hash(element)  # Calculate the hash code of the element(Just for the knowledge)
    array.append(element)
    print(f"Hash code of {element} is {hash_code}.")

# Pre-compute the frequency of each element using a dictionary (map)
frequency_dictionary = {}
for i in range(size):
    if array[i] in frequency_dictionary:
        frequency_dictionary[array[i]] += 1  # Increment the count if the element is already in the dictionary
    else:
        frequency_dictionary[array[i]] = 1  # Initialize the count if the element is not in the dictionary

# Prompt the user to enter the number of queries
query_num = int(input("How many numbers would you like to check? "))
query = []

# Loop to take query elements as input and fetch their frequency from the dictionary
for i in range(query_num):
    q = int(input("Enter the number whose frequency is to be fetched: "))
    query.append(q)
    # Fetch the frequency of the queried number
    if q in frequency_dictionary:
        print(f"The frequency of {q} is {frequency_dictionary[q]}.")
    else:
        print(f"{q} is not present in the array.")

"""
Explanation of Hashing in Python:
- Python uses a variant of the SipHash algorithm to generate hash codes, which is both fast and secure.
- The hash() function in Python computes the hash code of an object (e.g., integers, strings) 
  which is used by dictionaries to store and retrieve data.
- For security reasons, Python randomizes hash codes for strings between runs to prevent certain types
  of attacks (e.g., hash collision attacks).
- Collisions occur when two different keys produce the same hash code. Python handles collisions 
  internally using techniques like chaining (storing multiple items at the same slot) or probing 
  (finding another slot).
"""
