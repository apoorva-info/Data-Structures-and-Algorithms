def three_sum_brute(arr,n):
    ans = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i],arr[j],arr[k]]  
                    temp = sorted(temp)
                    ans.add(tuple(temp))
    return ans



# User Input
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
print(lst)
result = three_sum_brute(lst,n)
print(result)