# Function to find the intersection of two sorted arrays
# Example:
# Input:
# Enter the size of the first list: 5
# Enter the element at first_list[0]: 4
# Enter the element at first_list[1]: 4
# Enter the element at first_list[2]: 3
# Enter the element at first_list[3]: 2
# Enter the element at first_list[4]: 7
# Enter the size of the second list: 6
# Enter the element at second_list[0]: 4
# Enter the element at second_list[1]: 4
# Enter the element at second_list[2]: 2
# Enter the element at second_list[3]: 8
# Enter the element at second_list[4]: 5
# Enter the element at second_list[5]: 3
# Output: 
# [2, 3, 4, 4, 7]
# [2, 3, 4, 4, 5, 8]
# Brute Solution = [2, 3, 4, 4]
# Optimal Solution = [2, 3, 4, 4]

# Brute Force Approach
def intersection(list1,list2):
    intersection_list = []
    temp = [0] * len(list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j] and temp[j] == 0:
                    intersection_list.append(list1[i])
                    temp[j] = 1
                    break
            if list2[j] > list1[i]:
                 break
    return intersection_list
# Time Complexity = O(n1 * n2)
# Space Complexity = O(n2)

# Optimal Approach
def intersection_optimal(list1,list2):
    answer = []
    j = 0
    i = 0 
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
              i += 1
        elif list2[j] < list1[i]:
             j += 1
        else:
             answer.append(list1[i])
             i += 1
             j += 1
    return answer
# Time Complexity = O(n1 + n2)
# Space Complexity = O(1)
              
          

# User Input 
first_list = []
first_size = int(input("Enter the size of the first list: "))
for i in range(first_size):
    element = int(input(f"Enter the element at first_list[{i}]: "))
    first_list.append(element)
first_list = sorted(first_list)

second_list = []
second_size = int(input("Enter the size of the second list: "))
for i in range(second_size):
    element = int(input(f"Enter the element at second_list[{i}]: "))
    second_list.append(element)
second_list = sorted(second_list)

print(first_list)
print(second_list)

# Function Call
brute_solution = intersection(first_list,second_list)
print(f"Brute Solution = {brute_solution}")
optimal_solution = intersection_optimal(first_list,second_list)
print(f"Optimal Solution = {optimal_solution}")