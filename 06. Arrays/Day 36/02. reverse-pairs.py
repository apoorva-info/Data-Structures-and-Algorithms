# Goal : The goal is to find the number of elements with reverse pairs i.e. if i < j then a[i] > 2 * a[j]
# Example:
# Input:
# Enter the size of the array: 7
# Enter the element at array[0]: 40
# Enter the element at array[1]: 25
# Enter the element at array[2]: 19
# Enter the element at array[3]: 9
# Enter the element at array[4]: 6
# Enter the element at array[5]: 2
# Enter the element at array[6]: 5
# Output:
# 15

# Brute Force Approach
def reverse_pairs_brute(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > 2 * arr[j]:
                count += 1
    return count
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# User Input
size = int(input(f"Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
    
# Function Call
result = reverse_pairs_brute(array,size)
print(result)