# Goal: This code modifies a matrix such that if any element in the matrix is 0, 
# the entire row and column of that element are set to 0.
# It provides three approaches: brute force, a better approach using auxiliary space, and an optimal in-place approach.

# Example:
# Input:
# Enter the number of rows in the matrix: 3
# Enter the number of columns in the matrix: 3
# Enter the element at matrix[0][0]: 1
# Enter the element at matrix[0][1]: 0
# Enter the element at matrix[0][2]: 1
# Enter the element at matrix[1][0]: 1
# Enter the element at matrix[1][1]: 1
# Enter the element at matrix[1][2]: 1
# Enter the element at matrix[2][0]: 0
# Enter the element at matrix[2][1]: 1
# Enter the element at matrix[2][2]: 1
# Output:
# [[0 0 0]
#  [0 0 1]
#  [0 0 0]]

# Brute Force Approach: Mark rows and columns with -1, then set them to 0
def mark_row(matrix, m, i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def mark_column(matrix, n, j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def set_matrix_zeroes_brute(matrix, m, n):
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                mark_row(matrix, m, i)
                mark_column(matrix, n, j)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix
# Time Complexity = O((n*m)*(n+m) + (n*m)) 
# Space Complexity = O(1)

# Better Solution: Use additional arrays to track rows and columns to be zeroed
def set_matrix_zeroes_better(matrix, m, n):
    rows = [0] * m
    columns = [0] * n
    # Mark the rows and columns that need to be zeroed
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = 1
                columns[j] = 1
    # Update the matrix
    for i in range(m):
        for j in range(n):
            if rows[i] == 1 or columns[j] == 1:
                matrix[i][j] = 0
    return matrix
# Time Complexity = O(n*m) 
# Space Complexity = O(n+m)

# Optimal Solution: Use the first row and column as markers to avoid extra space
def set_matrix_zeroes_optimal(matrix, m, n):
    col0 = 1  # Flag for the first column
    # Mark the first row and column
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    # Update the matrix based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] != 0:
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
    # Update the first row if necessary
    if matrix[0][0] == 0:
        for j in range(n):
            matrix[0][j] = 0
    # Update the first column if necessary
    if col0 == 0:
        for i in range(m):
            matrix[i][0] = 0
    return matrix
# Time Complexity = O(n*m) 
# Space Complexity = O(1)

# User Input
import numpy as np

rows = int(input("Enter the number of rows in the matrix: "))
columns = int(input("Enter the number of columns in the matrix: "))

matrix = np.zeros((rows, columns), dtype=int)  # Creates a matrix of zeroes with data type int

for i in range(rows):
    for j in range(columns):
        matrix[i][j] = int(input(f"Enter the element at matrix[{i}][{j}]: "))
print(matrix)

# Uncomment to test brute force approach
# result = set_matrix_zeroes_brute(matrix, rows, columns)
# print(result)

# Uncomment to test better approach
# result = set_matrix_zeroes_better(matrix, rows, columns)
# print(result)

result = set_matrix_zeroes_optimal(matrix, rows, columns)
print(result)
