# Goal: The goal is to find the repeated and missing number in a given array.
# User Input

# Brute Force Approach
def repeating_and_missing_elements_brute(arr,n):
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == i:
                count += 1
        if count == 0:
            missing_number = i
        elif count == 2:
            repeated_number = i
    return repeated_number , missing_number





# def repeating_and_missing_elements(arr,n):
#     ans = []
#     arr = sorted(arr)
#     max_element = max(arr)
#     for i in range(1,n):
#         if arr[i-1] == arr[i]:
#             ans.append(arr[i])
    
#     for i in range(max_element):
#         if i 
lst = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    element = int(input(f"Enter the element at lst[{i}]: "))
    lst.append(element)
print(lst)

result = repeating_and_missing_elements_brute(lst,n)
print(result)