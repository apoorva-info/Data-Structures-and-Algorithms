# Recursive function to print numbers from 'a' down to 1 using backtracking
# Example:
# Input 1: 5
# Output 1:
# 5
# 4
# 3
# 2
# 1

def print_reverse_using_backtracking(a, count=1):
    if count > a: # Base Condition
        return
    else:
        print_reverse_using_backtracking(a, count + 1) # Recursive call with an incremented count
        print(count) # Print the current count value during the backtracking phase

# Prompt the user to enter a number
num = int(input("Enter a number: "))  

# Check if the input number is positive.
if num > 0:
    print_reverse_using_backtracking(num)
else:
    print("Please enter a positive number.")  # Prompt the user to enter a positive number if the input is not valid

# Time Complexity = O(n)