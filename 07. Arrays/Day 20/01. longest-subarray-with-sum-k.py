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


        



user_array = array('i', [])
n = int(input("Enter the size of the array: "))
for i in range(n):
    element = int(input(f"Enter the element of the array[{i}]: "))
    user_array.append(element)
k = int(input("Enter the value of k: "))
result = longest_sub_array_brute(user_array,k)
print(f"The length of the longest sub-array with sum {k} is {result}.")