from array import array
def sort_brute(arr):
    arr = sorted(arr)
    return arr
# Time Complexity = O(n log n)
# Space Complexity = O(n)

# Better Approach
def sort_better(arr):
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count0 += 1
        elif arr[i] == 1:
            count1 += 1
        else:
            count2 += 1
    print(count0)
    print(count1)
    print(count2)
    
    for i in range(count0):
        arr[i] = 0
    for i in range(count0,count1+count0):
        arr[i] = 1
    for i in range(count1+count0,count2+count0+count1):
        arr[i] = 2
    return arr
# Time Complexity = O(n)
# Space Complexity = O(1)






user_array = array('i', [])
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    user_array.append(element)
print(user_array)

# result = sort_brute(user_array)
# print(result)

result = sort_better(user_array)
print(result)