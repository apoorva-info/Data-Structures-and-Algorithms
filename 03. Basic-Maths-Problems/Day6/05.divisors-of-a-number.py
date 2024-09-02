# Function to find and print all divisors of a given number
# Example:
# Input: 12
# Output: 1, 2, 3, 4, 6, 12

def divisors_of_num(a):
    for i in range(1,a+1): # Check if the current number 'i' is a divisor of 'a'
        if a % i == 0:
            print(i , end = " ") # Print the divisor
    print()



# Taking user input and casting it to an integer
num = int(input("Enter a number: "))

# Call the function with the user input to display all divisors
divisors_of_num(num)
# Time Complexity = O(log a)       


# What if I want to reduce the time complexity of finding divisors?????

import math

# Function to find divisors with reduced time complexity using square root method
# Instead of iterating up to 'a', we iterate up to sqrt(a), which reduces the time complexity to O(sqrt(a)).
# And I can get all the divisors even if I run the loop till sqrt(a).
# Example : 12
# 1 * 12
# 2 * 6
# 3 * 4

def reduce_tc_divisor(a):
    n = int(math.sqrt(a))  # Calculate the square root of the number
    
    for i in range(1, n + 1):
        # Check if the current number 'i' is a divisor of 'a'
        if a % i == 0:
            print(i , end = " ")  # Print the divisor
            # Check and print the corresponding pair divisor if it's different
            if (a / i) != i: 
                print(a // i, end = " ")  # Use '//' to ensure integer output instead of float
    print()

# Call the function to print divisors with reduced time complexity
reduce_tc_divisor(num)


# Although the reduce_tc_divisor function reduces the time complexity, 
# it does not print the divisors in a sorted manner. To achieve a sorted order, a list can be used.

# Function to find divisors and print them in sorted order
# Example:
# Input: 12
# Output: 1, 2, 3, 4, 6, 12

def divisors_using_list(a):
    divisors = []  # Initialize an empty list to store divisors
    n = int(math.sqrt(a))  # Calculate the square root of the number
    # Loop through numbers from 1 to sqrt(a)
    for i in range(1, n + 1):
        # Check if the current number 'i' is a divisor of 'a'
        if a % i == 0:
            divisors.append(i)  # Append the divisor to the list
            # Check and append the corresponding pair divisor if it's different
            if a / i != i:
                divisors.append(a // i)  # Append the pair divisor
    
    divisors = sorted(divisors)  # Sort the list of divisors

    # Print each divisor in sorted order
    for i in divisors:
        print(i, end=" ")
    print()
# Call the function to print sorted divisors
divisors_using_list(num)

# Time complexity: O(sqrt(a) log a)
