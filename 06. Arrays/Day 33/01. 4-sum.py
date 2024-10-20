# Goal: Implement three different approaches to solve the Four Sum problem.
# The Four Sum problem aims to find all unique quadruplets in an array that sum up to a given target value.

# Example:
# Input: arr = [1, 0, -1, 0, -2, 2], target = 0
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

# Brute Force Approach
def four_sum_brute(arr, n, target):
    ans = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        temp.sort()
                        ans.add(tuple(temp))
    return ans

# Time Complexity = O(n^4)
# Space Complexity = O(no. of quads)*2(in which you store the answer and return)

# Better Approach
def four_sum_better(arr, n, target):
    ans = set()
    for i in range(n):
        for j in range(i+1, n):
            hash_set = set()
            for k in range(j+1, n):
                l = target - (arr[i] + arr[j] + arr[k])
                if l in hash_set:
                    temp = [arr[i], arr[j], arr[k], l]
                    temp.sort()
                    ans.add(tuple(temp))
                hash_set.add(arr[k])
    return ans

# Time Complexity = O(n^3)
# Space Complexity = O(n) + O(no. of quads)*2(in which you store the answer and return)

# Optimal Approach
def four_sum_optimal(arr, n, target):
    ans = set()
    arr = sorted(arr)  # Sort the array to enable two-pointer technique
    for i in range(n):
        # Skip duplicates for the first element
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, n):
            # Skip duplicates for the second element
            if j != i + 1 and arr[j] == arr[j-1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                sum = arr[i] + arr[j] + arr[k] + arr[l]
                if sum == target:
                    temp = [arr[i], arr[j], arr[k], arr[l]]
                    ans.add(tuple(temp))
                    k += 1
                    l -= 1
                    # Skip duplicates for third and fourth elements
                    while k < l and arr[k] == arr[k-1]:
                        k += 1
                    while k < l and arr[l] == arr[l+1]:
                        l -= 1
                elif sum < target:
                    k += 1
                else:
                    l -= 1
    return ans

# Time Complexity = O(n^3)
# Space Complexity = O(no. of quads)*2(in which you store the answer and return)

# User Input
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
target = int(input("Enter the value of the target: "))
print(lst)

# Uncomment the desired function call
# result = four_sum_brute(lst, n, target)
# result = four_sum_better(lst, n, target)
result = four_sum_optimal(lst, n, target)
print(result)