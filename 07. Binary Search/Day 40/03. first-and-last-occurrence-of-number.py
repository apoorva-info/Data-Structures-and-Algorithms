# Gaol: Find the first and last occurrence of a given number in a sorted array.
# Example:
# Input:
# Enter the size of the sorted array: 5
# Enter the element at array[0]: 1
# Enter the element at array[1]: 2
# Enter the element at array[2]: 2
# Enter the element at array[3]: 3
# Enter the element at array[4]: 5
# Enter the value of the target: 2
# Output:
# Floor Value:  (1, 2)

# Brute Force Approach
def first_and_last_occurrence_brute(arr,n,x):
    first = -1
    last = -1
    for i in range(n):
        if arr[i] == x:
            if first == -1:
                first = i
            last = i
    return first,last





# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
x = int(input("Enter the value of the target: "))

# Function Call
floor_value_result = first_and_last_occurrence_brute(array,size,x)
print("Floor Value: ", floor_value_result)