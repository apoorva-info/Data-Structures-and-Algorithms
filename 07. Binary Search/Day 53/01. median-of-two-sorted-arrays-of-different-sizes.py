# Goal: To find the median of two sorted arrays of different sizes.

# Brute Force Approach
def find_median_brute(arr1,arr2):
    arr = arr1 + arr2
    arr = sorted(arr)
    n = len(arr)
    print(arr)

    if n % 2 == 0:
        median = (arr[(n/2)] + arr[(n/2)+1])/2
        return median
    else:
        median = arr[n/2]
        return median


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
result = find_median_brute(arr1,arr2)
print(result)