# Function to check if a given number is a prime number
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# Example:
# Input: 7
# Output: 7 is a prime number.

def prime_number(a):
   
    if a <= 1:
        print(f"{a} is not a prime number")  

    else:
        
        for i in range(2, a):
            # Check if 'a' is divisible by 'i'
            if a % i == 0:
                print(f"{a} is not a prime number.")  
                break  # Exit the loop as we found a divisor
        else:
            # This else belongs to the for loop and executes if no divisors are found
            print(f"{a} is a prime number.")  

# Take user input and cast it to an integer
num = int(input("Enter a number: "))

# Call the function to check if the input number is prime
prime_number(num)



# Function to find and print all prime numbers in the range from 2 to the given number 'a'
# This function checks each number within the range to determine if it is prime.
# Example:
# Input: 10
# Output: 2, 3, 5, 7

def prime_number_range(a):
    
    for i in range(2, a + 1): # Loop through each number from 2 to 'a' since 1 is not a prime number
        
        if a > 2:
            for j in range(2, i):
                if i % j == 0:  
                    break  # Break if a divisor is found, meaning 'i' is not prime
            else:
                print(i, end=" ")  # Print the prime number

# Call the function to print all prime numbers up to the user input number
prime_number_range(num)
