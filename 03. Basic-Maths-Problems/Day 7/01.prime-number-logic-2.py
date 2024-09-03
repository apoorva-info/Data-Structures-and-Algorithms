# I would like to reduce the time complexity.
# Import the math module to perform mathematical operations
import math

# Function to check if a given number is a prime number
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# The function uses an optimized approach by checking divisors only up to the square root of the number.

def prime_number(a):
    n = int(math.sqrt(a)) # Calculate the square root of the input number and convert it to an integer
    if a <= 1:
        print(f"{a} is not a prime number.")
        return # Exit the function early since the number is not prime
    
    # Iterate from 2 up to the square root of the number
    # This reduces the number of checks and improves efficiency

    for i in range(2,n+1):
        if a % i == 0: # Check if the number is divisible by any value of 'i'
            print(f"{a} is not a prime number.")
            return
    else:  # If no divisors are found in the loop, the number is prime
        print(f"{a} is a prime number.")


# Prompt the user to enter a number and store it as an integer in 'num'
num = int(input("Enter a number: "))
# Call the function to check if the input number is prime
prime_number(num)

# Time Complexity: O(√a)
# The time complexity is reduced to O(√a) by checking only up to the square root of the number.




