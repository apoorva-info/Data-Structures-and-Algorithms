
# Example:
# Input:
# Enter the size of the array: 8
# Enter the element at array[0]: 0
# Enter the element at array[1]: 1
# Enter the element at array[2]: 0
# Enter the element at array[3]: 3
# Enter the element at array[4]: 12
# Enter the element at array[5]: 0
# Enter the element at array[6]: 5
# Enter the element at array[7]: 0
# Output:
# array('i', [0, 1, 0, 3, 12, 0, 5, 0])
# [1, 3, 12, 5, 0, 0, 0, 0]

from array import array

# Brute Force Approach: Move all zeroes to the end of the array while maintaining the order of non-zero elements
def shifting_zeroes(array, n):
    temp = []  # Temporary list to store non-zero elements
    for i in range(n):
        if array[i] != 0:
            temp.append(array[i])
    for i in range(len(temp)):
        array[i] = temp[i]
    for i in range(len(temp), n):
        array[i] = 0  
    print(array)

# Time Complexity = O(n)
# Space Complexity = O(n)

# Optimal Approach: Shift zeroes to the end using in-place swaps
def shifting_zeroes_using_optimal_approach(array, n):
    # Find the first zero in the array
    for i in range(n):
        if array[i] == 0:
            j = i
            break
    
    # Shift non-zero elements to the correct position and move zeroes to the end
    for i in range(j + 1, n):
        if array[i] != 0:
            array[j], array[i] = array[i], array[j]
            j += 1
    print(array)

# Time Complexity = O(n)
# Space Complexity = O(1)

# User Input
user_array = array('i', []) 
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)

# Print the original array
print(user_array)

# Uncomment one of the following lines to test different approaches:
# shifting_zeroes(user_array, size)  # Brute Force Approach
shifting_zeroes_using_optimal_approach(user_array, size)  # Optimal Approach
