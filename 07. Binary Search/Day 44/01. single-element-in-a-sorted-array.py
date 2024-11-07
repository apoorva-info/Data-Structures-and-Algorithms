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

# Brute Force Approach
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



# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
result = single_element_brute(array,size)
print(result)