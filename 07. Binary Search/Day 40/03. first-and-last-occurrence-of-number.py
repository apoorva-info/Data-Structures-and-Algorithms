# Gaol: Find the first and last occurrence of a given number in a sorted array.
# Example:
# Input:
# Enter the size of the sorted array: 5
# Enter the element at array[0]: 1
# Enter the element at array[1]: 2
# Enter the element at array[2]: 2
# Enter the element at array[3]: 3
# Enter the element at array[4]: 5
# Enter the value of the target: 2
# Output:
# (1, 2)

# Brute Force Approach
def first_and_last_occurrence_brute(arr,n,x):
    first = -1
    last = -1
    for i in range(n):
        if arr[i] == x:
            if first == -1:
                first = i
            last = i
    return first,last
# Time Complexity = O(log n)
# Space Complexity = O(1)

# Binary Search
def lower_bound(arr,n,x):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1     
    return ans

def upper_bound(arr,n,x):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high)//2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1     
    return ans

def first_and_last_occurrence_using_binary_search(arr,n,x):
    lb = lower_bound(arr,n,x)
    if lb == n or arr[lb] != x:
        return (-1,-1)
    else:
        return {lb,upper_bound(arr,n,x)-1}
# Time Complexity = O(log n)
# Space Complexity = O(1)

# Without using lower bound and upper bound function
def first_occurrence(arr,n,x):
    low = 0
    high = n - 1
    first = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return first

def last_occurrence(arr,n,x):
    low = 0
    high = n - 1
    last = -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return last
    

# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
x = int(input("Enter the value of the target: "))

# Function Call
# result = first_and_last_occurrence_brute(array,size,x)
# print(first_and_last_occurrence_brute)

# result = first_and_last_occurrence_using_binary_search(array,size,x)
# print(result)

result = first_and_last_without_lb_and_ub(array,size,x)
print(result)
