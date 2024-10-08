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


    



        










# Used numpy to create the multidimensional array. 
import numpy as np

rows = int(input("Enter the number of rows in the matrix: "))
columns = int(input("Enter the number of columns in the matrix: "))

matrix = np.zeros((rows,columns), dtype=int) # Creates a matrix of zeroes and data type int.

for i in range(rows):
    for j in range(columns):
        matrix[i][j] = int(input(f"Enter the element at matrix[{i}][{j}]: "))
print(matrix)

result = set_matrix_zeroes_brute(matrix,rows,columns)
print(result)