def max_sub_array_sum_brute(arr,n):
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum = sum + arr[k]
            max_sum = max(sum,max_sum)
    return max_sum
# Time Complexity = O(n^3)
# Space Complexity = O(1)



def max_sub_array_sum_better(arr,n):
    max_sum = float('-inf')
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum = sum + arr[j]
            max_sum = max(sum,max_sum)
    return max_sum
# Time Complexity = O(n^2)
# Space Complexity = O(1)
            











size = int(input("Enter the size of the list: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)
print(array)

# result = max_sub_array_sum_brute(array,size)
# print(result)

result = max_sub_array_sum_better(array,size)
print(result)