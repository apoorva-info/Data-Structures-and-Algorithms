from array import array

# Brute Force Approach: Uses a set to remove duplicates.
def remove_duplicates_using_brute_approach(sorted_array):
    user_set = set(sorted_array)  
    user_set = list(user_set)  
    sorted_array = array('i', user_set)  
    return user_set, len(sorted_array)  
# Time Complexity = O(n) 
# Space Complexity = O(n) 
# This approach does not maintain the original order of the elements.


# Better Approach: Maintains the order of elements while removing duplicates.
def remove_duplicates_using_better_approach(sorted_array):
    sorted_list = list(sorted_array)  
    temp = [] 
    for i in range(len(sorted_list)):
        if i == 0 or sorted_list[i - 1] != sorted_list[i]:
            temp.append(sorted_list[i])
    sorted_list = temp
    print(sorted_list)
# Time Complexity = O(n) 
# Space Complexity = O(n) 
# This approach maintains the order of the original sorted array.


# Optimal Approach: Removes duplicates in place without using extra space.
def remove_duplicates_using_optimal_approach(array):
    i = 0  
    for j in range(1, len(array)):
        if array[i] != array[j]:  
            array[i + 1] = array[j]  
            i += 1 
    return array[:i + 1], i + 1  
# Time Complexity = O(n) 
# Space Complexity = O(1)


# User Input
user_array = array('i', [])  # Initialize an empty integer array
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)
user_array = sorted(user_array)  # Sort the array to ensure it is in ascending order

# Uncomment one of the following lines to test different approaches:
# result = remove_duplicates_using_brute_approach(user_array)  # Brute Force Approach
# result = remove_duplicates_using_better_approach(user_array)  # Better Approach
result = remove_duplicates_using_optimal_approach(user_array)  # Optimal Approach

# Print the result
print(result)
