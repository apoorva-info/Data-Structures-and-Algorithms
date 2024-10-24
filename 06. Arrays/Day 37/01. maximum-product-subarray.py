# Goal: Given an array, find the maximum product subarray.
# Input:
# Enter the size of the array: 4
# Enter the element at array[0]: 2
# Enter the element at array[1]: 3
# Enter the element at array[2]: -2
# Enter the element at array[3]: 4
# Output
# 6

# Brute Force Approach
def maximum_product_subarray_brute(arr,n):
    max_product = float('-inf')
    for i in range(n):
        for j in range(i,n):
            product = 1
            for k in range(i,j+1):
                product = product * arr[k]
                max_product = max(product,max_product)
    return max_product

# Time Complexity = O(n^3)
# Space Complexity = O(1)

# Better Approach
def maximum_product_subarray_better(arr,n):
    max_product = float('-inf')
    for i in range(n):
        product = arr[i]
        for j in range(i+1,n):
            product = product * arr[j]
            max_product = max(product,max_product)
    return max_product

# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Optimal Approach:
# 1. If all the numbers are positive.
# 2. If there are odd number of negative values.
# 3. If there are even number of negative values.
# 4. If there are zeroes.

def maximum_product_subarray_optimal(arr,n):
    max_product = float('-inf')
    prefix = 1
    suffix = 1
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        prefix = prefix * arr[i]
        suffix = suffix * arr[n-i-1]
        max_product = max(max_product, max(prefix,suffix))
    return max_product

# User Input
size = int(input(f"Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
# result = maximum_product_subarray_brute(array,size)
# print(result)

# result = maximum_product_subarray_better(array,size)
# print(result)

result = maximum_product_subarray_optimal(array,size)
print(result)