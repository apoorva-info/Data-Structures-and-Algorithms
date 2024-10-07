
# Brute Force Approach
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

# Better Approach
def longest_consecutive_better(arr,n):
    arr = sorted(arr)
    longest = 1
    count = 0 
    last_smallest = float('-inf')
    for i in range(n):
        if arr[i] - 1 == last_smallest:
            count = count + 1
            last_smallest = arr[i]
        elif arr[i] != last_smallest:
            count = 1
            last_smallest = arr[i]
        longest = max(longest,count)
    return longest

# Time Complexity = O(n log n)
# Space Complexity = O(1)

# Optimal Approach
 
def longest_consecutive_optimal(arr,n):
    if n == 0:
        return 0 
    
    longest = 1
    arr = set(arr)

    for num in arr:
        if num - 1 not in arr:
            current_num = num
            count = 1
            while current_num + 1 in arr:
                count += 1
                current_num += 1
            longest = max(longest,count)
    return longest


    








size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# result = longest_consecutive_brute(array,size)
# print(result)

# result = longest_consecutive_better(array,size)
# print(result)

result = longest_consecutive_optimal(array,size)
print(result)