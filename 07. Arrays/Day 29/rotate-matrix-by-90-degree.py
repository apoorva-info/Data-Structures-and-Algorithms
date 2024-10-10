import numpy as np

# Brute Force Approach
def rotate_matrix(matrix,rows,columns):
    ans_rows = columns
    ans_col = rows

    ans = np.zeros((ans_rows,ans_col), dtype=int)

    for i in range(ans_col):
        for j in range(ans_rows):
            ans[j][ans_col-i-1] = matrix[i][j]

    return ans
# Time Complexity = O(n^2)
# Space Complexity = O(n^2)

# Optimal Approach: 1. Transpose 2. Reverse
def rotate_matrix_optimal(matrix,n):
    for i in range(n):
        for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
    return matrix
# Time Complexity = O(n^2)
# Space Complexity = O(1)






m = int(input("Enter the number of rows: "))
n = m

matrix = np.zeros((m,n),dtype=int)

for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input(f"Enter the element at matrix[{i}][{j}]: "))
print(f"Original matrix : \n{matrix}")

result = rotate_matrix(matrix,m,n)
print(f"Rotated matrix: \n{result}")

result = rotate_matrix_optimal(matrix,m)
print(f"Rotated matrix: \n{result}")