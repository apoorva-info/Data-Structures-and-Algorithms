# Goal: Find the single element in a sorted array.
# Example:
# Input:
# Enter the size of the sorted array: 11
# Enter the element at array[0]: 1
# Enter the element at array[1]: 1
# Enter the element at array[2]: 2
# Enter the element at array[3]: 2
# Enter the element at array[4]: 3
# Enter the element at array[5]: 3
# Enter the element at array[6]: 4
# Enter the element at array[7]: 5
# Enter the element at array[8]: 5
# Enter the element at array[9]: 6
# Enter the element at array[10]: 6
# Output:
# 4

# Brute Force Approach: Linear Search
def single_element_brute(arr,n):
    if n == 1:
        return arr[0]
    else:
        for i in range(n):
            if i == 0:
                if arr[i] != arr[i+1]:
                    return arr[i]

            elif i == n-1:
                if arr[i] != arr[i-1]:
                    return arr[i]

            else:
                if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
                    return arr[i]
            
# Time Complexity = O(n)
# Space Complexity = O(1)

# Binary Search
# (even,odd) ---> Element is on the right half
# (odd,even) ---> Element is on the left half

def single_element_binary(arr,n):
    if n == 1:
        return arr[n]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    else:
        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high)//2
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
                return arr[mid]
            if (mid % 2 == 1 and arr[mid - 1] == arr[mid]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1
            
        

# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
# result = single_element_brute(array,size)
# print(result)
result = single_element_binary(array,size)
print(result)