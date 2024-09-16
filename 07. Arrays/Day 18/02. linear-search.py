# Linear Search: Searches for a specified number in the array
# Example:
# Input:
# Enter the size of the array: 5
# Enter the element at array[0]: 10
# Enter the element at array[1]: 20
# Enter the element at array[2]: 30
# Enter the element at array[3]: 40
# Enter the element at array[4]: 50
# Enter the number that you want to search: 30
# Output:
# 2 (index of the searched element)
 
from array import array

def linear_search(array):
    num = int(input("Enter the number that you want to search: "))
    for i in range(len(array)):
        if array[i] == num:
            return i  
    else:
        return -1  
# Time Complexity = O(n)
# Space Complexity = O(1)

# User Input
user_array = array('i', [])  
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)

# Call the linear search function and print the result
print(linear_search(user_array))
