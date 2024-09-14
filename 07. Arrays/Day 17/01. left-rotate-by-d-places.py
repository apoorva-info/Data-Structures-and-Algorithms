from array import array
# Brute Force Approach
def left_rotate_by_d_places_brute(array,k):
    temp = []
    i = 0
    for i in range(k):
            temp.append(array[i])
    for i in range(k,len(array)):
        array[i-k] = array[i]
    for i in range(k):
        array[len(array)-k+i] = temp[i]
    print(array)

    






user_array = array('i',[])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)
d = int(input("Enter the number to which your array should be rotated: "))
d = d % size
print(user_array)
left_rotate_by_d_places_brute(user_array,d)