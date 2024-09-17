from array import array

# Brute Force Approach
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




# Better Solution
def missing_number(arr,n):
    for i in range(1,n+1):
        if i not in arr: # ---> Runs for n times for each element 
            return i
# Time Complexity = O(n^2)
# Space Complexity = O(1)


# User Input
user_array = array('i',[2,5,4,3,1,7])
len_of_user_array = 7
result1 = missing_number_brute(user_array,len_of_user_array)
print(f"Missing number: {result1}")
# result2 = missing_number(user_array,len_of_user_array)
# print(f"Missing number: {result2}")
