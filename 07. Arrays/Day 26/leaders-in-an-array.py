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
# Time Complexity = O(n^2)
# Space Complexity = O(n)

# Optimal Approach
def leaders_in_an_array_optimal(arr,n):
    temp = []
    max_element = float('-inf')
    for i in range(n-1,-1,-1):
        if arr[i] > max_element:
            max_element = arr[i]
            temp.append(arr[i])
    return temp

        
        
        
            
     










size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# result = leaders_in_an_array_brute(array,size)
# print(result)
result = leaders_in_an_array_optimal(array,size)
print(result)