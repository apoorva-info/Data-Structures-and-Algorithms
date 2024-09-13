# This code performs a left rotation on an array, shifting each element one position to the left.
# The first element moves to the end of the array.

# Example:
# Input:
# Enter the size of the array: 5
# Enter the element at array[0]: 1
# Enter the element at array[1]: 2
# Enter the element at array[2]: 3
# Enter the element at array[3]: 4
# Enter the element at array[4]: 5
# Output:
# Original Array: array('i', [1, 2, 3, 4, 5])
# Rotated Array: array('i', [2, 3, 4, 5, 1])

# Explanation of the Example:
# The first element (1) is stored temporarily, and each subsequent element is shifted left by one position.
# Finally, the first element is placed at the end of the array.

from array import array

def left_rotate(array):
    temp = array[0]
    for i in range(len(array) - 1):
        array[i] = array[i + 1]
    array[-1] = temp
    print(f"Rotated Array: {array}")

# Time Complexity = O(n) - because it iterates through the array once.
# Space Complexity = O(1) - in-place rotation with only a single temporary variable.

# User Input
user_array = array('i', [])  
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)

# Print the original array
print(f"Original Array: {user_array}")

# Call the function to left rotate the array
left_rotate(user_array)
