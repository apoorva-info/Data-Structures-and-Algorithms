# Brute Force Approach
def mark_row(matrix,m,i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def mark_column(matrix,n,j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1


def set_matrix_zeroes_brute(matrix,m,n):
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                mark_row(matrix,m,i)
                mark_column(matrix,n,j)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix

# Time Complexity = O((n*m)*(n+m)+(n*m)) 
# Space Complexity = O(1)

# Better Solution
def set_matrix_zeroes_better(matrix,m,n):
    rows=[0]*m
    columns=[0]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = 1
                columns[j] = 1
    for i in range(m):
        for j in range(n):
            if rows[i] == 1 or columns[j] == 1:
                matrix[i][j] = 0
    
    return matrix
# Time Complexity = O(n*m) 
# Space Complexity = O(n+m)

# Optimal Solution
def set_matrix_zeroes_better(matrix,m,n):
    col0 = 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] != 0:
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0
    
    return matrix
# Time Complexity = O(n*m) 
# Space Complexity = O(1)



    



        










# Used numpy to create the multidimensional array. 
import numpy as np

rows = int(input("Enter the number of rows in the matrix: "))
columns = int(input("Enter the number of columns in the matrix: "))

matrix = np.zeros((rows,columns), dtype=int) # Creates a matrix of zeroes and data type int.

for i in range(rows):
    for j in range(columns):
        matrix[i][j] = int(input(f"Enter the element at matrix[{i}][{j}]: "))
print(matrix)

# result = set_matrix_zeroes_brute(matrix,rows,columns)
# print(result)

result = set_matrix_zeroes_better(matrix,rows,columns)
print(result)