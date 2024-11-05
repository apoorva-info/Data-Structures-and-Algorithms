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

# Optimal Approach
# 1. Find the sorted half.
# 2. Sorted half may or may not have the answer.
def minimum_optimal(arr,n):
    low = 0
    high = n - 1
    min_value = float('inf')
    while low <= high:
        mid = (low + high)//2
        # If the search space is already sorted then arr[low] <= arr[high]
        if arr[low] <= arr[high]:
            min_value = min(arr[low],min_value)
            break
        if arr[low] <= arr[mid]:
            min_value = min(arr[low],min_value)
            low = mid + 1
        else:
            min_value = min(arr[mid],min_value)
            high = mid - 1
    return min_value
# Time Complexity = O(log n)
# Space Complexity = O(1)     
        
# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
# result = minimum_brute(array)
# print(result)
result = minimum_optimal(array,size)
print(result)