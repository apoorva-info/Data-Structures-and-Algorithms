# Function to find the missing number in an array

from array import array

# Brute Force Approach 1
def missing_number_brute(arr,n):
    for i in range(1,n):
        flag = 0
        for j in range(n-1):
            if arr[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
# Time Complexity = O(n^2)
# Space Complexity = O(1)


# Brute Force Approach 2
def missing_number(arr,n):
    for i in range(1,n+1):
        if i not in arr: # ---> Runs for n times for each element 
            return i
# Time Complexity = O(n^2)
# Space Complexity = O(1)


# Better Approach
def missing_number_using_hashing(arr,n):
    # Pre Computation
    hash_list = [0] * (n+1)
    for i in range(n-1):
        hash_list[arr[i]] += 1
    # Fetch
    for i in range(1,n):
        if hash_list[i] == 0:
            return i
# Time Complexity = O(n)
# Space Complexity = O(n)
  
# Optimal Approach 1
def missing_number_using_sum(arr,n):
    sum_of_n_numbers = n*(n+1)/2
    sum_of_numbers_in_array = 0
    for i in range(n-1):
        sum_of_numbers_in_array = sum_of_numbers_in_array + arr[i]
    return sum_of_n_numbers - sum_of_numbers_in_array
# Time Complexity = O(n)
# Space Complexity = O(1)

# Optimal Approach 2
def missing_number_using_xor(arr,n):
    xor1 = 0 
    for i in range(1,n+1):
        xor1 = xor1 ^ i
    xor2 = 0 
    for i in arr:
        xor2 = xor2 ^ i
    return xor1^xor2
# Time Complexity = O(n)
# Space Complexity = O(1)


# User Input
user_array = array('i',[2,5,4,3,1,7])
len_of_user_array = 7

# Function Call
# result1 = missing_number_brute(user_array,len_of_user_array)
# print(f"Missing number: {result1}")
# result2 = missing_number(user_array,len_of_user_array)
# print(f"Missing number: {result2}")
# result3 = missing_number_using_hashing(user_array,len_of_user_array)
# print(f"Missing number: {result3}")
# result4 = missing_number_using_sum(user_array,len_of_user_array)
# print(f"Missing number: {result4}")
result5 = missing_number_using_xor(user_array,len_of_user_array)
print(f"Missing number: {result5}")