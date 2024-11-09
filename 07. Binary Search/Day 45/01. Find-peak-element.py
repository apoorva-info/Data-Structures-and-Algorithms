# Goal: Find the peak element.
# Peak Element:  arr[i-1] < arr[i] > arr[i+1]

# Brute Force Approach
def peak_element(arr,n):
    for i in range(0,n):
        if i == 0:
            if arr[i] > arr[i+1]:
                return arr[i]
        elif i == n:
            if arr[i] > arr[i-1]:
                return arr[i]
        else:
            if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
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
result = peak_element(array,size)
print(result)
