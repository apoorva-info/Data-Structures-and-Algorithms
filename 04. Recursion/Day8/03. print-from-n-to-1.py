# Recursive function to print numbers from a given number 'a' down to 1 in reverse order
# Example:
# Input 1: 5
# Output 1:
# 5
# 4
# 3
# 2
# 1

def reverse_print(a):
    if a == 0: # Base Case
        return
    else:   
        print(a) # Print the current value of 'a'

    reverse_print(a - 1) # Recursive call with a decreased value of 'a'

# Prompt the user to enter a number
num = int(input("Enter a number: "))  # Takes an integer input from the user

# Call the function to print numbers from the entered number down to 1
reverse_print(num)
