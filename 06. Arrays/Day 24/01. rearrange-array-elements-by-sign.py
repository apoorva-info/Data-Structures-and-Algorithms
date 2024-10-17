# Goal: This code rearranges the elements of an array such that positive and negative numbers alternate.
# It uses two approaches: a brute force approach and an optimal approach. The array size must be even for this rearrangement.

# Example:
# Input:
# Enter the size of the list: 6
# Enter the element at array[0]: -1
# Enter the element at array[1]: 2
# Enter the element at array[2]: -3
# Enter the element at array[3]: 4
# Enter the element at array[4]: -5
# Enter the element at array[5]: 6
# Output:
# [-1, 2, -3, 4, -5, 6]

# Brute Force Approach: Separate positive and negative numbers, then rearrange them
def rearrange_elements_brute(arr, n):
    if n % 2 != 0:
        return "The size is invalid."
    else:
        positive_arr = []
        negative_arr = []
        # Separate positive and negative numbers
        for i in range(n):
            if arr[i] > 0:
                positive_arr.append(arr[i])
            else:
                negative_arr.append(arr[i])
        # Alternate positive and negative numbers
        for i in range(0, n // 2, 2):
            arr[i] = positive_arr[i]
        for i in range(1, n // 2, 2):
            arr[i] = negative_arr[i]
        return arr
# Time Complexity = O(n)
# Space Complexity = O(n)

# Optimal Approach: Rearrange the array in a single pass using separate pointers for positive and negative numbers
def rearrange_elements_optimal(arr, n):
    if n % 2 != 0:
        return "The size is invalid."
    else:
        ans = [None] * n  # Index error generated if the list is empty.
        positive_index = 0
        negative_index = 1
        # Traverse the array and place positive and negative numbers in alternate positions
        for i in range(n):
            if arr[i] > 0:
                ans[positive_index] = arr[i]
                positive_index += 2
            else:
                ans[negative_index] = arr[i]
                negative_index += 2     
        return ans
# Time Complexity = O(n)
# Space Complexity = O(n)

# User Input
size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# Uncomment to use the brute force approach
# result = rearrange_elements_brute(array, size)
# print(result)

# Use the optimal approach
result = rearrange_elements_optimal(array, size)
print(result)
