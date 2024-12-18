# Goal: Find the peak element in a 2D array where the adjacent cells are not same.

# Brute Force Approach
def find_peak_element_brute(arr,m,n):
    for i in range(m):
        for j in range(n):
            up = arr[i - 1][j] if i > 0 else float('-inf')
            down = arr[i + 1][j] if i < m - 1 else float('-inf')
            left = arr[i][j - 1] if j > 0 else float('-inf')
            right = arr[i][j + 1] if j < n - 1 else float('-inf')
            
            if arr[i][j] > max(up, down, left, right):
                return (i, j)  
    return None 
# Time Complexity: O(m*n)
# Space Complexity: O(1)

# Better Approach
def find_peak_element_better(arr, m, n):
    for i in range(m):  
        max_in_row = 0
        for j in range(n):  
            if arr[i][j] > arr[i][max_in_row]:
                max_in_row = j

        up = arr[i - 1][max_in_row] if i > 0 else float('-inf')
        down = arr[i + 1][max_in_row] if i < m - 1 else float('-inf')
        left = arr[i][max_in_row - 1] if max_in_row > 0 else float('-inf')
        right = arr[i][max_in_row + 1] if max_in_row < n - 1 else float('-inf')

        if arr[i][max_in_row] > max(up, down, left, right):
            return (i, max_in_row)  

    return None

# User Input
import numpy as np
m = int(input("Enter the number of rows in a matrix: "))
n = int(input("Enter the number of columns in a matrix: "))

array = np.empty((m,n), dtype=int)
for i in range(m):
    for j in range(n):
        array[i][j] = int(input(f"Enter the element at array{[i]}{[j]}: "))
print(array)

# Function Call
# result = find_peak_element_brute(array,m,n)
# print(result)
result = find_peak_element_better(array,m,n)
print(result)