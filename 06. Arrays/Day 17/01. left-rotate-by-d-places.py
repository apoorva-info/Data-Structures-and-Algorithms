from array import array

# Brute Force Approach: Left rotate the array by k places using a temporary array
def left_rotate_by_d_places_brute(array, k):
    k = k % len(array)  
    temp = []  
    for i in range(k):
        temp.append(array[i])
    for i in range(k, len(array)):
        array[i - k] = array[i]
    for i in range(k):
        array[len(array) - k + i] = temp[i]
    print(f"Rotated Array: {array}")
# Time Complexity = O(n), where n is the size of the array
# Space Complexity = O(k), where k is the number of positions to rotate

# Helper function to reverse a portion of the array
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# Optimal Approach: Left rotate the array by d places using reversal
def left_rotate_by_d_places_optimal(array, n, k):
    k = k % n  
    reverse(array, 0, k - 1)
    reverse(array, k, n - 1)
    reverse(array, 0, n - 1)
    print(f"Rotated Array: {array}")
# Time Complexity = O(n), where n is the size of the array
# Space Complexity = O(1), since the rotation is done in-place

# Example:
# Input:
# Enter the size of the array: 7
# Enter the element at array[0]: 1
# Enter the element at array[1]: 2
# Enter the element at array[2]: 3
# Enter the element at array[3]: 4
# Enter the element at array[4]: 5
# Enter the element at array[5]: 6
# Enter the element at array[6]: 7
# Enter the number to which your array should be rotated: 3
# Output:
# Original array: array('i', [1, 2, 3, 4, 5, 6, 7])
# Rotated Array: array('i', [4, 5, 6, 7, 1, 2, 3])

# User Input
user_array = array('i', []) 
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)

# Input the number of positions to rotate the array
d = int(input("Enter the number to which your array should be rotated: "))

# Print the original array
print(f"Original array: {user_array}")

# left_rotate_by_d_places_brute(user_array, d)  # Brute Force Approach
left_rotate_by_d_places_optimal(user_array, size, d)  # Optimal Approach
