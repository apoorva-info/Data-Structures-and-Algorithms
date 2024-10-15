# Three types of problems:
# 1. Given rows and columns, tell the element at that place.
# 2. Print any nth row of the pascal triangle.
# 3. Given N, print the pascal triangle. 


#  Problem 1:
# Use combinations to solve this problem
def fact(a):
    if a == 0:
        return 1
    else:
        a = a * fact(a-1)
        return a

def find_element(r,c):
    num = fact(r-1)
    d1 = fact(r - c)
    d2 = fact(c-1)
    element = num // (d1 * d2)
    return element

# A better approach 
def nCr(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res
# Time Complexity = O(r)
# Space Complexity = O(1)

def pascalTriangle(r,c):
    element = nCr(r-1,c-1)
    return element

row = int(input("Enter the number of row: "))
column = int(input("Enter the number of column: "))

result1 = find_element(row,column)
print(result1)

result2 = pascalTriangle(row,column)
print(result2)


