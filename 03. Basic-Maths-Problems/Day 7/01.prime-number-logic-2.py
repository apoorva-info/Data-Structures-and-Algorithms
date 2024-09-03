# I would like to reduce the time complexity.
# Import the math module to perform mathematical operations
import math

# Function to check if a given number is a prime number
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# The function uses an optimized approach by checking divisors only up to the square root of the number.
# Example:
# Input 1: 11
# Output 1: "11 is a prime number."
# Input 2: 12
# Output 2: "12 is not a prime number."

def prime_number(a):
    n = int(math.sqrt(a)) # Calculate the square root of the input number and convert it to an integer
    if a <= 1:
        print(f"{a} is not a prime number.")
        return # Exit the function early since the number is not prime

    for i in range(2,n+1):  # Iterate from 2 up to the square root of the number. This reduces the number of checks and improves efficiency
        if a % i == 0: # Check if the number is divisible by any value of 'i'
            print(f"{a} is not a prime number.")
            return
    else:  # If no divisors are found in the loop, the number is prime
        print(f"{a} is a prime number.")



# Function to check if a number is prime using a counter-based approach

def prime_number_using_counter(a):
    # Calculate the square root of the number 'a' and convert it to an integer
    n = int(math.sqrt(a))
    
    # Initialize a counter to count the number of divisors of 'a'
    count = 0
    
    # Loop through numbers from 1 to n (inclusive) to check for divisors
    for i in range(1, n + 1):
        # Check if 'i' is a divisor of 'a'
        if a % i == 0:
            count = count + 1  # Increment count as 'i' is a divisor
            
            # Check if the division result is not the same as 'i' to count both divisors
            if (a / i) != i:
                count += 1  # Increment count for the other divisor (a / i)
    
    # Check if the count of divisors is exactly 2 (only divisible by 1 and itself)
    if count == 2:
        print(f"{a} is a prime number.")  # Print that 'a' is prime
    else:
        print(f"{a} is not a prime number.")  # Print that 'a' is not prime

# Prompt the user to enter a number and store it as an integer in 'num'
num = int(input("Enter a number: "))
# Call the function to check if the input number is prime
prime_number(num)
prime_number_using_counter(num)

# Time Complexity: O(√a)
# The time complexity is reduced to O(√a) by checking only up to the square root of the number.




