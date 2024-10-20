# Goal: Find all unique triplets in the array that sum up to zero.
# Example: 
# Input: [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]

# Brute Force Approach
def three_sum_brute(arr, n):
    ans = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp = sorted(temp)  # Sort to avoid duplicates
                    ans.add(tuple(temp))  # Convert to tuple for set storage
    return ans

# Time Complexity = O(n^3)
# Space Complexity = O(n)

# Better Approach
def three_sum_better(arr, n):
    ans = set()
    for i in range(n):
        hash_set = set()
        for j in range(i+1, n):
            k = - (arr[i] + arr[j])  # Calculate the required third number
            if k in hash_set:
                temp = [arr[i], arr[j], k]
                temp.sort()  
                ans.add(tuple(temp))  
            hash_set.add(arr[j])
    ans = list(ans)
    return ans

# Time Complexity = O(n^2 log m) m--> size of set
# Space Complexity = O(n)

# Optimal Approach
def three_sum_optimal(arr, n):
    arr = sorted(arr)  
    ans = []
    for i in range(n):
        # Skip duplicates for i
        if i > 0 and arr[i] == arr[i-1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                temp = {arr[i], arr[j], arr[k]}
                ans.append(temp)
                j += 1
                k -= 1
                # Skip duplicates for j and k
                while j < k and arr[j] == arr[j-1]:
                    j += 1
                while j < k and arr[k] == arr[k+1]:
                    k -= 1
    return ans

# Time Complexity = O(n log n) + O(n^2)
# Space Complexity = O(number of unique triplets)

# User Input
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
print(lst)

# Uncomment the desired function call
# result = three_sum_brute(lst, n)
# result = three_sum_better(lst, n)
result = three_sum_optimal(lst, n)
print(result)