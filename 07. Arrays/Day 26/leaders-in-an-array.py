# Goal: This code finds all the "leaders" in an array. 
# An element is a leader if it is greater than all the elements to its right.
# The code provides two approaches: brute force and an optimal approach that works in O(n) time.

# Example:
# Input:
# Enter the size of the list: 6
# Enter the element at array[0]: 16
# Enter the element at array[1]: 17
# Enter the element at array[2]: 4
# Enter the element at array[3]: 3
# Enter the element at array[4]: 5
# Enter the element at array[5]: 2
# Output:
# Leaders in the array: [17, 5, 2]

# Brute Force Approach: Compare each element with the elements to its right
def leaders_in_an_array_brute(arr, n):
    temp = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                break
        else:
            temp.append(arr[i])
    return temp
# Time Complexity = O(n^2)
# Space Complexity = O(n)

# Optimal Approach: Traverse the array from right to left and keep track of the maximum element
def leaders_in_an_array_optimal(arr, n):
    temp = []
    max_element = float('-inf')
    # Traverse the array from right to left
    for i in range(n-1, -1, -1):
        if arr[i] > max_element:
            max_element = arr[i]
            temp.append(arr[i])
    return temp
# Time Complexity = O(n)
# Space Complexity = O(n)

# User Input
size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# Uncomment to test brute force approach
# result = leaders_in_an_array_brute(array, size)
# print(result)

# Use the optimal approach
result = leaders_in_an_array_optimal(array, size)
print(result)
