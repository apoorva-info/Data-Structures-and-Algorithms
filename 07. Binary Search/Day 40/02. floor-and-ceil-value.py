# Goal: To find the floor(largest number <= x) and ceil(smallest number >= x) value n sorted array.

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


# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
x = int(input("Enter the value of the target: "))

# Function Call
result = floor_value(array,size,x)
print(result)