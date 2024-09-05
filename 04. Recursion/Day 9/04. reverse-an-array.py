# Function to reverse an array using Recursion
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

def reverse_array(array, left, right):
    if left >= right: # Base case: if the left index is greater than or equal to the right index, stop the recursion
        return 
    else:
        swap(array, left, right) # Swap the elements at the left and right indices
        reverse_array(array, left + 1, right - 1) # Recursive call to reverse the next pair of elements

# Function to swap the elements at the specified indices
def swap(array, left, right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp

# Prompt the user to enter the size of the array
array = []
size = int(input("Enter the size of the array: "))
for i in range(size): 
    element = int(input(f"Enter the element for array[{i+1}]: "))
    array.append(element)

# Print the original array
print("Original array: ", array)

# Call the function to reverse the array
reverse_array(array, 0, len(array) - 1)

# Print the reversed array
print("Reverse array: ", array)

#  Time Complexity = O(n)
