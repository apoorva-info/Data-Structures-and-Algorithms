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
# Time Complexity = O(n)
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
        




# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
x = int(input("Enter the value of the target: "))

# Function Call
result = first_and_last_occurrence_brute(array,size,x)
print(first_and_last_occurrence_brute)