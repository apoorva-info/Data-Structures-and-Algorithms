# Goal: To find the row with the maximum number of 1's.
# Note:
# The elements must be either 0 or 1.
# Enter the elements in ascending order.

# Brute Force Approach (Works for unsorted rows)
def find_row_brute(arr,m,n):
    max_num = float('-inf')
    max_row = -1
    for i in range(m):
        count = 0 
        for j in range(n):
            if arr[i][j] == 1:
                count += 1
        if count > max_num:
            max_num = count 
            max_row = i
            
    return max_row
# Time Complexity: O(m*n)
# Space Complexity: O(1)


# User Input
import numpy as np
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

array = np.empty((m,n), dtype=int) # np.empty ---> Creates float array by default. Do initialize the data type.
for i in range(m):
    for j in range(n):
        array[i,j] = int(input(f"Enter the element at array[{i}][{j}]: "))
print(array)

# Function Call
result = find_row_brute(array,m,n)
print(result)
