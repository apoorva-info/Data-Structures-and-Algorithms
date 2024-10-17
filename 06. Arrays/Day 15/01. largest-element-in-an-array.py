# My approach to answer a question in an interview:
# 1. Brute Force Approach
# 2. Better Solution (Might or might not exist)
# 3. Optimal Solution
# This is how to drive an interview.

from array import array

# Brute Force Approach
# This approach sorts the array and then picks the last element, which is the largest.
def largest_element_brute(array):
    array = sorted(array)  # Sort the array
    print(f"The largest element in the array using Brute Force Approach is {array[-1]}")  # Print the last element
# Time Complexity = O(n log n) - due to sorting the array
# Space Complexity = O(n) - because sorting creates a new sorted array


# Optimal Solution
# This approach iterates through the array and keeps track of the largest element found.
def largest_element_optimal(array):
    largest = array[0]  # Initialize the largest element as the first element
    for i in range(len(array)):
        if array[i] > largest:  # If the current element is larger, update the largest
            largest = array[i]
    print(f"The largest element in the array using Optimal Approach is {largest}.")
# Time Complexity = O(n) - iterates through the array once
# Space Complexity = O(1) - only a single variable is used for tracking the largest element


# User Input
user_array = array('i', [])  # Create an empty array of integers
size = int(input("Enter the size of array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)

# Print the original array as a list
print(f"Original Array: {list(user_array)}")

# Call the Brute Force and Optimal approach functions
largest_element_brute(user_array)
largest_element_optimal(user_array)
