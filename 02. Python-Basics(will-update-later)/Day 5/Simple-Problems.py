# Function to calculate the sum of the first n natural numbers using a for loop
# Example for a = 5:
# The sum of 5 natural numbers is 15.

def natural_numbers_using_for_loop(a):
    sum = 0  
    # Iterate from 1 to a (inclusive) to add each number to the sum
    for i in range(1, a + 1):
        sum = sum + i
    print(f"The sum of {a} natural numbers is {sum}.")


# Function to calculate the sum of the first n natural numbers using a while loop
# Example for a = 5:
# The sum of 5 natural numbers is 15.

def natural_numbers_using_while_loop(a):
    sum = 0  
    i = 1  
    # Use while loop to add numbers from 1 to a
    while i < a + 1:
        sum = sum + i
        i = i + 1  # Increment i
    print(f"The sum of {a} natural numbers is {sum}.")


# Function to check if a number is a prime number
# Example for a = 9:
# The number 9 is not a prime number.

def prime_number(a):
    if a == 1:
        print(f"The number {a} is not a prime number.")  # 1 is not a prime
    elif a == 2:
        print(f"The number {a} is a prime number.")  # 2 is a prime
    else:
        # Check divisibility from 2 to a-1 to determine primality
        for i in range(2, a):
            if a % i == 0:  # If divisible by any i, it's not a prime
                print(f"The number {a} is not a prime number.")
                break
            else:
                print(f"The number {a} is a prime number.")
                break


# Function to print all prime numbers up to a given number
# Example for a = 10:
# 2
# 3
# 5
# 7

def display_prime_numbers(a):
    # Iterate from 1 to a (inclusive) to find prime numbers
    for i in range(2, a + 1):
        if a > 2:  
            # Check if i is divisible by any number from 2 to i-1
            for j in range(2, i):
                if i % j == 0:  # If divisible, not a prime
                    break
            else: # Unique feature in python : else statement can be used with the loop
                print(i)  # Print the number if it's prime


# User input to get a number
num = int(input("Enter a number: "))

# Function calls
natural_numbers_using_while_loop(num)  # Calculate sum using while loop
natural_numbers_using_for_loop(num)    # Calculate sum using for loop
prime_number(num)                      # Check if the number is prime
display_prime_numbers(num)             # Display all prime numbers up to the given number
