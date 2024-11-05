# Goal: Find the number of times an array has been rotated.
# From the previous problem, I observed that the index of minimum element is the number of times the array has been rotated.

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



# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
result = no_of_rotations(array,size)
