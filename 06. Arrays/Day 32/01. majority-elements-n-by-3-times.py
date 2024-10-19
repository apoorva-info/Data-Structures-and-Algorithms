def majority_elements_brute(arr,n):
    ans = []
    for i in range(n):
        if ans == [] or ans[0] != arr[i]:
            count = 0
            for j in range(n):
                if arr[i] == arr[j]:
                        count = count + 1
            if count > (n//3):
                ans.append(arr[i])
            if len(ans) == 2:
                break
    return ans
# Time Complexity = O(n^2)
# Space Complexity = O(n)


# User Input
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
print(lst)

result = majority_elements_brute(lst,n)
print(result)