# Goal:
# Given an integer array `arr` of size `n`, find all elements that appear more than ⌊ n/3 ⌋ times.
# You need to solve this problem using a brute force, better, and optimal approach.

# Example:
# Input: arr = [3, 2, 3], n = 3
# Output: [3]

# Input: arr = [1,1,1,3,3,2,2,2], n = 8
# Output: [1, 2]

# Brute Force Approach
def majority_elements_brute(arr, n):
    ans = []
    for i in range(n):
        if ans == [] or ans[0] != arr[i]:
            count = 0
            for j in range(n):
                if arr[i] == arr[j]:
                    count += 1
            if count > (n // 3):
                ans.append(arr[i])
            if len(ans) == 2:
                break
    return ans
# Time Complexity = O(n^2)
# Space Complexity = O(1)

from collections import defaultdict

# Better Approach using Hashmap
def majority_elements_better(arr, n):
    hash_lst = defaultdict(int)
    minimum_value = n // 3
    ans = []
    for i in range(n):
        hash_lst[arr[i]] += 1
        if hash_lst[arr[i]] == minimum_value:
            ans.append(arr[i])
        if len(ans) == 2:
            break
    return ans
# Time Complexity = O(n)
# Space Complexity = O(n)

# Optimal Approach using Moore's Voting Algorithm
def majority_elements_optimal(arr, n):
    element1 = float('-inf')
    count1 = 0
    element2 = float('inf')
    count2 = 0
    ans = []

    # First pass to find potential candidates
    for i in range(n):
        if count1 == 0 and arr[i] != element2:
            count1 = 1
            element1 = arr[i]
        elif count2 == 0 and arr[i] != element1:
            count2 = 1
            element2 = arr[i]
        elif arr[i] == element1:
            count1 += 1
        elif arr[i] == element2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    # Second pass to confirm if they appear more than n//3 times
    count1 = 0
    count2 = 0
    for i in range(n):
        if arr[i] == element1:
            count1 += 1
        if arr[i] == element2:
            count2 += 1

    if count1 > n // 3:
        ans.append(element1)
    if count2 > n // 3:
        ans.append(element2)
    
    return ans
# Time Complexity = O(n)
# Space Complexity = O(1)


# User Input
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
print(lst)

# Uncomment to test each approach
# result = majority_elements_brute(lst, n)
# print(result)
# result = majority_elements_better(lst, n)
# print(result)
result = majority_elements_optimal(lst, n)
print(result)
