# Goal: This code finds the maximum subarray sum in an array using three approaches: 
# brute force, a better approach, and Kadane's Algorithm (optimal approach).

# Example:
# Input:
# Enter the size of the list: 5
# Enter the element at array[0]: -2
# Enter the element at array[1]: 1
# Enter the element at array[2]: -3
# Enter the element at array[3]: 4
# Enter the element at array[4]: -1
# Output:
# Maximum subarray sum: 4, starting from index 3 to 3

# Brute Force Approach: Check every possible subarray to find the maximum sum
def max_sub_array_sum_brute(arr, n):
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j + 1):
                sum = sum + arr[k]
            max_sum = max(sum, max_sum)
    return max_sum
# Time Complexity = O(n^3)
# Space Complexity = O(1)

# Better Approach: Use two loops to calculate the sum of each subarray
def max_sub_array_sum_better(arr, n):
    max_sum = float('-inf')
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum = sum + arr[j]
            max_sum = max(sum, max_sum)
    return max_sum
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Optimal Approach: Kadane's Algorithm to find the maximum subarray sum in O(n) time
def max_sub_array_sum_optimal(arr, n):
    sum = 0
    max_sum = float('-inf')
    start = 0  # To track the start index of the subarray
    end = 0    # To track the end index of the subarray
    for i in range(n):
        if sum == 0:
            start = i
        sum = sum + arr[i]
        if max_sum < sum:
            max_sum = sum
            end = i
        if sum < 0:
            sum = 0
    return max_sum, start, end
# Time Complexity = O(n)
# Space Complexity = O(1)

# User Input
size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# Uncomment the approach you want to use:
# result = max_sub_array_sum_brute(array, size)
# print(result)

# result = max_sub_array_sum_better(array, size)
# print(result)

result = max_sub_array_sum_optimal(array, size)
print(result)
