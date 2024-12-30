# Goal: To find the median of a row-wise sorted matrix.

# Brute Force Approach
def find_median_brute(arr,m,n):
    ls = []
    for i in range(m):
        for j in range(n):
            ls.append(arr[i][j])
    ls = sorted(ls)
    median = (m * n)//2
    return ls[median]
    


# User Input
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

import numpy as np

array = np.empty((m,n),dtype=int)

for i in range(m):
    for j in range(n):
        array[i][j] = int(input(f"Enter the element at array[{i}][{j}]: "))
print(array)

# Function Call
result = find_median_brute(array,m,n)
print(result)