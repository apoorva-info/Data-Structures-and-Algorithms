# Brute Force Approach
def number_of_subarrays_with_sum_k_brute(arr,k,n):
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum = 0
            for m in range(i,j+1):
                sum = sum + arr[m]
            if sum == k:
                count+=1
    return count
# Time Complexity = O(n^3)
# Space Complexity = O(1)
















# User Input
k = int(input("Enter the value of k: "))
n = int(input("Enter the number of elements in the array: "))
user_array = []

for i in range(n):
    element = int(input(f"Enter the element at arr[{i}]: "))
    user_array.append(element)
# print(user_array)

result = number_of_subarrays_with_sum_k_brute(user_array,k,n)
print(result)