# This code implements the Quick Sort algorithm to sort an array in ascending order.
# Quick Sort is a divide-and-conquer algorithm that selects a pivot element and partitions the array around the pivot.
# The array is then recursively sorted on either side of the pivot.

# Example:
# Input:
# Enter the size of the array: 6
# Enter the element at array[0]: 10
# Enter the element at array[1]: 7
# Enter the element at array[2]: 8
# Enter the element at array[3]: 9
# Enter the element at array[4]: 1
# Enter the element at array[5]: 5
# Output:
# Original Array: [10, 7, 8, 9, 1, 5]
# Sorted Array: [1, 5, 7, 8, 9, 10]


def partition(array, low, high):
    pivot = array[low] # Select the first element as the pivot
    i = low
    j = high
    
    while i < j:
        while array[i] <= pivot and i <= high - 1:
            i += 1
        while array[j] > pivot and j >= low + 1:
            j -= 1
        if i < j: # Swap elements if indices 'i' and 'j' have not crossed
            array[i], array[j] = array[j], array[i]

    array[low], array[j] = array[j], array[low] # Place the pivot in its correct position
    return j  # Return the partition index

def quick_sort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)  # Get the partition index
        quick_sort(array, low, partition_index - 1)    # Sort the left sub-array
        quick_sort(array, partition_index + 1, high)   # Sort the right sub-array

# Prompt the user to enter the size of the array
num = int(input("Enter the size of the array: "))
array = []
for i in range(num):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Print the original array
print(f"Original Array: {array}")

# Call the Quick Sort function to sort the array
quick_sort(array, 0, num - 1)

# Print the sorted array
print(f"Sorted Array: {array}")

# Time Complexity = O(n*log(n)) in the average and best case.
# Space Complexity = O(log(n)) due to recursion stack space in the average and best case.
# Worst Case Time Complexity = O(n^2) when the pivot elements are the smallest or largest element repeatedly.
