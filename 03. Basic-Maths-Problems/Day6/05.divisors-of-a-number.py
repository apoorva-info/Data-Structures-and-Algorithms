# Function to find and print all divisors of a given number
# Example:
# Input: 12
# Output: 1, 2, 3, 4, 6, 12

def divisors_of_num(a):
    for i in range(1,a+1): # Check if the current number 'i' is a divisor of 'a'
        if a % i == 0:
            print(i) # Print the divisor



# Taking user input and casting it to an integer
num = int(input("Enter a number: "))

# Call the function with the user input to display all divisors
divisors_of_num(num)


        
        


