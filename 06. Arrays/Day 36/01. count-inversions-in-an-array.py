# Goal: The goal is to count the number of inversions in an array.
# Example:
# Input:
# Enter the size of the list: 6
# Enter the element at lst[0]: 5
# Enter the element at lst[1]: 3
# Enter the element at lst[2]: 2
# Enter the element at lst[3]: 7
# Enter the element at lst[4]: 5
# Enter the element at lst[5]: 4
# Output:
# 7

# Brute Force Approach
def count_inversions_brute(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                count += 1
    return count
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Optimal Approach
count = 0
# Merge Algorithm
def merge(array, low, mid, high):
    global count     # Do not use the global variable in the interview.
    temp_array = []  # Temporary array to store merged elements
    left = low       # Left Pointer
    right = mid + 1  # Right Pointer
    
    # Merge the two halves into temp_array
    while left <= mid and right <= high:
        if array[left] <= array[right]:
            temp_array.append(array[left])
            left += 1
        else:
            temp_array.append(array[right])
            count += mid - left + 1
            right += 1
    
    # Append remaining elements of the left half, if any
    while left <= mid:
        temp_array.append(array[left])
        left += 1
    
    # Append remaining elements of the right half, if any
    while right <= high:
        temp_array.append(array[right])
        right += 1
    
    # Copy the sorted elements back into the original array
    for i in range(low, high + 1):
        array[i] = temp_array[i - low]

def merge_sort(array, low, high):
    # Recursive function to divide the array and sort the sub-arrays
    if low == high:
        return  # Base case: single element
    else:
        mid = (low + high) // 2  
        merge_sort(array, low, mid)     # Sort the left half
        merge_sort(array, mid + 1, high)  # Sort the right half
        merge(array, low, mid, high) 

def count_inversions_better(arr,n):
    merge_sort(arr,0,n-1)
    return count
# Time Complexity = O(n log n)
# Space Complexity = O(n) --> For the temporary array that was used while merging.

    
# User Input
lst = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)

# Function Call
# result = count_inversions_brute(lst,n) 
# print(result)
result = count_inversions_better(lst,n) 
print(result)