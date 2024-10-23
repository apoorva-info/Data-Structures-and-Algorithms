# Goal : The goal is to find the number of elements with reverse pairs i.e. if i < j then a[i] > 2 * a[j]
# Example:
# Input:
# Enter the size of the array: 7
# Enter the element at array[0]: 40
# Enter the element at array[1]: 25
# Enter the element at array[2]: 19
# Enter the element at array[3]: 9
# Enter the element at array[4]: 6
# Enter the element at array[5]: 2
# Enter the element at array[6]: 5
# Output:
# 15

# Brute Force Approach
def reverse_pairs_brute(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > 2 * arr[j]:
                count += 1
    return count
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Optimal Approach
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
count = 0
def countPairs(arr,low,mid,high):
    global count
    right = mid + 1
    for i in range(low,mid+1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
            count += (right - (mid + 1))


def merge_sort(array, low, high):
    # Recursive function to divide the array and sort the sub-arrays
    if low == high:
        return  # Base case: single element
    else:
        mid = (low + high) // 2  
        merge_sort(array, low, mid)     # Sort the left half
        merge_sort(array, mid + 1, high)  # Sort the right half
        countPairs(array,low,mid,high)
        merge(array, low, mid, high)    # Merge the two sorted halves

def reverse_pairs_optimal(arr,n):
    merge_sort(arr,0,n-1)
    return count
# Time Complexity = O(2 n log n)
# Space Complexity = O(n)


# User Input
size = int(input(f"Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
# result = reverse_pairs_brute(array,size)
# print(result)
result = reverse_pairs_optimal(array,size)
print(result)