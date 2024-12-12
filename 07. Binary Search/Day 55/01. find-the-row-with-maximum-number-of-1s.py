# Goal: To find the row with the maximum number of 1's.



# User Input
import numpy as np
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

array = np.empty((m,n))
for i in range(m):
    for j in range(n):
        array[i,j] = int(input(f"Enter the element at array[{i}][{j}]: "))
print(array)
