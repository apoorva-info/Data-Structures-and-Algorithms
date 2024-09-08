# This code calculates the frequency of lowercase alphabetic characters in a string using a hash array (frequency array).
# Example:
# Input:
# Enter a string of lowercase characters: hello
# Enter the number of characters that you want to check: 2
# Enter the character whose frequency you want to check: l
# Output:
# The frequency of l is 2.
# Enter the character whose frequency you want to check: e
# Output:
# The frequency of e is 1.

# Prompt the user to enter a string of lowercase characters
string = input("Enter a string of lowercase characters: ")

# Pre-computation
hash = [0] * 26

# Calculate the frequency of each character in the string
for i in range(len(string)):
    hash[ord(string[i]) - ord('a')] += 1 # Increase the count by 1


q = int(input("Enter the number of characters that you want to check: "))

# Fetch Method: Checking the frequency of specified characters
for i in range(q):
    character = input("Enter the character whose frequency you want to check: ")
    print(f"The frequency of {character} is {hash[ord(character) - ord('a')]}.")
