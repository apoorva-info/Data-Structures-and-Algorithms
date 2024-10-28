# Goal: To find the floor(largest number <= x) and ceil(smallest number >= x) value n sorted array.
# Example:
# Input:
# Enter the size of the sorted array: 5
# Enter the element at array[0]: 2
# Enter the element at array[1]: 3
# Enter the element at array[2]: 5
# Enter the element at array[3]: 6
# Enter the element at array[4]: 8
# Enter the value of the target: 4
# Output:
# Floor Value:  3
# Ceil Value:  5

# Floor Value
def floor_value(arr,n,target):
    low = 0
    high = n - 1
    ans = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] <= target:
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    return ans
# Time Complexity = O(log n)
# Space Complexity = O(1)

# Ceil Value
def ceil_value(arr,n,target):
    low = 0
    high = n - 1
    ans = n 
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= target:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans
# Time Complexity = O(log n)
# Space Complexity = O(1)

# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
x = int(input("Enter the value of the target: "))

# Function Call
floor_value_result = floor_value(array,size,x)
print("Floor Value: ", floor_value_result)
ceil_value_result = ceil_value(array,size,x)
print("Ceil Value: ", ceil_value_result)