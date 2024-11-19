# Goal: Find the n th of an integer.

# Brute Force Approach
def f(i,n):
    return i ** n

def find_sqrt_brute(num,n):
    i = 1
    for i in range(1,num+1):
        if f(i,n)  == num:
            return i
        elif f(i,n) > num:
            break
    return -1
# Time Complexity: O(m*n)
# Space Complexity: O(1)

# Binary Search Approach
def find_sqrt_better(num,n):
    low = 1
    high = num
    while high >= low:
        mid = (low + high)//2
        if f(mid,n) > num:
            high = mid - 1
        elif f(mid,n) < num:
            low = mid + 1
        else:
            return mid
    return -1

# Time Complexity: O((log n)*(log m))
# Space Complexity: O(1)

#  User Input
num = int(input("Enter the value of the integer: "))
n = int(input("Enter the value of the nth root: "))
# Function Call
# result = find_sqrt_brute(num,n)
# print(result)
result = find_sqrt_better(num,n)
print(result)