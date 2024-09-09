# Taking an integer input from the user
num = int(input("Enter a number: "))

# Function to print a square pattern of asterisks
# Example for num = 4:
# ****
# ****
# ****
# ****
def pattern1(a):
    # Outer loop to control the number of rows
    for i in range(a):
        # Inner loop to control the number of columns
        for j in range(a):
            print("*", end="")  # Print an asterisk without moving to the next line
        print("")  # Move to the next line after completing each row

# Function to print a right-angled triangle pattern of asterisks
# Example for num = 4:
# *
# **
# ***
# ****
def pattern2(a):
    # Outer loop to control the number of rows
    for i in range(a):
        # Inner loop to control the number of columns
        for j in range(a):
            if j <= i:  # Condition to print asterisks up to the current row index
                print("*", end="")  # Print an asterisk without moving to the next line
        print("")  # Move to the next line after completing each row

# Function to print a right-angled triangle pattern with increasing numbers
# Example for num = 5:
# 1
# 12
# 123
# 1234
def pattern3(a):
    # Outer loop starting from 1 to (a-1)
    for i in range(1, a):
        # Inner loop to control number printing up to the current row index
        for j in range(1, a):
            if j <= i:  # Condition to print numbers up to the current row index
                print(j, end="")  # Print the current number without moving to the next line
        print("")  # Move to the next line after completing each row

# Function to print a right-angled triangle pattern with repeated row numbers
# Example for num = 5:
# 1
# 22
# 333
# 4444
def pattern4(a):
    # Outer loop starting from 1 to (a-1)
    for i in range(1, a):
        # Inner loop to control number printing up to the current row index
        for j in range(1, a):
            if j <= i:  # Condition to print numbers up to the current row index
                print(i, end="")  # Print the current row number without moving to the next line
        print("")  # Move to the next line after completing each row

# Function to print an inverted right-angled triangle pattern of asterisks
# Example for num = 5:
# *****
# ****
# ***
# **
# *
def pattern5(a):
    # Outer loop starting from 0 to (a-1)
    for i in range(0, a):
        # Inner loop to print asterisks decreasing with each row
        for j in range(0, a - i):
            print("*", end="")  # Print an asterisk without moving to the next line
        print("")  # Move to the next line after completing each row
