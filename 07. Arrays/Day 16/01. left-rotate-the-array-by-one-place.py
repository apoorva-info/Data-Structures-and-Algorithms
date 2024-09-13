from array import array
def left_rotate(array):
    temp = array[0]
    for i in range(len(array)-1):
        array[i] = array[i+1]
    array[-1] = temp
    print(f"Rotated Array: {array}")





user_array = array('i' , [])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)
print(f"Original Array: {user_array}")
left_rotate(user_array)