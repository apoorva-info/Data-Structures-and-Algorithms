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
# Space Complexity = O(n)





m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

matrix = np.zeros((m,n),dtype=int)

for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input(f"Enter the element at matrix[{i}][{j}]: "))
print(matrix)

result = rotate_matrix(matrix,m,n)
print(result)