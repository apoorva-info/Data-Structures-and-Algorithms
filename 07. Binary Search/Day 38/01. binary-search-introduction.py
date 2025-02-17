# Binary Search: A searching algorithm in a limited search space.
# Search in a sorted area

# Goal: Given a sorted array, return the index of a given target value.

# Example:
# Input:
# Enter the size of the array: 6
# Enter the element at array[0]: 1
# Enter the element at array[1]: 3
# Enter the element at array[2]: 5
# Enter the element at array[3]: 7
# Enter the element at array[4]: 9
# Enter the element at array[5]: 10
# Enter the value that you want to search: 7
# Output:
# 3

# Linear Search
def search_target_linear(arr,n,target):
    for i in range(n):
        if arr[i] == target:
            return i
# Time Complexity = O(n)
# Space Complexity = O(1)

# Search space: Everything between low and high.
# Iterative Approach
def search_target_binary(arr,n,target):
    low = 0 
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Recursive Binary Search Code
def recursive_code(arr,low,high,target):
    if low > high:
        return -1
    else:
        mid = (low + high)//2
        if target == arr[mid]:
            return mid 
        elif target < arr[mid]:
            return recursive_code(arr,low,mid-1,target)
        else:
            return recursive_code(arr,mid+1,high,target)
# Time Complexity = O(log n)
# Space Complexity = O(log n) --> Temporary space used
        
# User Input
size = int(input(f"Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
target_value = int(input("Enter the value that you want to search: "))

# Function Call
# result = search_target_linear(array, size, target_value)
# print(result)
# result = search_target_binary(array, size, target_value)
# print(result)
# result = recursive_code(array, 0, size - 1, target_value)
# print(result)

# Overflow Case:
# if low = 0 and high = int(inf) i.e. infinity
# Might happen that low = int(inf) then mid = 2 * int(inf) which cannot be stored in an integer.
# Take mid = low - ((high - low)//2) to avoid the case of overflow.

# Explanation:
# In binary search, we usually find the middle index with: mid = (low + high) // 2.
# But if `low` and `high` are both large numbers, adding them directly (low + high) can create a number
# that’s too big to store correctly, causing an "overflow" error in some systems.
#
# Solution:
# To prevent this, we can rewrite the formula as: mid = low + (high - low) // 2.
# This way, instead of adding two large numbers, we subtract first to get a smaller number (high - low),
# then divide by 2, and finally add `low` to find `mid`.
# This keeps `mid` within safe limits and avoids overflow!
