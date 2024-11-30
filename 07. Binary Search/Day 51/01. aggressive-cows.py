# Goal: Find the maximum possible minimum distance between the two cows.

# Brute Force Approach
def canWePlace(arr,distance,cows):
    count = 1
    last = arr[0]
    for i in arr:
        if arr[i] - last >= distance:
            count += 1
            last = arr[i]
    if count >= cows:
        return True
    else:
        return False


def max_possible_min_distance_brute(arr,c):
    for i in range(1,max-min):
        if canWePlace(arr,i,c) == True:
            continue
        else:
            return i-1
# Time Complexity: O(max-min)*O(n)
# Space Complexity: O(1)

# User Input
cows = int(input("Enter the number of cows: "))

stalls = int(input("Enter the total number of stalls: "))
positions = []
for i in range(stalls):
    position = int(input(f"Enter the position of the {i+1} stall: "))
    positions.append(position)

print(positions)
positions = sorted(positions)

# Function Call
result = max_possible_min_distance_brute(positions,stalls,cows)
print(result)