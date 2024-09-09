# This code implements the Insertion Sort algorithm to sort an array in ascending order.
# Insertion Sort builds the sorted array one element at a time by repeatedly picking the next element 
# and inserting it into its correct position among the already sorted elements.

# Example:
# Input:
# Enter the size of the array: 5
# Enter the element at array[0]: 12
# Enter the element at array[1]: 11
# Enter the element at array[2]: 13
# Enter the element at array[3]: 5
# Enter the element at array[4]: 6
# Output:
# Sorted Array: [5, 6, 11, 12, 13]

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]: # Compare the current element with the previous elements
            array[j], array[j - 1] = array[j - 1], array[j] # Swap
            j -= 1  


# Prompt the user to enter the size of the array
size = int(input("Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Call the Insertion Sort function to sort the array
insertion_sort(array)

# Print the sorted array
print(f"Sorted Array: {array}")

# Time Complexity:
# Worst Case: O(n²) - occurs when the array is sorted in reverse order.
# Average Case: O(n²) - occurs when the elements are in random order.
# Best Case: O(n) - occurs when the array is already sorted.
