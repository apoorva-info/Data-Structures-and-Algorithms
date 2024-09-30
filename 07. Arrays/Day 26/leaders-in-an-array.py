# Brute Force Approach
def leaders_in_an_array_brute(arr,n):
    temp = []
    for i in range(n):
        for j in range(i+1 , n):
            if arr[j] > arr[i]:
                break
        else:
            temp.append(arr[i])
    return temp










size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

result = leaders_in_an_array_brute(array,size)
print(result)