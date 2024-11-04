# Goal: Given a rotated sorted array with duplicates and a target value, return True if target value is present in the array 
# else return False.

# Brute Force Approach
def search_element_in_rotated_sorted_array_brute(arr,x):
    for element in arr:
        if element == x:
            return True
    return False

# Time Complexity = O(n) ---> Loop runs n times 
# Space Complexity = O(1) ---> No extra space is being used 

# Optimal Approach
def search_element_in_rotated_sorted_array_optimal(arr,n,x):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            return True
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
        if arr[low] <= arr[mid]:
            if arr[low] <= x <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False
    

# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
x = int(input("Enter the value of the target: "))

# Function Call
# result = search_element_in_rotated_sorted_array_brute(array,x)
# print(result)
result = search_element_in_rotated_sorted_array_optimal(array,size,x)
print(result)