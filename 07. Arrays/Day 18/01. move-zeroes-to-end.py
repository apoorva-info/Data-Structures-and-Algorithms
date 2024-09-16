from array import array

# Brute Force Approach
def shifting_zeroes(array,n):
    temp = []
    for i in range(n):
     if array[i] != 0:
       temp.append(array[i])

    for i in range(len(temp)):
       array[i] = temp[i]
    for i in range(len(temp),n):
      array[i] = 0
    
    print(array)
        
    



            



# User Input
user_array = array('i',[])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)
print(user_array)
shifting_zeroes(user_array,size)