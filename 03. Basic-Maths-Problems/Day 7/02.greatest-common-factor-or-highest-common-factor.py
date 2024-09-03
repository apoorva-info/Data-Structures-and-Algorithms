# Prompt the user to enter two numbers separated by a space
first_input, second_input = map(int, input("Enter two numbers separated by a space: ").split())

# 'split()' splits the input string into a list of strings based on spaces
# 'map(int, ...)' converts each string in the list to an integer


# Function to find the greatest common factor (GCF) of two numbers

def greatest_common_factor(num1, num2):
    n = max(num1, num2) # Find the maximum of the two numbers to determine the range of divisors
    divisors = [] # Initialize an empty list to store common divisors of the two numbers

    for i in range(1, n + 1):
        if num1 % i == 0 and num2 % i == 0: # Check if 'i' is a divisor of both num1 and num2
            divisors.append(i)  # Append the divisor to the list
    
    print(f"The greatest common factor of {first_input} and {second_input} is {divisors[-1]}")
    # divisors[-1] is used to access the last element of the list.

# Call the function with the user-provided numbers
greatest_common_factor(first_input, second_input)
