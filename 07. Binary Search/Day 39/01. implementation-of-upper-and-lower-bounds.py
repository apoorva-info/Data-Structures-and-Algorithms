# Goal: To find the lower bound of the given number.
# Lower Bound: The smallest index such that arr[i] >= x
def lower_bound(arr,n,x):
    low = 0
    high = n - 1
    ans = n 
    while low <= high:
        mid = (low + high)//2 
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
            
# User Input
size = int(input(f"Enter the size of the sorted array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
x = int(input("Enter the value whose lower bound is to found: "))

result = lower_bound(array,size,x)
print(result)