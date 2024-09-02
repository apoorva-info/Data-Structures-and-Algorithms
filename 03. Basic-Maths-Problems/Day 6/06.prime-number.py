# Function to check if a given number is a prime number
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# Example:
# Input: 7
# Output: 7 is a prime number.

def prime_number(a):
   
    # Check if the number is less than or equal to 1
    if a <= 1:
        print(f"{a} is not a prime number")  # Numbers less than or equal to 1 are not prime numbers

    else:
        # Loop through numbers from 2 to a-1 to check for factors
        for i in range(2, a):
            # Check if 'a' is divisible by 'i'
            if a % i == 0:
                print(f"{a} is not a prime number.")  # Print if a divisor is found
                break  # Exit the loop as we found a divisor
        else:
            # This else belongs to the for loop and executes if no divisors are found
            print(f"{a} is a prime number.")  # Print if no divisors are found, meaning 'a' is prime

# Take user input and cast it to an integer
num = int(input("Enter a number: "))

# Call the function to check if the input number is prime
prime_number(num)
