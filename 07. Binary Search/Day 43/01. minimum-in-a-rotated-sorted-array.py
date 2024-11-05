# Goal: Find the minimum in a rotated sorted array.

# Brute Force Approach
def minimum_brute(arr):
    min_value = float('inf')
    for i in arr:
        min_value = min(i, min_value)
    return min_value



# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
result = minimum_brute(array)
print(result)