# Function to find the maximum consecutive ones in an array.
# Input:
# Enter the size of the array: 6
# Enter either 1 or 0 at array[0]: 1
# Enter either 1 or 0 at array[1]: 1
# Enter either 1 or 0 at array[2]: 1
# Enter either 1 or 0 at array[3]: 0
# Enter either 1 or 0 at array[4]: 1
# Enter either 1 or 0 at array[5]: 1
# Output:
# 3

from array import array
def maximum_consecutive_ones(arr):
    count = 0
    maximum = 0
    for i in arr:
        if i == 1:
            count += 1
            maximum = max(maximum,count)
        else:
            count = 0
    
    return maximum
# Time Complexity = O(n)
# Space Complexity = O(1)

# User Input 
user_array = array('i',[])
n = int(input("Enter the size of the array: "))
for i in range(n):
    element = int(input(f"Enter either 1 or 0 at array[{i}]: "))
    user_array.append(element)

# Function Call
result = maximum_consecutive_ones(user_array)
print(result)