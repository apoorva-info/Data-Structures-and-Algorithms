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
result = find_element_brute(arr1,arr2,size1,size2,k)
print(result)