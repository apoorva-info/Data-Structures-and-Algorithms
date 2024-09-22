from array import array
# Brute Force Approach
def majority_element_brute(arr,n):
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
                if count > n//2:
                    return arr[i]
# Time Complexity = O(n^2)
# Space Complexity = O(1)

                

    






user_array = array('i', [])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)
print(user_array)

result = majority_element_brute(user_array,size)
print(result)