from collections import defaultdict
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
# Space Complexity = O(1)

def majority_elements_better(arr,n):
    hash_lst = defaultdict(int)
    minimum_value = n//3
    ans = []
    for i in range(n):
        hash_lst[arr[i]] += 1
        if hash_lst[arr[i]] == minimum_value:
            ans.append(arr[i])
    return ans
# Time Complexity = O(n)
# Space Complexity = O(n)




# User Input
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
print(lst)

# result = majority_elements_brute(lst,n)
# print(result)
result = majority_elements_better(lst,n)
print(result)