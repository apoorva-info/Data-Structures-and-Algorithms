import numpy as np

rows = int(input("Enter the number of rows in the matrix: "))
columns = int(input("Enter the number of columns in the matrix: "))

matrix = np.zeros((rows,columns), dtype=int)

for i in range(rows):
    for j in range(columns):
        matrix[i][j] = int(input(f"Enter the element at matrix[{i}][{j}]: "))
print(matrix)