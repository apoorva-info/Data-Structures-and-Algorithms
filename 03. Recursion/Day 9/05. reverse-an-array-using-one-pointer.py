# Recursive function to reverse an array by swapping elements
# Example:
# Input:
# Enter the size of the array: 5
# Enter the element for array[1]: 1
# Enter the element for array[2]: 7
# Enter the element for array[3]: 2
# Enter the element for array[4]: 9
# Enter the element for array[5]: 2
# Output:
# Original array:  [1, 7, 2, 9, 2]
# Reverse array:  [2, 9, 2, 7, 1]

def reverse_an_array(array, i=0):
    if i >= ((len(array) - i - 1) / 2) + 1: # Base Case
        return
    else:
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]
        reverse_an_array(array, i + 1)

# Prompt the user to enter the size of the array
size = int(input("Enter the size of the array: "))
array = []

# Loop to take array elements as input from the user
for i in range(size):
    element = input(f"Enter the element of array[{i+1}]: ")
    array.append(element)

# Print the original array
print("Original array: ", array)

# Call the function to reverse the array
reverse_an_array(array, i=0)

# Print the reversed array
print("Reverse array: ", array)

# Time Complexity = O(n)
