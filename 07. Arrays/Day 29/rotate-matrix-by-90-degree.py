# Goal: This code rotates a square matrix by 90 degrees.

# Example:
# Input:
# Enter the number of rows: 3
# Enter the element at matrix[0][0]: 1
# Enter the element at matrix[0][1]: 2
# Enter the element at matrix[0][2]: 3
# Enter the element at matrix[1][0]: 4
# Enter the element at matrix[1][1]: 5
# Enter the element at matrix[1][2]: 6
# Enter the element at matrix[2][0]: 7
# Enter the element at matrix[2][1]: 8
# Enter the element at matrix[2][2]: 9
# Output:
# Rotated matrix (Brute Force):
# [[7 4 1]
#  [8 5 2]
#  [9 6 3]]

# Brute Force Approach: Use an auxiliary matrix to store rotated values
def rotate_matrix(matrix, rows, columns):
    # Create a new matrix for the rotated result
    ans_rows = columns
    ans_col = rows
    ans = np.zeros((ans_rows, ans_col), dtype=int)  

    for i in range(ans_col):
        for j in range(ans_rows):
            ans[j][ans_col - i - 1] = matrix[i][j]  

    return ans
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

# Optimal Approach: In-place matrix rotation using transpose and reverse
def rotate_matrix_optimal(matrix, n):
    # Step 1: Transpose the matrix (convert rows to columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # Swap elements

    # Step 2: Reverse each row to achieve 90-degree rotation
    for i in range(n):
        for j in range(n // 2):  # Only reverse half the row
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]  # Swap elements in the row

    return matrix
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# User Input Section: Accept matrix size and elements
import numpy as np

m = int(input("Enter the number of rows: "))
n = m  # Since it's a square matrix, the number of rows is equal to the number of columns

# User Input
matrix = np.zeros((m, n), dtype=int)

for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input(f"Enter the element at matrix[{i}][{j}]: "))
print(f"Original matrix: \n{matrix}")

# Brute Force Approach
# result_brute = rotate_matrix(matrix, m, n)
# print(f"Rotated matrix (Brute Force): \n{result_brute}")

# Optimal Approach
result_optimal = rotate_matrix_optimal(matrix,m)
print(f"Rotated matrix (Optimal): \n{result_optimal}")
