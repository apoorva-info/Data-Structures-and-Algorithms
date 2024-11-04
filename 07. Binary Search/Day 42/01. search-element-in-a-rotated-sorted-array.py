# Goal: Given a rotated sorted array with duplicates and a target value, return True if target value is present in the array 
# else return False.

# Brute Force Approach
def search_element_in_rotated_sorted_array_brute(arr,x):
    for element in arr:
        if element == x:
            return True
    return False

# Time Complexity = O(n) ---> Loop runs n times 
# Space Complexity = O(1) ---> No extra space is being used 



# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
x = int(input("Enter the value of the target: "))

result = search_element_in_rotated_sorted_array_brute(array,x)
print(result)