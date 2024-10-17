# This code implements the Selection Sort algorithm to sort an array in ascending order.
# Selection Sort works by repeatedly finding the minimum element from the unsorted part of the array
# and swapping it with the first element of the unsorted part.

# Example:
# Input:
# Enter the size of the array: 5
# Enter the element at array[0]: 64
# Enter the element at array[1]: 25
# Enter the element at array[2]: 12
# Enter the element at array[3]: 22
# Enter the element at array[4]: 11
# Output:
# Sorted Array: [11, 12, 22, 25, 64]

# Selection Sort Algorithm
def selection_sort(array):
    for i in range(len(array)):
        min_value_index = i 
        # Finding the minimum element in the unsorted part of the array
        for j in range(i + 1, len(array)): 
            if array[j] < array[min_value_index]:
                min_value_index = j  
        # Swapping
        array[i], array[min_value_index] = array[min_value_index], array[i]

# User Input
size = int(input("Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Function Call
selection_sort(array)
# Print the sorted array
print(f"Sorted Array: {array}")

# Time Complexity = O(n^2) ---> (Best Case , Average Case , Worst Case)
