
def overlapping_intervals_brute(arr):
    ans = []
    arr = sorted(arr)
    n = len(arr)
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]
        if ans != [] and end <= ans[len(ans)-1][1]:
            continue
        for j in range(i+1,n):
            if arr[j][0] <= end: 
                end = max(end , arr[j][1])
            else:
                break
        ans.append((start,end))


    return ans
    
intervals = [(1,3),(2,6),(8,9),(9,11),(8,10),(2,4),(15,18),(16,17)]
result = overlapping_intervals_brute(intervals)
print(result)