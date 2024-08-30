# Function to print a decreasing sequence pattern of numbers
# Example for a = 5:
# 12345
# 1234
# 123
# 12
# 1
def pattern6(a):
    # Outer loop to control the rows
    for i in range(1, a + 1):
        # Inner loop to print numbers in decreasing order
        for j in range(1, a - i + 2):
            print(j, end="")
        print("")  # Move to the next line after each row

# Function to print a centered pyramid of stars
# Example for a = 4:
#    *   
#   ***  
#  ***** 
# *******
def pattern7(a):
    # Loop to control the number of rows
    for i in range(0, a):
        # Print spaces on the left side to center the stars
        print(" " * (a - i - 1), end="")
        # Print stars in increasing order
        print("*" * (2 * i + 1), end="")
        # Print spaces on the right side
        print(" " * (a - i - 1), end="")
        print("")  # Move to the next line

# Function to print an inverted centered pyramid of stars
# Example for a = 4:
# *******
#  ***** 
#   ***  
#    *   
def pattern8(a):
    # Loop to control the number of rows
    for i in range(0, a):
        # Print spaces on the left side
        print(" " * i, end="")
        # Print stars in decreasing order
        print("*" * (2 * (a - i) - 1), end="")
        # Print spaces on the right side
        print(" " * i, end="")
        print("")  # Move to the next line

# Function to print a diamond shape using pattern7 and pattern8
# Example for a = 4:
#    *   
#   ***  
#  ***** 
# *******
# *******
#  ***** 
#   ***  
#    *   
def pattern9(a):
    # Call pattern7 to print the upper pyramid
    pattern7(a)
    # Call pattern8 to print the lower inverted pyramid
    pattern8(a)

# Function to print a right-aligned triangle of stars
# followed by an inverted right-aligned triangle
# Example for a = 4:
# *
# **
# ***
# ****
# ***
# **
# *
def pattern10(a):
    # First loop to print the increasing triangle
    for i in range(0, a):
        for j in range(0, i + 1):
            print("*", end="")
        print("")
    # Second loop to print the decreasing triangle
    for i in range(0, a):
        print("*" * (a - i - 1), end="")
        print("")

# Function to print a pattern of alternating 1s and 0s
# Example for a = 5:
# 1
# 01
# 101
# 0101
# 10101
def pattern11(a):
    # Outer loop to control the rows
    for i in range(1, a + 1):
        # Determine starting value based on row index
        start = 1 if i % 2 != 0 else 0
        # Inner loop to print alternating 1s and 0s
        for j in range(1, i + 1):
            print(start, end="")
            start = 1 - start  # Toggle between 1 and 0
        print("")  # Move to the next line

# Function to print a pattern of numbers with mirrored sequences
# Example for a = 4:
# 1      1
# 12    21
# 123  321
# 12344321
def pattern12(a):
    # Outer loop to control the rows
    for i in range(1, a + 1):
        # Print increasing sequence of numbers
        for j in range(1, i + 1):
            print(j, end="")
        # Print spaces in the middle
        print(" " * (2 * a - (2 * i)), end="")
        # Print decreasing sequence of numbers
        for j in range(i, 0, -1):
            print(j, end="")
        print("")  # Move to the next line

# Function to print a pattern of consecutive numbers
# Example for a = 4:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
def pattern13(a):
    num = 1  # Start number sequence from 1
    # Outer loop to control the rows
    for i in range(1, a + 1):
        # Inner loop to print numbers
        for j in range(1, i + 1):
            print(num, end=" ")
            num = num + 1  # Increment the number
        print("")  # Move to the next line

# Function to print a pattern of increasing letters
# Example for a = 4:
# A
# AB
# ABC
# ABCD
def pattern14(a):
    # Outer loop to control the rows
    for i in range(1, a + 1):
        # Inner loop to print consecutive letters
        for j in range(ord("A"), ord("A") + i):
            print(chr(j), end="")
        print("")  # Move to the next line

# Function to print a pattern of decreasing letters
# Example for a = 4:
# ABCD
# ABC
# AB
# A
def pattern15(a):
    # Outer loop to control the rows
    for i in range(a, 0, -1):
        # Inner loop to print consecutive letters
        for j in range(0, i):
            print(chr(65 + j), end="")
        print("")  # Move to the next line

# Function to print a pattern of repeated letters
# Example for a = 4:
# A
# BB
# CCC
# DDDD
def pattern16(a):
    # Outer loop to control the rows
    for i in range(1, a + 1):
        # Inner loop to print the same letter multiple times
        for j in range(1, i + 1):
            print(chr(ord("A") + i - 1), end="")
        print("")  # Move to the next line

# Function to print a pyramid pattern of letters with mirroring
# Example for a = 4:
#    A
#   ABA
#  ABCBA
# ABCDCBA
def pattern17(a):
    # Outer loop to control the rows
    for i in range(1, a + 1):
        # Print spaces to center the pattern
        print(" " * (a - i), end="")
        # Print increasing sequence of letters
        for j in range(ord("A"), ord("A") + i):
            print(chr(j), end="")
        # Print decreasing sequence of letters
        for j in range(ord("A") + i, ord("B"), -1):
            print(chr(j - 2), end="")
        # Print spaces to maintain symmetry
        print(" " * (a - i), end="")
        print("")  # Move to the next line
