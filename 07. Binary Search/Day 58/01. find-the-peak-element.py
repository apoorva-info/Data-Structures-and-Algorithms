# Goal: Find the peak element in a 2D array where the adjacent cells are not same.

def find_peak_element(arr,m,n):
    


# User Input
import numpy as np
m = int(input("Enter the number of rows in a matrix: "))
n = int(input("Enter the number of columns in a matrix: "))

array = np.empty((m,n), dtype=int)
for i in range(m):
    for j in range(n):
        array[i][j] = int(input(f"Enter the element at array{[i]}{[j]}: "))
print(array)

# Function Call
result = find_peak_element_brute(array,m,n)
print(result)