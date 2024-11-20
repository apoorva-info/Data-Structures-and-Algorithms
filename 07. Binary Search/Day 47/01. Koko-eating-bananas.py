# Goal: Find the minimum integer k such that Koko can eat all bananas within h hours.

import math

def func(arr,hours):
    total_hours = 0
    for i in range(len(arr)):
        total_hours += math.ceil(arr[i]/hours)
    return total_hours    
    
def koko_eating_bananas_brute(pile,h):
    max_num = max(pile)
    for i in range(1,max_num+1):
        required_time = func(pile,i)
        if required_time <= h:
            return i
# Time Complexity: O(max(arr)*n)
# Space Complexity: O(1)
        
def koko_eating_bananas_better(pile,h):
    high = max(pile)
    low = 1
    ans = float('inf')
    while low <= high:
        mid = (low + high)//2
        required_time = func(pile,mid)
        if required_time > h:
            low = mid + 1
        elif required_time <= h:
            ans = mid
            high = mid - 1
    return ans
# Time Complexity: O(log(max(arr))*n)
# Space Complexity: O(1)

# User Input
size = int(input("Enter the size of the array: "))
h = int(input("Enter the value of h: "))
pile = []
for i in range(size):
    element = int(input(f"Enter the no. of bananas in {i + 1} pile: "))
    pile.append(element)
print(pile)

# Function Call
result = koko_eating_bananas_brute(pile,h)
print(result)
result2 = koko_eating_bananas_better(pile,h)
print(result2)