# Hashing Methods:
# 1. Division Method (Most Important)
# 2. Folding Method
# 3. Mid Square Method

# Prompt the user to enter the size of the array
size = int(input("Enter the size of array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Pre Compute Using Division Method
hash_table = [0] * 10  # Size Limitation
for i in range(size):
    index = array[i] % 10  # Compute index using Division Method
    hash_table[index] += 1  

# Prompt the user to enter the size of the query
q = int(input("Enter the size of query: "))
for i in range(q):
    query = int(input("Enter the query: "))
    # Fetch the frequency of the queried number using the precomputed hash table
    index = query % 10
    print(f"The frequency of {query} is {hash_table[index]}.")

#  Unordered map ---> O(1) ---> Best Case and Average Case 
#                ---> O(n) ---> Worst Case ---> Rarely happens 
#                ---> Won't allow pairs 
# Collisions are common here so I will be using chaining to avoid collisions.
# If there are multiple values, I can do linear chaining.
