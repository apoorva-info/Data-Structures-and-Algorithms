from array import array

def find_number(arr):
    xor = 0
    for i in arr:
        xor ^= i
    return xor



# User Input 
user_array = array('i',[])
n = int(input("Enter the size of the array: "))
for i in range(n):
    element = int(input(f"Enter either 1 or 0 at array[{i}]: "))
    user_array.append(element)

# Function Call
result = find_number(user_array)
print(result)