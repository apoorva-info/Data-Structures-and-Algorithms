# Goal: Find the minimum in a rotated sorted array.
# Example:
# Input:
# Enter the size of the sorted array: 7
# Enter the element at array[0]: 4
# Enter the element at array[1]: 5
# Enter the element at array[2]: 6
# Enter the element at array[3]: 7
# Enter the element at array[4]: 0
# Enter the element at array[5]: 1
# Enter the element at array[6]: 2
# Output:
# 0

# Brute Force Approach
def minimum_brute(arr):
    min_value = float('inf')
    for i in arr:
        min_value = min(i, min_value)
    return min_value

# Time Complexity = O(n)
# Space Complexity = O(1)



# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
result = minimum_brute(array)
print(result)