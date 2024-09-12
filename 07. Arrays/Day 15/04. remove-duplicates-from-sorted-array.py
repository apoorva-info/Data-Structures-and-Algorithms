from array import array
# Brute Force Approach
def remove_duplicates_using_sets(sorted_array):
    user_set = set(sorted_array)
    user_set = list(user_set)
    sorted_array = array('i',user_set)
    
    return user_set,len(sorted_array)
# Time Complexity = O(n)
# Space Complexity = O(n)




# Better Approach
def remove_duplicates(sorted_array):
    sorted_list = list(sorted_array)
    temp = []
    for i in range(len(sorted_list)):
        if i == 0 or sorted_list[i-1] != sorted_list[i]:
            temp.append(sorted_list[i])
    sorted_list = temp     
    print(sorted_list)
# Time Complexity = O(n)
# Space Complexity = O(n)






user_array = array('i',[])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)

# remove_duplicates(user_array)
result = remove_duplicates_using_sets(user_array)
print(result)