# Goal: Given an array and k, find the kth missing positive integer.

# Brute Force Approach
def missing_number_brute(nums,n,k):
    for i in range(n):
        if nums[i] <= k:
            k += 1
        else:
            break
    return k
# Time Complexity: O(n)
# Space Complexity: O(1)

# Better Approach
def missing_number_better(arr,n,k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return (high + 1 + k)

    






# User Input
size = int(input("Enter the size of the array: "))
arr = []
for i in range(size):
    element = int(input(f"Enter the element at {i+1} position: "))
    arr.append(element)
print(arr)

k = int(input("Enter the value of k: "))

# Function Call
result = missing_number_brute(arr,size,k) 
print(result)
