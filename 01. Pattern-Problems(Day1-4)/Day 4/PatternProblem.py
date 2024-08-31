# Function to print a symmetrical pattern of stars with mirrored sequences
# Example for a = 4:
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
def pattern19(a):
    # Print the upper half of the pattern
    for i in range(a, 0, -1):
        # Print the left side stars
        for j in range(1, i + 1):
            print("*", end="")
        # Print spaces in the middle
        print(" " * (2 * (a - i)), end="")
        # Print the right side stars
        for j in range(1, i + 1):
            print("*", end="")
        print()  # Move to the next line
    
    # Print the lower half of the pattern
    for i in range(1, a + 1):
        # Print the left side stars
        for j in range(1, i + 1):
            print("*", end="")
        # Print spaces in the middle
        print(" " * (2 * (a - i)), end="")
        # Print the right side stars
        for j in range(1, i + 1):
            print("*", end="")
        print()  # Move to the next line
    print()  # Final line break

# Function to print a pattern of stars forming a symmetrical diamond shape
# Example for a = 4:
# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *
def pattern20(a):
    # Print the upper half of the pattern
    for i in range(1, a + 1):
        # Print the left side stars
        for j in range(1, i + 1):
            print("*", end="")
        # Print spaces in the middle
        print(" " * (2 * (a - i)), end="")
        # Print the right side stars
        for j in range(1, i + 1):
            print("*", end="")
        print()  # Move to the next line
    
    # Print the lower half of the pattern
    for i in range(a - 1, 0, -1):
        # Print the left side stars
        for j in range(1, i + 1):
            print("*", end="")
        # Print spaces in the middle
        print(" " * (2 * (a - i)), end="")
        # Print the right side stars
        for j in range(1, i + 1):
            print("*", end="")
        print()  # Move to the next line

# Function to print a hollow rectangle of stars
# Example for a = 5:
# *****
# *   *
# *   *
# *****
def pattern21(a):
    # Print the top row of stars
    for i in range(1, a + 1):
        print("*", end="")
    print()  # Move to the next line
    
    # Print the middle rows with spaces
    for i in range(1, a - 2 + 1):
        print("*", end="")
        print(" " * (a - 2), end="")
        print("*", end="")
        print()  # Move to the next line
    
    # Print the bottom row of stars
    for i in range(1, a + 1):
        print("*", end="")
    print()  # Final line break

# Function to print a pattern of numbers decreasing towards the center
# Example for a = 4:
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444
def pattern22(a):
    n = int(a / 2)  # Define the middle point
    # Outer loop for the rows
    for i in range(1, 2 * a - 2):
        # Inner loop for the columns
        for j in range(1, 2 * a - 2):
            # Determine the value to print based on the minimum distance from any edge
            top = i
            left = j
            right = (2 * a - 2) - j
            bottom = (2 * a - 2) - i
            print(a - min(min(top, bottom), min(left, right)), end="")
        print()  # Move to the next line

# Example of how to use the function with user input
num = int(input("Enter a number: "))
pattern22(num)
