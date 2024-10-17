# This code calculates the frequency of any characters (including special characters) in a given input string using a hash array.
# Example:
# Input:
# Enter the characters: hello@2024
# Enter the numbers of characters whose frequencies are to be checked: 3
# Enter the character: l
# Output:
# The frequency of l is 2.
# Enter the character: @
# Output:
# The frequency of @ is 1.
# Enter the character: 2
# Output:
# The frequency of 2 is 2.

# Prompt the user to enter a string of characters
characters = input("Enter the characters: ")

# Pre-computation
hash = [0] * 256

# Calculate the frequency of each character in the string
for i in range(len(characters)):
    hash[ord(characters[i])] += 1

# Prompt the user to enter the number of characters whose frequencies are to be checked
q = int(input("Enter the numbers of characters whose frequencies are to be checked: "))

# Fetch Method
for i in range(q):
    query = input("Enter the character: ")
    print(f"The frequency of {query} is {hash[ord(query)]}.")

# Time Complexity = O(n)