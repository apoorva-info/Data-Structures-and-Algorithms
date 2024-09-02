# Program to count the number of digits in a number entered by the user.

# Prompt the user to enter a number and store it as an integer in 'num'
num = int(input("Enter a number: "))

# Example:
# Input: 7789
# Output: "The number of digits in the given number is 4"


# Define a function to count the number of digits in a given number
def countDigits(a):
    count = 0  # Initialize a counter to zero
    while(a > 0):  
        count = count + 1  # Increment the count by 1 for each digit
        a = a // 10  # Remove the last digit from the number
    print("The number of digits in the given number is", count)  



# Call the function with the user-provided number
countDigits(num)


#Time Complexity = O(log₁₀(N))
