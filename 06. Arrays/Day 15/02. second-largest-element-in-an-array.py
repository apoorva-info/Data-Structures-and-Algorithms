from array import array 

# Brute Force Approach
def second_largest_brute(array):
    array = sorted(array)
    largest = len(array) - 1
    for i in range(len(array) - 2, -1, -1):
        if array[i] != array[largest]:
            second_largest = array[i]
            print(f"The second largest element in the array using Brute Force Approach is {second_largest}.")
            return
    print("No second largest element was found.")
# Time Complexity = O(nlogn)
# Space Complexity = O(n)

# Better Solution
def second_largest_better(array):
    if len(array) < 2:
        print("No second largest element was found.")
        return
    largest = float('-inf')  # -inf --> Negative infinity --> Special floating point value --> Smaller than any other number
    for i in range(len(array)):
        if array[i] > largest:
            largest = array[i]
    second_largest = float('-inf')
    for i in range(len(array)):
        if array[i] > second_largest and array[i] != largest:
            second_largest = array[i]
    if second_largest == float('-inf'):
        print("No second largest element is found.")
    else:
        print(f"The second largest element in the array using better approach is {second_largest}.")
# Time Complexity = O(2n) -> Simplifies to O(n)
# Space Complexity = O(1)

# Optimal Approach
def second_largest_optimal(array):
    if len(array) < 2:
        print("The second largest number is not found.")
        return
    if array[0] > array[1]:
        largest = array[0]
        second_largest = array[1]
    else:
        largest = array[1]
        second_largest = array[0]
    for i in range(2, len(array)):
        if array[i] > largest:
            second_largest = largest
            largest = array[i]
        elif array[i] > second_largest and array[i] != largest:
            second_largest = array[i]
            
    print(f"The largest element is {largest} and the second largest element is {second_largest}.")
# Time Complexity = O(n)
# Space Complexity = O(1)

# User Input
user_array = array('i', [])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)

# Uncomment the approach you want to test
# second_largest_brute(user_array)
# second_largest_better(user_array)
second_largest_optimal(user_array)
