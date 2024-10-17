# Recursive function to calculate the sum of numbers from 1 to 'a' using a parameterized approach
# Example:
# Input: 5
# Output: "The sum of the numbers is 15."

def sum_using_parameterized_way(a, sum=0):
    if a == 0: # Base Condition
        print(f"The sum of the numbers is {sum}.")
        return
    else:
        sum_using_parameterized_way(a - 1, sum=sum + a) # Recursive call, decrementing 'a' and adding the current value of 'a' to 'sum'

# Prompt the user to enter a number
num = int(input("Enter a number: "))  # Takes an integer input from the user

# Call the function with the user-provided number
sum_using_parameterized_way(num)

# Time Complexity = O(n)
