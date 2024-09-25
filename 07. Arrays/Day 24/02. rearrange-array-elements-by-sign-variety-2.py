# Goal: This code rearranges the elements of an array such that positive and negative numbers alternate.
# The positive and negative elements are maintained in their relative order. If one list is longer, 
# the remaining elements are appended to the result.

# Example:
# Input:
# Enter the size of the list: 6
# Enter the element at array[0]: -1
# Enter the element at array[1]: 2
# Enter the element at array[2]: -3
# Enter the element at array[3]: 4
# Enter the element at array[4]: -5
# Enter the element at array[5]: 6
# Output:
# [2, -1, 4, -3, 6, -5]

# Brute Approach: Separate positive and negative numbers, then alternate them in the result
def rearrange_elements_brute(arr, k):
    positive_list = []
    negative_list = []
    # Separate positive and negative numbers
    for i in range(k):
        if arr[i] > 0:
            positive_list.append(arr[i])
        else:
            negative_list.append(arr[i])
    
    m = len(positive_list)
    n = len(negative_list)
    result = []
    min_len = min(m, n)
    
    # Alternate positive and negative numbers
    for i in range(min_len):
        result.append(positive_list[i])
        result.append(negative_list[i])
    
    # Append remaining elements from the longer list
    if m > n:
        result.extend(positive_list[min_len:])
    else:
        result.extend(negative_list[min_len:])
    
    # Copy the rearranged elements back to the original array
    for i in range(k):
        arr[i] = result[i]
    
    return arr

# User Input
size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# Use the brute approach to rearrange elements
result = rearrange_elements_brute(array, size)
print(result)

# Time Complexity = O(k)
# Space Complexity = O(k)
