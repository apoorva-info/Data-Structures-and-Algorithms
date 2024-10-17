# This code calculates the frequency of elements in an array using a hash array (or frequency array)
# Example:
# Input:
# Enter the size of array: 5
# Enter the element at array[0]: 1
# Enter the element at array[1]: 2
# Enter the element at array[2]: 1
# Enter the element at array[3]: 3
# Enter the element at array[4]: 1
# Given Array: [1, 2, 1, 3, 1]
# Enter the number of elements you want to check: 2
# Enter the element at array[0]: 1
# Output:
# The frequency of 1 is 3
# Enter the element at array[1]: 5
# Output:
# 5 is out of range

# Prompt the user to enter the size of the array
size = int(input("Enter the size of array: "))
array = []

# Loop to take array elements as input from the user
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Print the given array
print(f"Given Array: {array}")

# Pre-computation method using a hash array to store frequencies
hash = [0] * 13  # Initialize a hash array of size as described in the question
for i in range(size):
    if array[i] < len(hash):  # Check if the element is within the range of the hash array
        hash[array[i]] += 1  # Increment the count of the element in the hash array

# Prompt the user to enter the number of elements to check frequency for
num = int(input("Enter the number of elements you want to check: "))

# Fetch Method: Checking the frequency of the specified elements
for j in range(num):
    element = int(input(f"Enter the element at array[{j}]: "))
    if element < len(hash):  # Check if the element is within the range of the hash array
        print(f"The frequency of {element} is {hash[element]}")  # Print the frequency
    else:
        print(f"{element} is out of range")  # Print if the element is not within the hash range

# Time Complexity = O(n)
# Maximum Hashing Array Size:
# int ---> 10^6 ---> inside main
# int ---> 10^7 ---> globally
# bool ---> 10^7 ---> inside main
# bool ---> 10^8 ---> globally
