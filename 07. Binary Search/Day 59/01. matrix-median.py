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
# Time Complexity: O((m*n)+(m*n)log(m*n))  
# Space Complexity: O(m*n)

# Better Approach 

def find_median_better(arr, m, n):
    low = min(arr)
    high = max(arr)
    req = (m*n)//2

    while low <= high:
        mid = (low + high)//2
        smaller_equals = blackbox(arr, m, mid)
        if smaller_equals <= req:
            low = mid + 1
        else:
            high = mid - 1
    return low



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
# result = find_median_brute(array,m,n)
# print(result)
result = find_median_better(array,m,n)
print(result)