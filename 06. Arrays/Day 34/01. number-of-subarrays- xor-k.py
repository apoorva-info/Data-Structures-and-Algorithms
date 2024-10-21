def count_subarrays_with_xor_k_brute(arr,n,k):
    count = 0
    for i in range(n):
        for j in range(i,n):
            XOR = 0
            for l in range(i,j+1):
                XOR = XOR ^ arr[l]
            if XOR == k:
                count += 1
    return count
# Time Complexity = O(n^3)
# Space Complexity = O(1)


# User Input
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
k = int(input("Enter the value of k: "))
print(lst)

result = count_subarrays_with_xor_k_brute(lst,n,k)
print(result)