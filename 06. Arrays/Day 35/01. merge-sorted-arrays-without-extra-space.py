def merge_sorted_arrays_brute(arr1,arr2,m,n):
    arr3 = [0] * (m+n)
    left = 0 
    right = 0
    index = 0
    while left < m and right < n:
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
            index += 1
        else:
            arr3[index] = arr2[right]
            right += 1
            index += 1
    while left < m:
        arr3[index] = arr1[left]
        index += 1
        left += 1
    while right < n:
        arr3[index] = arr2[right]
        index += 1
        right += 1
    for i in range(m):
        arr1[i] = arr3[i]
    for i in range(m,m+n):
        arr2[i-m] = arr3[i]

    return arr1,arr2
# Time Complexity = O(m+n)
# Space Complexity = O(m+n)

# Optimal Approach 1
def optimal_approach1(arr1,arr2,m,n):
    left = m - 1
    right = 0
    while left >= 0 and right < n:
        if arr1[left] > arr2[right]:
            arr1[left],arr2[right] = arr2[right],arr1[left]
            left -= 1
            right += 1
        else:
            break
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    return arr1,arr2
    

# User Input
lst1 = []
lst2 = []

m = int(input("Enter the size of lst1: "))
for i in range(m):
    element1 = int(input(f"Enter the element at [{i}]: "))
    lst1.append(element1)

n = int(input("Enter the size of lst2: "))
for i in range(n):
    element2 = int(input(f"Enter the element at [{i}]: "))
    lst2.append(element2)

print(lst1)
print(lst2)

# result = merge_sorted_arrays_brute(lst1,lst2,m,n)
# print(result)

result = optimal_approach1(lst1,lst2,m,n)
print(result)