# User Input
num=int(input("Enter a number: "))



# Function to extract digits and print them in reverse
# num=7241621
# output=1261427

def extractionOfDigits(a):
    while(a>0):
        last_digit = a%10
        a = a//10  # Floor Division: The result is always rounded to the nearest integer
        print(last_digit,end="")



    
# Function Call
extractionOfDigits(num)
print() # Printed a new line because I got the output as 1261427%, % operator is not the fault of the code but the environment
