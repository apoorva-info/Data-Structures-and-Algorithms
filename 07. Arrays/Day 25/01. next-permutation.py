


def permutations(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    permutations_list = []

    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for p in permutations(remaining):
            permutations_list.append([current]+p)
    return permutations_list



# Brute Force Approach
def next_permutation_brute(arr):
    permutation_list = permutations(arr)
    permutation_list = sorted(permutation_list)
    for i in range(len(permutation_list)):
        if permutation_list[i] == arr:
            if i+1 < len(permutation_list):
                return permutation_list[i+1]
            else:
                return permutation_list[0]
# Time Complexity = O(n! * n log (n!))
# Space Complexity = O(n! * n)

import itertools
# Better Approach
def next_permutation_better(arr):
    permutation_list = list(itertools.permutations(arr)) # Returns a tuple so conversion to list is important.
    permutation_list = sorted(permutation_list)
    for i,value in enumerate(permutation_list):
        if value == tuple(arr):
            if i + 1 < len(permutation_list):
                return list(permutation_list[i+1])
            else:
                return list(permutation_list[0])
# Time Complexity = O(n! * n log (n!))
# Space Complexity = O(n! * n)









size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# result = next_permutation_brute(array)
# print(result)

result = next_permutation_better(array)
print(result)