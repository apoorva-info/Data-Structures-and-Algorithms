# Problem 2:
# Print any nth row of the pascal triangle.
# In the previous problem, the element at any place in the pascal triangle was calculated. Use this approach to find the nth row.

def nCr(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res

def find_nth_row(r):
    for c in range(1,r+1):
        print(nCr(r-1,c-1))

# Time complexity = O(n*r)
# Space Complexity = O(1)

# A better approach
def pascalTriangle(r):
    previous_result = 1
    for c in range(1,r):
        previous_result = (previous_result * (r-c))//c
        print(previous_result)

row = int(input("Enter the number of row: "))

# result = find_nth_row(row)
result = pascalTriangle(row)

