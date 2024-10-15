# Problem 3
# Goal : To print the pascal triangle.

def nCr(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return int(res)


def pascalTriangle(r):
    ans = []
    for i in range(r):
        temp = []
        for c in range(i+1):
            temp.append(nCr(i,c))
        ans.append(temp)
    return ans
            




row = int(input("Enter the number of rows: "))
result = pascalTriangle(row)
print(result)