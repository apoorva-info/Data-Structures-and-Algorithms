# Goal: To find the least capacity to ship the packages within d days
def daysReq(arr,capacity):
    d = 1, sum_of_loads = 0
    for i in arr:
        if (sum_of_loads + i) > capacity:
            d += 1
            sum_of_loads = i 
        else:
            sum_of_loads += i
    return d

def least_capacity_brute(arr,n,days):
    for capacity in range(max(arr),sum(arr)+1):
        days_required = daysReq(arr,capacity)
        if days_required <= days:
            return days_required

            
    




        

# User Input
days = int(input("Enter the total number of days: "))
weights = []
n = int(input("Enter the number of items: "))
for i in range(n):
    element = int(input(f"Enter the weight of the package at {i+1} position: "))
    weights.append(element)
print(weights)

# Function Call
result = 
print(result)