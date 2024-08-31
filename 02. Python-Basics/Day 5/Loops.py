# Iterating over a string using a for loop
# Example:
# For the string "Hello, how are you?", each character is printed individually.
# Output:
# H
# e
# l
# l
# o
# ,
#  
# h
# o
# w
#  
# a
# r
# e
#  
# y
# o
# u
# ?

a = "Hello, how are you?"
for i in a:  # Loop through each character in the string
    print(i)  # Print each character
print()
print()


# Break statement
# Exits the loop prematurely when the condition is met
# Example: 
# For the range 0 to 9, when i reaches 6, the loop breaks, stopping further iteration.
# Output:
# 0
# 1
# 2
# 3
# 4
# 5

for i in range(10):
    if i == 6:
        break  # Exits the loop when i is 6
    print(i)
print()
print()


# Continue statement
# Skips the current iteration when the condition is met and continues with the next iteration
# Example:
# For the range 0 to 9, when i is 8, it skips printing 8 and continues with 9.
# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 9

for i in range(10):
    if i == 8:
        continue  # Skips the current iteration when i is 8
    print(i)
print()
print()


# Pass statement
# Null operation; it does nothing but is used as a placeholder
# Example:
# For the range 0 to 9, when i is 4, "The number is 4" is printed, and the pass statement does nothing, allowing the loop to continue.
# Output:
# 0
# 1
# 2
# 3
# The number is 4
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(10):
    if i == 4:
        print("The number is ", i)  # Prints the message when i is 4
        pass  # Pass does nothing; the loop continues normally
    print(i)
print()
print()
