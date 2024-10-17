# Function to find the number that appears once, and the others appears twice.
# Example:
# Input:
# Enter the size of the array: 5
# Enter either 1 or 0 at array[0]: 4
# Enter either 1 or 0 at array[1]: 4
# Enter either 1 or 0 at array[2]: 3
# Enter either 1 or 0 at array[3]: 2
# Enter either 1 or 0 at array[4]: 2
# Output:
# 3

from array import array

# Brute Force Approach
def find_number_brute(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Better Approach
def find_number_better(arr,n):
    max_num = max(arr)
    hash_list = [0] * (max_num+1)
    # Pre Computation 
    for i in arr:
        hash_list[i] += 1
    # Fetch
    for i in range(n):
        if hash_list[arr[i]] == 1:
            return arr[i]
# Time Complexity = O(3n)
# Space Complexity = O(max_num)
"""
If there are large values, use map data structure.
"""
    
    
    

# Optimal Approach
def find_number_optimal(arr):
    xor = 0
    for i in arr:
        xor ^= i
    return xor
# Time Complexity = O(n)
# Space Complexity = O(1)



# User Input 
user_array = array('i',[])
n = int(input("Enter the size of the array: "))
for i in range(n):
    element = int(input(f"Enter either 1 or 0 at array[{i}]: "))
    user_array.append(element)

# Function Call
# result1 = find_number_optimal(user_array)
# print(result1)
# result2 = find_number_brute(user_array)
# print(result2)
result3 = find_number_better(user_array,n)
print(result3)