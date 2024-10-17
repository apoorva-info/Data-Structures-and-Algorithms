# Recursive function to calculate the factorial of a given number 'a'
# Example:
# Input: 5
# Output: "The factorial of 5 is 120."

def factorial_of_n(a):
    if a == 0: # Base Condition
        return 1
    else:
        return a * factorial_of_n(a - 1) # Recursive call to calculate the factorial of (a-1) and multiply it by 'a'

# Prompt the user to enter a number
num = int(input("Enter a number: "))  # Takes an integer input from the user

# Call the function and store the result
result = factorial_of_n(num)

# Print the result of the factorial
print(f"The factorial of {num} is {result}.")

# Time Complexity = O(n)
