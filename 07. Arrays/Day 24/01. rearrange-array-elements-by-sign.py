def rearrange_elements_brute(arr,n):
    if n % 2 != 0:
        return "The size should be even."
    else:
        positive_arr = []
        negative_arr = []
        for i in range(n):
            if arr[i] > 0:
                positive_arr.append(arr[i])
            else:
                negative_arr.append(arr[i])
        for i in range(0,n//2,2):
                arr[i] = positive_arr[i]
        for i in range(1,n//2,2):
                arr[i] = negative_arr[i]
        return arr
                

                
            
        






size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

result = rearrange_elements_brute(array,size)
print(result)


