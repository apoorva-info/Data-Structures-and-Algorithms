# Brute Force Approach
def rearrange_elements_brute(arr,n):
    if n % 2 != 0:
        return "The size is invalid."
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
# Time Complexity = O(n)
# Space Complexity = O(n)

# Optimal Approach
def rearrange_elements_optimal(arr,n):
    if n % 2 != 0:
        return "The size is invalid."
    else:
        ans = [None] * n # The list should not be empty.
        positive_index = 0
        negative_index = 1
        for i in range(n):
            if arr[i] > 0:
                ans[positive_index] = arr[i]
                positive_index += 2
            else:
                ans[negative_index] = arr[i] 
                negative_index += 2     
        
        return ans
# Time Complexity = O(n)
# Space Complexity = O(n)
        
     

                
            
        






size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# result = rearrange_elements_brute(array,size)
# print(result)

result = rearrange_elements_optimal(array,size)
print(result)

