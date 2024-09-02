# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

# Function to check if the given number is an Armstrong number

# Example:
# Input: 153
# Output: 153 is an Armstrong number.


def armstrong_number(a):
    original_number = a  
    sum_of_powers = 0  
    n = count_digits(a)  # Get the number of digits in the number
    
    while a > 0:
        last_digit = a % 10  # Extract the last digit of the number
        sum_of_powers = sum_of_powers + last_digit ** n  # Add the digit raised to the power of n to the sum
        a = a // 10  # Remove the last digit
    
    # Check if the original number is equal to the calculated sum
    if original_number == sum_of_cubes:
        print(f"{original_number} is an Armstrong number.")  # Print if it is an Armstrong number
    else:
        print(f"{original_number} is not an Armstrong number.")  # Print if it is not an Armstrong number


# Function to count the number of digits in a given number
# Example:
# Input: 123
# Output: 3

def count_digits(a):
    count = 0
    while a > 0:
        count = count + 1  # Increment the count for each digit
        a = a // 10  # Remove the last digit
    return count  # Return the total count of digits


# Taking user input and casting it to an integer
num = int(input("Enter a number: "))

# Call the function to check Armstrong number with the user input
armstrong_number(num)


