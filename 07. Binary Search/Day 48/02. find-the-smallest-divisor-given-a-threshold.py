# Goal: To find the smallest divisor given a threshold value.

# Brute Force Approach
import math
def smallest_divisor_brute(lst,size,limit):
    ans = float('inf')
    for divisor in range(1,max(lst)+1):
        sum_of_ceil_values = 0
        for i in range(size):
            ceil_value = math.ceil(lst[i]/divisor)
            sum_of_ceil_values = sum_of_ceil_values + ceil_value
        if sum_of_ceil_values <= limit:
            ans = min(ans,divisor)
    return ans
# Time Complexity: O(n * max(lst))
# Space Complexity: O(1)

# Better Approach
def sum_of_values(lst,mid):
    sum_of_values = 0
    for i in lst:
        ceil_value = math.ceil(i/mid)
        sum_of_values = sum_of_values + ceil_value
    return sum_of_values

def smallest_divisor_better(lst,size,limit):
    low = 1
    high = max(lst)
    while low <= high:
        mid = (low + high)//2
        if sum_of_values(lst,mid) <= limit:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

        
# User Input
size = int(input("Enter the size of the array: "))
lst = []
for i in range(size):
    element = int(input(f"Enter the {i+1}th element: "))
    lst.append(element)
print(lst)
threshold = int(input("Enter the threshold value: "))

# Function Call
# result = smallest_divisor_brute(lst,size,threshold)
# print(result)
result = smallest_divisor_better(lst,size,threshold)
print(result)