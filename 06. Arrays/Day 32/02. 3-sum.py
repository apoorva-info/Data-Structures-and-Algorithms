
# Brute Force Approach
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
# Time Complexity = O(n^3)
# Space Complexity = O(n)

# Better Approach
def three_sum_better(arr,n):
    ans = set()
    for i in range(n):
        hash_set = set()
        for j in range(i+1,n):
            k = - (arr[i] + arr[j])
            if k in hash_set:
                temp = [arr[i],arr[j],k]  
                temp.sort()
                ans.add(tuple(temp))
            hash_set.add(arr[j])
        
    ans = list(ans)     
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
# result = three_sum_brute(lst,n)
# print(result)
result = three_sum_better(lst,n)
print(result)