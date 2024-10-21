# Goal: Implement three different approaches to count the number of subarrays with XOR equal to k.
# This problem aims to find the count of subarrays in a given array where the XOR of all elements in the subarray equals a given value k.

# Example:
# Input: arr = [4, 2, 2, 6, 4], k = 6
# Output: 4
# Explanation: The subarrays with XOR 6 are [4, 2], [2, 2, 6], [6], [2, 2, 6, 4]

# Brute Force Approach
def count_subarrays_with_xor_k_brute(arr,n,k):
    count = 0
    for i in range(n):
        for j in range(i,n):
            XOR = 0
            for l in range(i,j+1):
                XOR = XOR ^ arr[l]
            if XOR == k:
                count += 1
    return count
# Time Complexity = O(n^3)
# Space Complexity = O(1)

# Better Approach
def count_subarrays_with_xor_k_better(arr,n,k):
    count = 0
    for i in range(n):
        XOR = 0
        for j in range(i,n):
            XOR = XOR ^ arr[j]
            if XOR == k:
                count += 1
    return count
# Time Complexity = O(n^2)
# Space Complexity = O(1)

from collections import defaultdict
# Optimal Approach
def count_subarrays_with_xor_k_optimal(arr,n,k):
    count = 0
    xr = 0
    hash_map = defaultdict(int)
    hash_map[xr] = 1
    for i in range(n):
        xr = xr ^ arr[i]
        x = xr ^ k 
        count += hash_map[x]
        hash_map[xr] += 1
    return count
# Time Complexity = O(n)
# Space Complexity = O(n)

# User Input
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
k = int(input("Enter the value of k: "))
print(lst)

# result = count_subarrays_with_xor_k_brute(lst,n,k)
# print(result)

# result = count_subarrays_with_xor_k_better(lst,n,k)
# print(result)

result = count_subarrays_with_xor_k_optimal(lst,n,k)
print(result)