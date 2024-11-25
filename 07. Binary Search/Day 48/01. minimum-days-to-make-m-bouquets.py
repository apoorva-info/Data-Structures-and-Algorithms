# Goal: To find the minimum number of days to make m bouquets.

def minimum_days_brute(lst,size,k,m):
    if size < (m*k): # Base Case
        return -1
    else:
        for day in range(min(lst),max(lst)+1): # This loop will run from min(lst) to max(lst)
            count = 0
            temp = 0 # For counting number of bouquets
            for i in range(size): # This loop will run from 0 to size of the array
                if lst[i] <= day:
                    count += 1
                else:
                    temp += (count//k)
                    count = 0
            temp += (count//k) # To add the final bouquet
            if temp == m:
                return day
        return -1
# Time Complexity: O(n * (max(lst)- min(lst) + 1))
# Space Complexity: O(1)

def possible_condition(lst,size,mid,k):
    count = 0
    temp = 0
    for i in range(size):
        if lst[i] <= mid:
            count += 1 
        else:
            temp += (count//k)
            count = 0
    temp += (count//k)
    return temp
                    
            
def minimum_days_better(lst,size,k,m):
    if size < (m*k):
        return -1
    else:
        low = min(lst)
        high = max(lst)
        ans = 0
        while low <= high:
            mid = (low + high)//2
            if possible_condition(lst,size,mid,k) >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
# Time Complexity: O(n * log(max(lst)- min(lst) + 1))
# Space Complexity: O(1)

# User Input
k = int(input("Enter the number of flowers in a bouquet: ")) # Number of flowers in a bouquet
m = int(input("Enter the total number of bouquets: ")) # Total number of bouquets

size = int(input("Enter the size of the array: "))
lst = []
# Number of days taken by a flower to bloom
for i in range(size):
    element = int(input(f"Enter the {i+1}th element: "))
    lst.append(element)
print(lst)

# Function Call
# result = minimum_days_brute(lst,size,k,m)
# print(result)

result = minimum_days_better(lst,size,k,m)
print(result)