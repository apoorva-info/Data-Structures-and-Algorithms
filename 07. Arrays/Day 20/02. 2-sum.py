# Goal: This code finds two numbers in the array that sum up to a given target value.
# It provides three approaches: brute force, better approach using a hash map, and an optimal solution using two pointers.
# The optimal approach checks if such a pair exists but does not return the indices.

# Example:
# Input:
# Enter the size of the array: 5
# Enter the element at array[0]: 2
# Enter the element at array[1]: 7
# Enter the element at array[2]: 11
# Enter the element at array[3]: 15
# Enter the element at array[4]: 1
# Enter the target value: 9
# Output:
# Brute Force: 2 7 (indices: 0, 1)
# Better Approach: 2 7 (indices: 0, 1)
# Optimal Approach: Yes

from array import array

# Brute Force Solution: Check every pair of elements to find the sum
def two_sum_brute(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] + arr[i] == target:
                print(arr[i], arr[j])
                return i, j
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Better Approach: Use a hash map to store visited elements and find the pair in a single pass
def two_sum_better(arr, target):
    hash_map = {}
    for i in range(len(arr)):
        difference = target - arr[i]        
        if difference in hash_map:
            print(arr[i], difference)
            return i, hash_map[difference]
        hash_map[arr[i]] = i
    return None
# Time Complexity = O(n)
# Space Complexity = O(n)

# Optimal Approach: This approach finds the pair but does not return the indices
def two_sum_optimal(arr, target):
    arr = sorted(arr)  # Sorting the array for two-pointer technique
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return "Yes"
        elif arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1
    return "No"
# Time Complexity = O(n log n) due to the sorting step
# Space Complexity = O(n)
# Why Space Complexity is O(n)?
# The space complexity is O(n) because the sorting function creates a new copy of the array during the sorting process.
# Even if I assign the sorted array back to `arr`, a new copy has already been created.
# If sorting were done in-place, the space complexity would be O(1).

# User Input
user_array = array('i', [])  # Create an empty integer array
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)

target_value = int(input("Enter the target value: "))

# Uncomment the approach you want to use:
# result = two_sum_brute(user_array, target_value)
# print(result)

# result = two_sum_better(user_array, target_value)
# print(result)

result = two_sum_optimal(user_array, target_value)
print(result)
