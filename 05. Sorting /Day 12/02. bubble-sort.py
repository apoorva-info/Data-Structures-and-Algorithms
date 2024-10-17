# This code implements the Bubble Sort algorithm to sort an array in ascending order.
# Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# This process continues until the array is sorted.

# Example:
# Input:
# Enter the size of the array: 5
# Enter the element at array[0]: 64
# Enter the element at array[1]: 34
# Enter the element at array[2]: 25
# Enter the element at array[3]: 12
# Enter the element at array[4]: 22
# Output:
# Sorted Array: [12, 22, 25, 34, 64]


def bubble_sort(array):
    for i in range(len(array)):
        swap = 0
        for j in range(0, len(array) - i - 1): # Inner loop to compare adjacent elements
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1] # Swap
                swap = 1
        if swap == 0:
            break
        # print("Swap") # ---> Number of times swapping was done

# Prompt the user to enter the size of the array
size = int(input("Enter the size of the array: "))
array_list = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array_list.append(element)

# Function Call
bubble_sort(array_list)

# Print the sorted array
print(f"Sorted Array: {array_list}")

# Time Complexity = O(n^2) ---> Worst Case & Average Case 
                    # O(n) ---> Best Case
