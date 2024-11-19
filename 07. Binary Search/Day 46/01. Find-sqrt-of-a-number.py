# Goal: Find the sqrt of an integer.

# Brute Force Approach
def find_sqrt_brute(x):
    i = 1
    ans = 0
    for i in range(1,x+1):
        if i * i <= x:
            ans = i
        else:
            break
    return ans




#  User Input
n = int(input("Enter the value of the integer: "))

# Function Call
result = find_sqrt_brute(n)
print(result)