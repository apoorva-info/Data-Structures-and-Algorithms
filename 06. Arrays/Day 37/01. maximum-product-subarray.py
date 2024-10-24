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
        product = arr[i]
        for j in range(i+1,n):
            product = product * arr[j]
            max_product = max(product,max_product)
    return max_product






# User Input
size = int(input(f"Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
result = maximum_product_subarray_brute(array,size)
print(result)