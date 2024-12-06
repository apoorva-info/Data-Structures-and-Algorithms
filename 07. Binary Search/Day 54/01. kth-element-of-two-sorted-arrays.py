# Goal: Find the k-th element of two sorted arrays.

# Brute Force Approach
def find_element_brute(arr1,arr2,n1,n2,k):
    n = n1 + n2
    arr = []
    i = 0
    j = 0
    while i < n1 and j <n2:
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while i < n1:
        arr.append(arr1[i])
        i += 1
    while j < n2:
        arr.append(arr2[j])
        j += 1
    print(arr)

    return arr[k-1]

# Time Complexity: O(n)
# Space Complexity: O(n)

# Better Approach
def find_element_better(arr1,arr2,n1,n2,k):
    if n1 > n2:
        return find_element_better(arr2,arr1,n2,n1,k)
    left = k
    low = max(0,k-n2)
    high = min(k,n1)
    while low <= high:
        mid1 = (low + high)//2
        mid2 = left - mid1
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        if mid1 < n1:
            r1 = arr1[mid1]
        if mid2 < n2:
            r2 = arr2[mid2]
        if mid1 - 1>= 0:
            l1 = arr1[mid1-1]
        if mid2 - 1>= 0:
            l2 = arr2[mid2-1]
        if l1 <= r2 and l2 <= r1:
            return max(l1,l2)
        elif l1>r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0


# User Input:
size1 = int(input("Enter the size of array 1: "))
arr1 = []
for i in range(size1):
    element = int(input(f"Enter the element at {i+1} position: "))
    arr1.append(element)
arr1 = sorted(arr1)

size2 = int(input("Enter the size of array 2: "))
arr2 = []
for i in range(size2):
    element = int(input(f"Enter the element at {i+1} position: "))
    arr2.append(element)
arr2 = sorted(arr2)

k = int(input("Enter the value of the k-th element: "))

# Function Call
# result = find_element_brute(arr1,arr2,size1,size2,k)
# print(result)
result = find_element_better(arr1,arr2,size1,size2,k)
print(result)