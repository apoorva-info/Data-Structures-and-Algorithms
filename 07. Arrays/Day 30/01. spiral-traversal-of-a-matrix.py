
# Goal: Traverse a matrix in spiral order starting from the top-left corner and moving towards the center.
# The function spirally traverses the matrix and returns a list of elements in the order they are visited. 
# This problem has just one solution.

# Example:
# Input:
# Enter the number of rows: 3
# Enter the number of columns: 3
# Enter the value at matrix[0][0]: 1
# Enter the value at matrix[0][1]: 2
# Enter the value at matrix[0][2]: 3
# Enter the value at matrix[1][0]: 4
# Enter the value at matrix[1][1]: 5
# Enter the value at matrix[1][2]: 6
# Enter the value at matrix[2][0]: 7
# Enter the value at matrix[2][1]: 8
# Enter the value at matrix[2][2]: 9
# Output:
# [1, 2, 3, 6, 9, 8, 7, 4, 5]

import numpy as np
def spiral_traversal_of_a_matrix(matrix,m,n):
    ans = []
    top = 0
    left = 0
    right = n-1
    bottom = m-1
    while right >= left and top <= bottom :
        for i in range(left,right+1):
            ans.append(matrix[top][i])
        top += 1
        for i in range(top,bottom+1):
            ans.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom -= 1
        if left <= right :
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left += 1
    return ans
# Time Complexity = O(n*m)
# Space Complexity = O(n*m)

# User Input

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = np.zeros((rows,columns), dtype = int)
for i in range(rows):
    for j in range(columns):
        matrix[i][j] = int(input(f"Enter the value at matrix[{i}][{j}]: "))
print(matrix)

# Call the function and print the result
result = spiral_traversal_of_a_matrix(matrix,rows,columns)
print(result)



