# Brute Force Approach
def four_sum_brute(arr,n, target):
    ans = set()
    for i in range(n):
        temp = []
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        temp = [arr[i],arr[j],arr[k],arr[l]]
                        temp.sort()
                        ans.add(tuple(temp))
    return ans
# Time Complexity = O(n^4)
# Space Complexity = O(no. of quads)*2(in  which you store the answer and return)

# Better Approach
def four_sum_better(arr, n, target):
    ans = set()
    for i in range(n):
        for j in range(i+1,n):
            hash_set = set()
            for k in range(j+1,n):
                l = target - (arr[i] + arr[j] + arr[k])
                if l in hash_set:
                    temp = [arr[i],arr[j],arr[k],l]
                    temp.sort()
                    ans.add(tuple(temp))
                hash_set.add(arr[k])
    return ans
# Time Complexity = O(n^3)
# Space Complexity = O(no. of quads)*2(in  which you store the answer and return)
            


lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
target = int(input("Enter the value of the target: "))
print(lst)

# Uncomment the desired function call
# result = four_sum_brute(lst, n, target)
result = four_sum_better(lst, n, target)
# result = four_sum_optimal(lst, n)
print(result)