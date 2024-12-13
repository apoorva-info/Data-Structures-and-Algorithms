# Goal: To search an element in a 2D matrix.

# Brute Force Approach
def find_element_brute(arr,m,n,target):
    for i in range(m):
        for j in range(n):
            if arr[i][j] == target:
                return True
    return False

# Time Complexity: O(m*n)
# Space Complexity: O(1)

# Better Approach
def find_element_better(arr,m,n,target):
    for i in range(m):
        if arr[i][0] <= target and arr[i][n-1] >= target:
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high)//2
                if arr[i][mid]== target:
                    return True
                elif arr[i][mid] < target:
                    low = mid + 1
                else: 
                    high = mid - 1
    return False




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
# result = find_element_brute(array,m,n, target)
# print(result)
result = find_element_better(array,m,n, target)
print(result)