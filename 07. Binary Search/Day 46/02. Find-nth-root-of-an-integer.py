# Goal: Find the n th of an integer.

# Brute Force Approach
def f(i,n):
    return i ** n

def find_sqrt_brute(num,n):
    i = 1
    ans = 0
    for i in range(1,num+1):
        if f(i,n)  <= num:
            ans = i
        else:
            break
    return ans
# Time Complexity: O(n)
# Space Complexity: O(1)


#  User Input
num = int(input("Enter the value of the integer: "))
n = int(input("Enter the value of the nth root: "))
# Function Call
result = find_sqrt_brute(num,n)
print(result)
