# Goal: Merge overlapping intervals in a given list of intervals.
# This problem aims to combine intervals that overlap with each other into a single interval.

# Example:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Intervals [1,3] and [2,6] overlap, so they are merged into [1,6].

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
        ans.append([start,end])

    return ans

# Time Complexity = O(n log n) + O(2n)
# Space Complexity = O(n)

# Optimal Approach
def overlapping_intervals_optimal(arr):
    arr = sorted(arr)
    n = len(arr)
    ans = []
    for i in range(n):
        if ans == [] or arr[i][0] > ans[len(ans)-1][1]:
            ans.append(arr[i])
        else:
            ans[len(ans)-1][1] = max(ans[len(ans)-1][1],arr[i][1])
    return ans

# Time Complexity = O(n log n) 
# Space Complexity = O(n)

# User Input   
intervals = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]

# result = overlapping_intervals_brute(intervals)
# print(result)

result = overlapping_intervals_optimal(intervals)
print(result)