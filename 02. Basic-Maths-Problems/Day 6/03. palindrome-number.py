# A Palindrome number is a number that remains the same when its digits are reversed.

# User input and type casting to integer
num = int(input("Enter a number: "))


# Function to check if the number is palindrome or not.
# Example:
# Input: 121
# Output: True

def palindrome_number(a):
    original_number = a
    reverse_number = 0
 
    # Loop to reverse the digits of the number
    while(a > 0):
        last_digit = a % 10  # Extract the last digit of the number
        a = a // 10  # Remove the last digit from the number
        reverse_number = reverse_number * 10 + last_digit  # Add the last digit to the reversed number
    
    # Check if the original number is equal to the reversed number
    if original_number == reverse_number:
        print(True)
    else:
        print(False)

# Call the function with the user input
palindrome_number(num)


