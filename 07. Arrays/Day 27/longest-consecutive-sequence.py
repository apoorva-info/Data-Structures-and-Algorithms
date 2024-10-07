def ls(arr,a):
    for i in arr:
        if a == i:
            return True
    return False

def longest_consecutive_brute(arr,n):
    longest = 1
    for i in range(n):
        x = arr[i]
        count = 1
        while (ls(arr,x+1) == True):
            x = x+1
            count = count + 1
        longest = max(count,longest)
    return longest

# Time Complexity = O(n^2)
# Space Complexity = O(1)








size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

result = longest_consecutive_brute(array,size)
print(result)