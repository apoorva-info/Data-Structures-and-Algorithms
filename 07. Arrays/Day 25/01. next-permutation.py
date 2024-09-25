# Goal: This code finds the next permutation of a given list of integers. 
# It provides three approaches: brute force, better using itertools, and an optimal approach that handles duplicates.

# Example:
# Input:
# Enter the size of the list: 3
# Enter the element at array[0]: 1
# Enter the element at array[1]: 2
# Enter the element at array[2]: 3
# Output:
# Next permutation: [1, 3, 2]

# Helper function to generate all permutations
def permutations(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    permutations_list = []

    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for p in permutations(remaining):
            permutations_list.append([current] + p)
    return permutations_list

# Brute Force Approach: Generate all permutations and return the next one in lexicographical order
def next_permutation_brute(arr):
    permutation_list = permutations(arr)
    permutation_list = sorted(permutation_list)
    for i in range(len(permutation_list)):
        if permutation_list[i] == arr:
            if i + 1 < len(permutation_list):
                return permutation_list[i+1]
            else:
                return permutation_list[0]
# Time Complexity = O(n! * n log (n!))
# Space Complexity = O(n! * n)

import itertools

# Better Approach: Use itertools to generate permutations and return the next one
def next_permutation_better(arr):
    permutation_list = list(itertools.permutations(arr))  # Returns a tuple, so conversion to list is important
    permutation_list = sorted(permutation_list)
    for i, value in enumerate(permutation_list):
        if value == tuple(arr):
            if i + 1 < len(permutation_list):
                return list(permutation_list[i+1])
            else:
                return list(permutation_list[0])
# Time Complexity = O(n! * n log (n!))
# Space Complexity = O(n! * n)

# Helper function to reverse a sub-array
def reverse_arr(a, start, end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    return a

# Optimal Approach: Find the next permutation in O(n) time, handles duplicates
def next_permutation_optimal(arr):
    n = len(arr)
    index = -1
    # Find the first index where arr[i] < arr[i+1] from the right
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            index = i
            break
    # If no such index exists, reverse the array (this is the last permutation)
    if index == -1:
        next_permutation = reverse_arr(arr, 0, n-1)
        return next_permutation
    
    # Find the next largest element to swap with arr[index]
    for i in range(n-1, index, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
            break
    # Reverse the elements after index to get the next permutation
    next_permutation = reverse_arr(arr, index+1, n-1)
    return next_permutation
# Time Complexity = O(n)
# Space Complexity = O(1)

# User Input
size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# Uncomment to test brute force approach
# result1 = next_permutation_brute(array)
# print(result1)

# Use the better approach
result2 = next_permutation_better(array)
print(result2)

# Uncomment to test optimal approach
# result3 = next_permutation_optimal(array)
# print(result3)
