# Brute Approach
def rearrange_elements_brute(arr,k):
    positive_list = []
    negative_list = []
    for i in range(k):
        if arr[i] > 0:
            positive_list.append(arr[i])
        else:
            negative_list.append(arr[i])
    m = len(positive_list)
    n = len(negative_list)
    result = []
    min_len = min(m,n)
    for i in range(min_len):
        result.append(positive_list[i])
        result.append(negative_list[i])
    if m > n:
        result.extend(positive_list[min_len:])
    else:
        result.extend(negative_list[min_len:])
    for i in range(k):
        arr[i] = result[i]
    

   
    return arr
                

        
            



size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

result = rearrange_elements_brute(array, size)
print(result)

# result = rearrange_elements_optimal(array, size)
# print(result)