# Goal: Given a sorted array of distinct values and target, search for the index of the target value in an array.
# If the value is present in an array, return the index and if not, determine the index where it should be inserted in the array
# while maintaining the sorted order.

def search_insert_position(arr,n,target):
    low = 0 
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high)//2
        if arr[mid] >= target:
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    return ans
# Time Complexity = O(n)
# Space Complexity = O(1)


# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
x = int(input("Enter the value of the target: "))

# Function Call
result = search_insert_position(array,size,x)
print(result)