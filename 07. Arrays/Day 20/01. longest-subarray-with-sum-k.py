from array import array
# Brute Force Solution
def longest_sub_array_brute(arr,k):
    length = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)): 
            current_sum = 0
            for l in range(i,j+1):
                current_sum += arr[l]
            if current_sum == k:
                length = max(length,j-i+1)
    return length
# Time Complexity = O(n^3)
# Space Complexity = O(1)

# Better Solution
def longest_sub_array_better(arr,k):
    length = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):  
            sum = sum + arr[j]
            if sum == k:
                current_length = j-i+1
                length = max(length,current_length)             
    return length
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Optimal Solution
def longest_sub_array_optimal(arr,k):
    sum_map = {}
    max_length = 0
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
        if sum == k:
            max_length = i+1
        if (sum - k) in sum_map:
            max_length = max(max_length , i - sum_map[sum - k])
        if sum not in sum_map:
            sum_map[sum] = i

    return max_length
# Time Complexity = O(n)
# Space Complexity = O(n)

        



user_array = array('i', [])
n = int(input("Enter the size of the array: "))
for i in range(n):
    element = int(input(f"Enter the element of the array[{i}]: "))
    user_array.append(element)
k = int(input("Enter the value of k: "))
result1 = longest_sub_array_brute(user_array,k)
print(f"The length of the longest sub-array with sum {k} is {result1}.")
result2 = longest_sub_array_better(user_array,k)
print(f"The length of the longest sub-array with sum {k} is {result2}.")
result3 = longest_sub_array_optimal(user_array,k)
print(f"The length of the longest sub-array with sum {k} is {result3}.")