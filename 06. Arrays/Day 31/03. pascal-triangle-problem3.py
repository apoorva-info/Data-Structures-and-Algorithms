# Problem 3
# Goal : To print the pascal triangle.

# Using the approach used to solve problem 1.
def nCr(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return int(res)
# Time Complexity = O(r)

def pascalTriangle_brute(r):
    ans = []
    for i in range(r):
        temp = []
        for c in range(i+1):
            temp.append(nCr(i,c))
        ans.append(temp)
    return ans
# Time Complexity ~ O(n^3)
# Space Complexity = O(n)
            
# Using the approach stated in problem 2.
def pascalTriangle_better(r):
    ans = []
    for row in range(1,r+1):
        temp = []
        previous_result = 1
        temp.append(previous_result)
        for c in range(1,row):
            previous_result = (row - c) * previous_result
            previous_result = previous_result // c
            temp.append(previous_result)
        ans.append(temp)
    return ans
# Time Complexity ~ O(n^2)
# Space Complexity = O(n)

row = int(input("Enter the number of rows: "))

# result = pascalTriangle_brute(row)
# print(result)

result = pascalTriangle_better(row)
print(result)