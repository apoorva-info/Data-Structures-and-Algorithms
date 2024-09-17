# Function to find the intersection of two sorted arrays
# Example:
# Input:
# Enter the size of the first list: 7
# Enter the element at first_list[0]: 3
# Enter the element at first_list[1]: 2
# Enter the element at first_list[2]: 1
# Enter the element at first_list[3]: 1
# Enter the element at first_list[4]: 4
# Enter the element at first_list[5]: 5
# Enter the element at first_list[6]: 3
# Enter the size of the second list: 4
# Enter the element at second_list[0]: 4
# Enter the element at second_list[1]: 1
# Enter the element at second_list[2]: 1
# Enter the element at second_list[3]: 2
# Output: 
# [1, 1, 2, 4]

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
    print(intersection_list)
# Time Complexity = O(n1 * n2)
# Space Complexity = O(n2)



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
intersection(first_list,second_list)