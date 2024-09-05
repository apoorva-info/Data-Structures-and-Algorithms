# Recursive function to print numbers from 1 to a given number 'a'
# Example:
# Input 1: 5
# Output 1:
# 1
# 2
# 3
# 4
# 5

def print_number(a, count=1):
    if count == a + 1: # Base case: if count reaches a + 1, stop the recursion
        return
    else:
        print(count) # Print the current count value
        print_number(a, count + 1) # Recursive call to print the next number

# Prompt the user to enter a number
num = int(input("Enter a number: "))  

# Call the function to print numbers from 1 to the entered number
print_number(num)

# Time Complexity = O(n)