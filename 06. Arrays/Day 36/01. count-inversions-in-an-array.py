# Goal: The goal is to count the number of inversions in an array.
# Example:
# Input:
# Enter the size of the list: 6
# Enter the element at lst[0]: 5
# Enter the element at lst[1]: 3
# Enter the element at lst[2]: 2
# Enter the element at lst[3]: 7
# Enter the element at lst[4]: 5
# Enter the element at lst[5]: 4
# Output:
# 7

# Brute Force Approach
def count_inversions_brute(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                count += 1
    return count
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Better Approach
def count_inversions_better(arr,n):
    
# User Input
lst = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)

# Function Call
# result = count_inversions_brute(lst,n) 
# print(result)
result = count_inversions_better(lst,n) 
print(result)