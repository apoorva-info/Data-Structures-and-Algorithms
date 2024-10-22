# Goal: The goal is to find the repeated and missing number in a given array.
# User Input

# Brute Force Approach
def repeating_and_missing_elements_brute(arr,n):
    repeated_number = -1
    missing_number = -1
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == i:
                count += 1
        if count == 0:
            missing_number = i
        elif count == 2:
            repeated_number = i
        if repeated_number != -1 and missing_number != -1:
            break
    return repeated_number, missing_number

# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Better Approach
def repeating_and_missing_elements_better(arr,n):
    max_element = max(arr)
    min_element = min(arr)
    hash_set = [0] * (max_element+1)
    for i in arr:
        hash_set[i] += 1
    repeated_number = -1
    missing_number = -1
    for i in range(min_element,max_element+1):
        if hash_set[i] == 0:
            missing_number = i
        elif hash_set[i] == 2:
            repeated_number = i
        if repeated_number != -1 and missing_number != -1:
            break
    return repeated_number, missing_number
# Time Complexity = O(n)
# Space Complexity = O(n)


lst = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
print(lst)

# result = repeating_and_missing_elements_brute(lst,n)
# print(result)

result = repeating_and_missing_elements_better(lst,n)
print(result)