# Goal: To search an element in a matrix. The last element of each row may/may not be lesser than the first element of the next row.

# Brute Force Approach
def find_element_brute(arr,m,n,target):
    for i in range(m):
        for j in range(n):
            if arr[i][j] == target:
                return i,j
    return (-1,-1)
# Time Complexity: O(m*n)
# Space Complexity: O(1)

# Better Approach
def find_element_better(arr,m,n,target):
    for i in range(m):
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high)//2
            if arr[i][mid] == target:
                return i,mid
            elif arr[i][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return (-1,-1)
# Time Complexity: O(m * log n)
# Space Complexity: O(1)

# Optimal Approach
def find_element_optimal(arr,m,n,target):
    row = 0
    column = n - 1
    while row < m and column >= 0:
        if arr[row][column] == target:
            return (row,column)
        elif arr[row][column] < target:
            row += 1
        else:
            column -= 1
    return (-1,-1)

# User Input
import numpy as np
m = int(input("Enter the number of rows in a matrix: "))
n = int(input("Enter the number of columns in a matrix: "))

array = np.empty((m,n), dtype=int)
for i in range(m):
    for j in range(n):
        array[i][j] = int(input(f"Enter the element at array{[i]}{[j]}: "))
print(array)

target = int(input("Enter the value of the target: "))

# Function Call
# result = find_element_brute(array,m,n,target)
# print(result)
result = find_element_better(array,m,n,target)
print(result)