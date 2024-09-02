# Function to reverse the digits of a given number

# Prompt the user to enter a number and store it as an integer in 'num'
num = int(input("Enter a number: "))

# Example:
# Input 1: 1234:
# Output 1: "The reverse number is 4321"
# Input 2: 6700
# Output 2: "The reverse number is 76"

def reverseANumber(a):
    reverse_number = 0  # Initialize reverse_number to store the reversed digits
    while(a > 0):
        last_digit = a % 10  # Get the last digit of the number
        a = a // 10  # Remove the last digit from the number
        reverse_number = reverse_number * 10 + last_digit  # Append the last digit to the reversed number
    # Print the reversed number
    print("The reverse number is", reverse_number)

# Call the function with the user-provided number
reverseANumber(num)


