# Goal: To find the median of two sorted arrays of different sizes.

# Brute Force Approach
def find_median_brute(arr1,arr2,n1,n2):
    i = 0 
    j = 0
    arr = []
    while (i < n1 and j < n2):
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

    n = n1 + n2

    if n % 2 == 0:
        median = (arr[n//2] + arr[(n//2)-1])/2
        return median
    else:
        median = arr[n//2]
        return median
# Time Complexity: O(n)
# Space Complexity: O(n)

# Better Approach
def find_median_better(arr1,arr2,n1,n2):
    i = 0
    j = 0
    n = n1 + n2
    ind2 = n//2
    ind1 = ind2 - 1
    count = 0
    ind1_element = -1 
    ind2_element = -1

    while (i < n1 and j < n2):
        if arr1[i] < arr2[j]:
            if count == ind1:
                ind1_element = arr1[i]
            elif count == ind2:
                ind2_element = arr1[i]
            count += 1
            i += 1
        else:
            if count == ind1:
                ind1_element = arr2[j]
            elif count == ind2:
                ind2_element = arr2[j]
            count += 1
            j += 1

    while(i < n1):
        if count == ind1:
            ind1_element = arr1[i]
        elif count == ind2:
            ind2_element = arr1[i]
        count += 1
        i += 1

    while(j < n2):
        if count == ind1:
            ind1_element = arr2[j]
        elif count == ind2:
            ind2_element = arr2[j]
        count += 1
        j += 1
        
    if n % 2 == 0:
        return (ind1_element + ind2_element)/2
    else:
        return ind2_element
            
# Time Complexity: O(n)
# Space Complexity: O(1)
        
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

# Function Call 
# result = find_median_brute(arr1,arr2,size1,size2)
# print(result)
result = find_median_better(arr1,arr2,size1,size2)
print(result)