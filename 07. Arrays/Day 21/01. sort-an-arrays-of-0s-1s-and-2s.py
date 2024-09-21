# Goal: This code sorts an array containing only 0s, 1s, and 2s using three different approaches.
# The approaches include brute force, a better counting method, and an optimal approach using the Dutch National Flag algorithm.

# Example:
# Input:
# Enter the size of the array: 6
# Enter the element at array[0]: 0
# Enter the element at array[1]: 1
# Enter the element at array[2]: 2
# Enter the element at array[3]: 0
# Enter the element at array[4]: 1
# Enter the element at array[5]: 2
# Output:
# Brute Force: [0, 0, 1, 1, 2, 2]
# Better Approach: [0, 0, 1, 1, 2, 2]
# Optimal Approach: [0, 0, 1, 1, 2, 2]

from array import array

# Brute Force Solution: Sort the array using Python's built-in sorting function
def sort_brute(arr):
    arr = sorted(arr)
    return arr
# Time Complexity = O(n log n)
# Space Complexity = O(n)

# Better Approach: Count the number of 0s, 1s, and 2s, then rewrite the array
def sort_better(arr):
    count0 = 0
    count1 = 0
    count2 = 0
    # Count occurrences of 0s, 1s, and 2s
    for i in range(len(arr)):
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1
    # Fill the array with the correct number of 0s, 1s, and 2s
    for i in range(count0):
        arr[i] = 0
    for i in range(count0, count1 + count0):
        arr[i] = 1
    for i in range(count1 + count0, count2 + count0 + count1):
        arr[i] = 2
    return arr
# Time Complexity = O(n)
# Space Complexity = O(1)

# Optimal Approach: Dutch National Flag Algorithm to sort the array in a single pass
"""
Dutch National Flag Algorithm
Intuition: 
0 to low-1: 0    ---> Extreme left
low to mid-1: 1 
mid to high: Unsorted
high+1 to n-1: 2 ---> Extreme right

Visual representation:
0        low-1 low      mid-1 mid       high high+1      n-1     

0000000000000 11111111111111 <--unsorted--> 2222222222222222
"""
def sort_optimal(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    # Traverse the array and sort it in a single pass
    while high >= mid:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
# Time Complexity = O(n)
# Space Complexity = O(1)

# User Input
user_array = array('i', [])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)
print(user_array)

# Uncomment the approach you want to use:
# result = sort_brute(user_array)
# print(result)

# result = sort_better(user_array)
# print(result)

result = sort_optimal(user_array)
print(result)
