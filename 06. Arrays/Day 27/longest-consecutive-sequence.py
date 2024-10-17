# Goal: This code finds the length of the longest consecutive subsequence in an unsorted array.
# It implements three approaches: brute force, better approach, and an optimal approach using a set.

# Example:
# Input:
# Enter the size of the list: 7
# Enter the element at array[0]: 100
# Enter the element at array[1]: 4
# Enter the element at array[2]: 200
# Enter the element at array[3]: 1
# Enter the element at array[4]: 3
# Enter the element at array[5]: 2
# Enter the element at array[6]: 101
# Output:
# 4 

# Brute Force Approach: Check if each number has the next consecutive number in the array
def ls(arr, a):
    for i in arr:
        if a == i:
            return True
    return False

def longest_consecutive_brute(arr, n):
    longest = 1
    for i in range(n):
        x = arr[i]
        count = 1
        while ls(arr, x + 1) == True:
            x = x + 1
            count = count + 1
        longest = max(count, longest)
    return longest
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Better Approach: Sort the array and count consecutive elements
def longest_consecutive_better(arr, n):
    arr = sorted(arr)
    longest = 1
    count = 0 
    last_smallest = float('-inf')
    for i in range(n):
        if arr[i] - 1 == last_smallest:
            count = count + 1
            last_smallest = arr[i]
        elif arr[i] != last_smallest:
            count = 1
            last_smallest = arr[i]
        longest = max(longest, count)
    return longest
# Time Complexity = O(n log n)
# Space Complexity = O(n)

# Optimal Approach: Use a set to find consecutive elements in linear time
def longest_consecutive_optimal(arr, n):
    if n == 0:
        return 0 
    
    longest = 1
    arr = set(arr)

    for num in arr:
        # Check if it's the start of a sequence
        if num - 1 not in arr:
            current_num = num
            count = 1
            # Count consecutive numbers
            while current_num + 1 in arr:
                count += 1
                current_num += 1
            longest = max(longest, count)
    return longest
# Time Complexity = O(n)
# Space Complexity = O(n)

# User Input
size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# Uncomment to test brute force approach
# result = longest_consecutive_brute(array, size)
# print(result)

# Uncomment to test better approach
# result = longest_consecutive_better(array, size)
# print(result)

# Use the optimal approach
result = longest_consecutive_optimal(array, size)
print(result)
