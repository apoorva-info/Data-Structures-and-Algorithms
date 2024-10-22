# Goal: This code merges two sorted arrays while maintaining the sorted order.
# It implements three approaches: brute force, optimal approach with sorting, and gap method.
# Example:
# Input:
# Enter the size of lst1: 3
# Enter the element at [0]: 1
# Enter the element at [1]: 4
# Enter the element at [2]: 8
# Enter the size of lst2: 2
# Enter the element at [0]: 2
# Enter the element at [1]: 5
# Output:
# Initial arrays: [1, 4, 8] [2, 5]
# Final arrays: ([1, 2, 4], [5, 8])

def merge_sorted_arrays_brute(arr1,arr2,m,n):
    arr3 = [0] * (m+n)
    left = 0 
    right = 0
    index = 0
    while left < m and right < n:
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
            index += 1
        else:
            arr3[index] = arr2[right]
            right += 1
            index += 1
    while left < m:
        arr3[index] = arr1[left]
        index += 1
        left += 1
    while right < n:
        arr3[index] = arr2[right]
        index += 1
        right += 1
    for i in range(m):
        arr1[i] = arr3[i]
    for i in range(m,m+n):
        arr2[i-m] = arr3[i]

    return arr1,arr2
# Time Complexity = O(m+n)
# Space Complexity = O(m+n)

# Optimal Approach 1
def optimal_approach1(arr1,arr2,m,n):
    left = m - 1
    right = 0
    while left >= 0 and right < n:
        if arr1[left] > arr2[right]:
            arr1[left],arr2[right] = arr2[right],arr1[left]
            left -= 1
            right += 1
        else:
            break
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    return arr1,arr2
# Time Complexity = O(min(m,n)) + O(m log m) + O(n log n)
# Space Complexity = O(1)

# Optimal Approach 2
# Gap Method
def swapifgreater(arr1,arr2,ind1,ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]
    
def optimal_approach2(arr1,arr2,m,n):
    len = m + n
    gap = (len // 2) + (len % 2)
    while gap > 0:
        left = 0
        right = left + gap
        while right < m+n:
            # Case 1: When left is in arr1 and right is in arr2 
            if left < m and right >= m:
                swapifgreater(arr1,arr2,left,right-m)

            # Case 2: When both are in arr2
            elif left >= m:
                swapifgreater(arr2,arr2,left-m,right-m)

            # Case 3: When both are in arr1
            else:
                swapifgreater(arr1,arr1,left,right)

            left += 1
            right += 1
        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)
    return arr1,arr2

# User Input
lst1 = []
lst2 = []

m = int(input("Enter the size of lst1: "))
for i in range(m):
    element1 = int(input(f"Enter the element at [{i}]: "))
    lst1.append(element1)

n = int(input("Enter the size of lst2: "))
for i in range(n):
    element2 = int(input(f"Enter the element at [{i}]: "))
    lst2.append(element2)

print(lst1)
print(lst2)

# result = merge_sorted_arrays_brute(lst1,lst2,m,n)
# print(result)

# result = optimal_approach1(lst1,lst2,m,n)
# print(result)

result = optimal_approach2(lst1,lst2,m,n)
print(result)