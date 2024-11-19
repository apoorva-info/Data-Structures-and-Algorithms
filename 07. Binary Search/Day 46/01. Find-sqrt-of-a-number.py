# Goal: Find the sqrt of an integer.

# Brute Force Approach
def find_sqrt_brute(n):
    i = 1
    ans = 0
    for i in range(1,n+1):
        if i * i <= n:
            ans = i
        else:
            break
    return ans
# Time Complexity: O(n)
# Space Complexity: O(1)

# Binary Search Approach
def find_sqrt_better(n):
    low = 1
    high = n
    ans = 0
    while high >= low:
        mid = (low + high)//2
        if mid * mid > n:
            high = mid - 1
        else:
            ans = mid
            low = mid + 1
    return ans
# Time Complexity: O(log n)
# Space Complexity: O(1)

#  User Input
x = int(input("Enter the value of the integer: "))

# Function Call
# result = find_sqrt_brute(x)
# print(result)

result = find_sqrt_better(x)
print(result)