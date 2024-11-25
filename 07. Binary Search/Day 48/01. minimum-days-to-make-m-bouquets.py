# Goal: To find the minimum number of days to make m bouquets.

def minimum_days_brute(lst,size,k,m):
    if size < (m*k): # Base Case
        return -1
    else:
        min_value = min(lst)
        max_value = max(lst)
        count = 0
        temp = 0
        for i in range(min_value,max_value+1):
            for j in range(size):
                if lst[j] <= i:
                    count += 1
                    if count == k:
                        temp += 1
                        if temp == m:
                            return i
                else:
                    count = 0 
            
        

                
                    
            



            




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
