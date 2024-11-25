# Goal: To find the minimum number of days to make m bouquets.

def minimum_days_brute(lst,size,k,m):
    if size < (m*k): # Base Case
        return -1
    else:
        count = 0
        temp = 0 # For counting number of bouquets
        for day in range(min(lst),max(lst)+1):
            for i in range(size):
                if lst[i] <= day:
                    count += 1
                else:
                    temp += (count/k)
                    count = 0
            temp += (count/k)
            if temp == m:
                return day
        

                
                    
            



            




k = int(input("Enter the number of flowers in a bouquet: ")) # Number of flowers in a bouquet
m = int(input("Enter the total number of bouquets: ")) # Total number of bouquets

size = int(input("Enter the size of the array: "))
lst = []
# Number of days taken by a flower to bloom
for i in range(size):
    element = int(input(f"Enter the {i+1}th element: "))
    lst.append(element)

print(lst)

result = minimum_days_brute(lst,size,k,m)
print(result)