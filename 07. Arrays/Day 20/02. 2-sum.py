from array import array
# Brute Force Solution
def two_sum_brute(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] + arr[i] == target:
                print(arr[i], arr[j])
                return i,j
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Better Approach
def two_sum_better(arr,target):
    hash_map = {}
    for i in range(len(arr)):
        difference = target - arr[i]        
        if difference in hash_map:
            print(arr[i] , difference)
            return i,hash_map[difference]
        hash_map[arr[i]] = i
    return None
# Time Complexity = O(n)
# Space Complexity = O(n)

# Optimal Approach : Will not be able to tell the indices 
def two_sum_optimal(arr,target):
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return "yes"
        elif arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1
    return "No"
# Time Complexity = O(n log n)
# Space Complexity = O(n)
# Why Space Complexity = O(n)? 
# Because the sorting function makes a new copy of sorted array during the sorting process even if I assign 
# the value of sorted(arr) to arr, a new copy has already been created. If the sorting is done in-place then
# no extra space will be involved and hence, the space complexity will be O(1).



     

















# User Input
user_array = array('i',[])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)

target_value = int(input("Enter the target value: "))

# result = two_sum_brute(user_array,target_value)
# print(result)

# result = two_sum_better(user_array,target_value)
# print(result)

result = two_sum_optimal(user_array,target_value)
print(result)
