# This code checks if a given array is sorted in ascending order.
# It iterates through the array, comparing each element with the next to ensure the order is correct.

# Example:
# Input:
# Enter the size of the array: 5
# Enter the element at array[0]: 1
# Enter the element at array[1]: 2
# Enter the element at array[2]: 3
# Enter the element at array[3]: 4
# Enter the element at array[4]: 5
# Output:
# True

from array import array

def sorted_array(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

# Time Complexity = O(n)
# Space Complexity = O(1)

# User Input
user_array = array('i', [])  
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)

# Check if the array is sorted
result = sorted_array(user_array)

# Print the result: True if sorted, False otherwise
print(result)
