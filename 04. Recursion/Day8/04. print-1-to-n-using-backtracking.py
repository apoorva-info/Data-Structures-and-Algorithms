# Recursive function to print numbers from 1 to a given number 'count' using backtracking
# Example:
# Input: 5
# Output:
# 1
# 2
# 3
# 4
# 5

def print_using_backtracking(count):
    if count == 0: # Base case
        return
    else:
        print_using_backtracking(count - 1)  # Recursive call with a decreased value of count
        print(count)  # Recursive call with a decreased value of count

# Prompt the user to enter a number
num = int(input("Enter a number: "))  # Takes an integer input from the user

# Call the function to print numbers from 1 to the entered number using backtracking
print_using_backtracking(num)
