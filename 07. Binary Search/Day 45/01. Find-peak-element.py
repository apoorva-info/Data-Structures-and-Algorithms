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
    if n == 1: # Case 1: If there is a single element in an array.
        return arr[n]
    if arr[0] > arr[1]: # Case 2: If the first element is the peak element.
        return arr[i]
    if arr[n-1] > arr[n-2]: # Case 3: If the last element is the peak element.
        return arr[n-1]
    
    else:
        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high)//2
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            if arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1


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