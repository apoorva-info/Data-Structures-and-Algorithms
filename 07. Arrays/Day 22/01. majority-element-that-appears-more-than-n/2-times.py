from array import array
# Brute Force Approach
def majority_element_brute(arr,n):
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
                if count > n//2:
                    return arr[i]
# Time Complexity = O(n^2)
# Space Complexity = O(1)

                
# Better Approach
def majority_element_better(arr,n):
    max_element = max(arr)
    hash_arr = [0] * (max_element+1)
    for i in range(n):
        hash_arr[arr[i]] += 1
    for i in range(max_element+1):
        if hash_arr[i] > n/2:
            return i
    return None
# Time Complexity = O(n)
# Space Complexity = O(n)

# Optimal Approach
# Moore"s Voting Algorithm
def majority_element_optimal(arr,n):
    count = 0
    for i in range(n):
        if count == 0:
            element = arr[i]
        elif arr[i] == element:
            count += 1
        else:
            count -= 1
    count1 = 0
    for i in range(n):
        if arr[i] == element:
            count1 += 1
    if count1 > n//2:
        return element
# Time Complexity = O(n)
# Space Complexity = O(1)
    

        








user_array = array('i', [])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)
print(user_array)

# result = majority_element_brute(user_array,size)
# print(result)
# result = majority_element_better(user_array,size)
# print(result)
result = majority_element_optimal(user_array,size)
print(result)