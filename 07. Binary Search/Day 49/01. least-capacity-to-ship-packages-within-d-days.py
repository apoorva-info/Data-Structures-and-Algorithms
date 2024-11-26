# Goal: To find the least capacity to ship the packages within d days

# Brute Force Approach
def daysReq(arr,capacity):
    sum_of_loads = 0
    d = 1
    for i in arr:
        if (sum_of_loads + i) > capacity:
            d += 1
            sum_of_loads = i 
        else:
            sum_of_loads += i
    return d

def least_capacity_brute(arr,days):
    for capacity in range(max(arr),sum(arr)+1):
        days_required = daysReq(arr,capacity)
        if days_required <= days:
            return capacity
# Time Complexity: O(n*(sum(arr)-max(arr)+1))
# Space Complexity: O(1)

# Better Approach
def least_capacity_better(arr,days):
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high)//2
        if daysReq(arr,mid) <= days:
            high = mid - 1
        else:
            low = mid + 1
    return low
    




        

# User Input
days = int(input("Enter the total number of days: "))
weights = []
n = int(input("Enter the number of items: "))
for i in range(n):
    element = int(input(f"Enter the weight of the package at {i+1} position: "))
    weights.append(element)
print(weights)

# Function Call
# result = least_capacity_brute(weights,days)
# print(result)
result = least_capacity_better(weights,days)
print(result)