# Function to find the frequency of a given number 'num' in an array
# Example:
# Input:
# Enter the size of the array: 5
# Enter the element at array[0]: 1
# Enter the element at array[1]: 2
# Enter the element at array[2]: 1
# Enter the element at array[3]: 3
# Enter the element at array[4]: 1
# Enter the number whose frequency is to be checked: 1
# Output:
# The frequency of array element 1 is 3.

def frequency_of_array_element(array, num):
    count = 0
    for i in range(len(array)):
        if array[i] == num: # If the current element matches 'num', increment the counter
            count = count + 1
    return count # Return the final count of 'num' in the array

# Prompt the user to enter the size of the array
size = int(input("Enter the size of array: "))
array = []

# Loop to take array elements as input from the user
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Prompt the user to enter the number whose frequency is to be checked
num = int(input("Enter the number whose frequency is to be checked: "))

# Call the function to find the frequency of the number in the array
result = frequency_of_array_element(array, num)

# Print the frequency of the given number
print(f"The frequency of array element {num} is {result}.")
