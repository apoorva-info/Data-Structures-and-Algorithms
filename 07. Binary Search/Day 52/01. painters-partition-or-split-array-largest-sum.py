# Goal: Split the array into k subarrays such that the max subarray sum is minimum.

# Brute Force Approach
def fun(arr,i):
    count = 1
    sum_area = 0
    for j in arr:
        if sum_area + j <= i:
            sum_area += j
        else:
            count += 1
            sum_area = j
    return count
            
def split_arrays_brute(arr,k,n):
    if k > n:
        return -1
    else:
        low = max(arr)
        high = sum(arr)
        for i in range(low, high+1):
            count_painters = fun(arr,i)
            if count_painters == k:
                return i
            
# Time Complexity: O(sum - max + 1) * O(n) 
# Space Complexity: O(1)




# User Input
k = int(input("Enter the number of subarrays: "))

size = int(input("Enter the size of the array: "))
lst = []
for i in range(size):
    element = int(input(f"Enter the element at {i+1} position: "))
    lst.append(element)

print(lst)

# Function Call 
result = split_arrays_brute(lst,k,size)
print(result)