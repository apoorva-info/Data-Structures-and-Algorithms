from array import array
def left_rotate_by_d_places(array,n):
    temp = array[0]
    for i in range(len(array)-n):
        array[i] = array[i+n]
    array[len(array)-n] = temp
    print(array)

    






user_array = array('i',[])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)
d = int(input("Enter the number to which your array should be rotated: "))
print(user_array)

left_rotate_by_d_places(user_array,d)