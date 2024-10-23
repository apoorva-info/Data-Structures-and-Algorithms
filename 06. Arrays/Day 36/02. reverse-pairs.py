def reverse_pairs_brute(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > 2 * arr[j]:
                count += 1
    return count


size = int(input(f"Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

result = reverse_pairs_brute(array,size)
print(result)