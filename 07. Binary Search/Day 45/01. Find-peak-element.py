# Goal: Find the peak element.
# Peak Element:  arr[i-1] < arr[i] > arr[i+1]

# Brute Force Approach
def peak_element_brute(arr,n):
    for i in range(0,n):
        if i == 0:
            if arr[i] > arr[i+1]:
                return arr[i]
        elif i == n:
            if arr[i] > arr[i-1]:
                return arr[i]
        else:
            if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                return arr[i]
# Time Complexity = O(n)
# Space Complexity = O(1)

# Optimal Approach
def peak_element_optimal(arr,n):
    if (i == 0 or arr[i] > arr[i - 1]) and (i == n - 1 or arr[i] > arr[i + 1]):
        return arr[i]
    else:
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            if arr[mid] > arr[mid - 1]:
                low = mid - 1
            else:
                high = mid + 1


# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
# result = peak_element_brute(array,size)
# print(result)
result = peak_element_optimal(array,size)
print(result)