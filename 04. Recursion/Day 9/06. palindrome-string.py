# Recursive function to check if a given string is a palindrome
# A palindrome is a string that reads the same forward and backward.
# Example:
# Input 1: Enter a string: helleh
# Output 1: True
# Input 2: Enter a string: hello
# Output 2: False

def palindrome_string(a, i=0):
    # Base case: if the index reaches or exceeds the midpoint, the string is a palindrome
    if i >= (len(a) - i - 1)/2:
        return True
    else:
        # Check if characters at the current index and its corresponding end index are not the same
        if a[i] != a[len(a) - i - 1]:
            return False
        return palindrome_string(a, i + 1) # Recursive call to check the next pair of characters

# Prompt the user to enter a string
original_string = input("Enter a string: ")  # Takes input from the user

# Call the function to check if the string is a palindrome and store the result
result = palindrome_string(original_string, i=0)

# Print the result: True if the string is a palindrome, False otherwise
print(result)

# Time Complexity = O(n)
