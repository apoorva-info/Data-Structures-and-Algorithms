# Finds the union of two sorted arrays
# Example:
# Input:
# Enter the size of the array: 4
# Enter the element at array[0]: 1
# Enter the element at array[1]: 2
# Enter the element at array[2]: 3
# Enter the element at array[3]: 4
# Enter the size of the array: 5
# Enter the element at array[0]: 2
# Enter the element at array[1]: 3
# Enter the element at array[2]: 5
# Enter the element at array[3]: 6
# Enter the element at array[4]: 7
# Output:
# {1, 2, 3, 4, 5, 6, 7} (for Brute Force)
# [1, 2, 3, 4, 5, 6, 7] (for Optimal Approach)
from array import array

# Brute Force Approach: Finds the union of two arrays using set operations
def union_of_arrays(array1, array2):
    union = set(list(array1) + list(array2))
    print(union)
# Time Complexity = O(n + m), where n is the size of array1 and m is the size of array2
# Space Complexity = O(n + m)

# Optimal Approach: Finds the union of two sorted arrays using two pointers
def union_of_arrays_optimal(array1, array2):
    n1 = len(array1) 
    n2 = len(array2)  
    union = [] 
    i = 0  
    j = 0  

    # Traverse both arrays until one of them is exhausted
    while i < n1 and j < n2:
        if array1[i] < array2[j]:
            if len(union) == 0 or union[-1] != array1[i]:
                union.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            if len(union) == 0 or union[-1] != array2[j]:
                union.append(array2[j])
            j += 1
        else:  # array1[i] == array2[j]
            if len(union) == 0 or union[-1] != array1[i]:
                union.append(array1[i])
            i += 1
            j += 1

    # Add remaining elements from array1
    while i < n1:
        if len(union) == 0 or union[-1] != array1[i]:
            union.append(array1[i])
        i += 1

    # Add remaining elements from array2
    while j < n2:
        if len(union) == 0 or union[-1] != array2[j]:
            union.append(array2[j])
        j += 1

    print(union)
# Time Complexity = O(n1 + n2)
# Space Complexity = O(n1 + n2)



# User Input for first array
user_array1 = array('i', [])
size1 = int(input("Enter the size of the first array: "))
for i in range(size1):
    element1 = int(input(f"Enter the element at array[{i}]: "))
    user_array1.append(element1)
user_array1 = array('i', sorted(user_array1))  

# User Input for second array
user_array2 = array('i', [])
size2 = int(input("Enter the size of the second array: "))
for i in range(size2):
    element2 = int(input(f"Enter the element at array[{i}]: "))
    user_array2.append(element2)
user_array2 = array('i', sorted(user_array2)) 

# Uncomment to use the brute force approach
# union_of_arrays(user_array1, user_array2)

# Optimal Approach Call
union_of_arrays_optimal(user_array1, user_array2)
