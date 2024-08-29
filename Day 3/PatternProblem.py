num = int(input("Enter a number: "))

# Function to print a right angled triangle with reverse letters
# E
# D E
# C D E 
# B C D E 
# A B C D E
def pattern18(a):
    for i in range(1,a+1): # Outer loop to print the number of rows from 1 to a
        for j in range(1,i+1):
            print(chr(ord("A")+(a-j)), end="")
        print("")


pattern18(num)