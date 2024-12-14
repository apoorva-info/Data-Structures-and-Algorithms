# Goal: To search an element in a matrix. The last element of each row may/may not be lesser than the first element of the next row.






# User Input
import numpy as np
m = int(input("Enter the number of rows in a matrix: "))
n = int(input("Enter the number of columns in a matrix: "))

array = np.empty((m,n), dtype=int)
for i in range(m):
    for j in range(n):
        array[i][j] = int(input(f"Enter the element at array{[i]}{[j]}: "))
print(array)

target = int(input("Enter the value of the target: "))

# Function Call
result = 
print(result)