# Goal: Find the number of times an array has been rotated.
# From the previous problem, I observed that the index of minimum element is the number of times the array has been rotated.

# Example:
# Input:
# Enter the size of the sorted array: 8
# Enter the element at array[0]: 4
# Enter the element at array[1]: 5
# Enter the element at array[2]: 6
# Enter the element at array[3]: 7
# Enter the element at array[4]: 0
# Enter the element at array[5]: 1
# Enter the element at array[6]: 2
# Enter the element at array[7]: 3
# Output:
# 4

def no_of_rotations(arr,n):
    low = 0
    high = n - 1
    min_value = float('inf')
    index = -1
    while low <= high:
        mid = (low + high)//2
        if arr[low] <= arr[high]:
            if arr[low] <= min_value:
                min_value = arr[low]
                index = low
                break
        if arr[low] <= arr[mid]:
            if arr[low] <= min_value:
                min_value = arr[low]
                index = low
            low = mid + 1
        else:
            if arr[mid] <= min_value:
                min_value = arr[mid]
                index = mid
            high = mid - 1
    return index
# Time Complexity = O(log n)
# Space Complexity = O(n)

# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
result = no_of_rotations(array,size)
print(result)