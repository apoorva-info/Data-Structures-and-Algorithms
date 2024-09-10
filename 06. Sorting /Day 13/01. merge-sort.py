# This code implements the Merge Sort algorithm to sort an array in ascending order.
# Merge Sort is a divide-and-conquer algorithm that divides the array into halves, sorts each half, 
# and then merges the sorted halves back together.
#  In simple terms: Merge Sort ---> 1. Divide 
#                                   2. Merge

# Example:
# Input:
# Enter the size of the array: 5
# Enter the element at array[0]: 38
# Enter the element at array[1]: 27
# Enter the element at array[2]: 43
# Enter the element at array[3]: 3
# Enter the element at array[4]: 9
# Output:
# Sorted Array: [3, 9, 27, 38, 43]

# Merge Algorithm
def merge(array, low, mid, high):
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
        merge(array, low, mid, high)    # Merge the two sorted halves

# Prompt the user to enter the size of the array
size = int(input(f"Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Call the Merge Sort function to sort the array
merge_sort(array, 0, size - 1)       

# Print the sorted array
print(f"Sorted Array: {array}")

# Time Complexity = O(n*log(n))
# Space Complexity = O(n)
