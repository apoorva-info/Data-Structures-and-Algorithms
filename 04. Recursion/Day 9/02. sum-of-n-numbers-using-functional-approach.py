# Recursive function to calculate the sum of numbers from 1 to 'a' using a functional approach
# Example:
# Input: 5
# Output: "The sum of numbers is 15."

def sum_of_n_numbers_using_functional_approach(a):
    if a == 0: # Base Condition
        return 0
    else:
        return a + sum_of_n_numbers_using_functional_approach(a - 1) # Recursive call to add 'a' to the sum of numbers from (a-1) down to 1

# Prompt the user to enter a number
num = int(input("Enter a number: "))  # Takes an integer input from the user

# Call the function and store the result
result = sum_of_n_numbers_using_functional_approach(num)

# Print the result of the sum
print(f"The sum of numbers is {result}.")

# Time Complexity = O(n)
