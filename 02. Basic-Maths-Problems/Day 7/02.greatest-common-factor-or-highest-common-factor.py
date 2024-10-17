# Prompt the user to enter two numbers separated by a space
first_input, second_input = map(int, input("Enter two numbers separated by a space: ").split())

# 'split()' splits the input string into a list of strings based on spaces
# 'map(int, ...)' converts each string in the list to an integer


# Function to find the greatest common factor (GCF) of two numbers

def greatest_common_factor(num1, num2):
    n = min(num1, num2) # Find the minimum of the two numbers to determine the range of divisors
    divisors = [] # Initialize an empty list to store common divisors of the two numbers

    for i in range(1, n + 1):
        if num1 % i == 0 and num2 % i == 0: # Check if 'i' is a divisor of both num1 and num2
            divisors.append(i)  # Append the divisor to the list
    
    print(f"The greatest common factor of {first_input} and {second_input} is {divisors[-1]}")
    # divisors[-1] is used to access the last element of the list.

# Call the function with the user-provided numbers
greatest_common_factor(first_input, second_input)

# Time Complexity = O(min(first_value , second_value))



# Function to find the greatest common factor (GCF) of two numbers using the Euclidean algorithm
"""Euclidean Algorithm: A method to find the GCF of two numbers by repeatedly
replacing the larger number with the remainder when it is divided by the smaller number.
The process continues until one of the numbers becomes zero. The non-zero number is the GCF.
GCF(a , b) = GCF(b , a % b) """

# Example:
# Input 1: 12 18
# Output 1: "The greatest common factor of 12 and 18 is 6"


def gcd_using_euclidean_algo(num1, num2):
   
    while num1 > 0 and num2 > 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    
    if num1 == 0:
        return print(f"The greatest common factor of {first_input} and {second_input} is {num2}")
    return print(f"The greatest common factor of {first_input} and {second_input} is {num1}")

# Call the function with the user-provided numbers
gcd_using_euclidean_algo(first_input, second_input)

# Time Complexity: O(log_ϕ(min(num1, num2)))
# Explanation: The time complexity is logarithmic relative to the size of the smaller input,
# which makes the Euclidean algorithm very efficient for large numbers.


        
    


