# Recursive function to calculate the Fibonacci number at a given position 'a'
# The Fibonacci sequence is defined as:
# F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1
# Example:
# Input: Enter a number: 5
# Output: The Fibonacci number at position 5 is 5.


def fibonacci_number(a):
    if a <= 1: # Base Case
        return a
    else:
        # Recursive call to calculate the Fibonacci number using the sum of the two preceding numbers
        return fibonacci_number(a - 1) + fibonacci_number(a - 2)

# Prompt the user to enter a position number
num = int(input("Enter a number: "))  

# Call the function to get the Fibonacci number at the given position
result = fibonacci_number(num)

# Print the result
print(f"The Fibonacci number at position {num} is {result}.")

# Time Complexity = O(2^n)
