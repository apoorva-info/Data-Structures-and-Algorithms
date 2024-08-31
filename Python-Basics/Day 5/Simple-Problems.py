# Function to calculate the sum of first n natural numbers using for and while loop
def natural_numbers_using_for_loop(a):
    sum = 0
    for i in range(1,a+1):
        sum=sum+i
    print(f"The sum of {a} natural numbers is {sum}.") 

def natural_numbers_using_while_loop(a):
    sum=0
    i=1
    while(i<a+1):
        sum=sum+i
        i=i+1
    print(f"The sum of {a} natural numbers is {sum}.") 

# Function to check if the number is a prime number

def prime_number(a):
    if a==1 or a==2:
        print(f"The number {a} is a prime number.")
    else:
        for i in range(2,a):
            if a%i == 0:
                print(f"The number {a} is not a prime number.")
                break
            else:
                print(f"The number {a} is a prime number.")
                break


# Function to print the prime numbers
def display_prime_numbers(a):
    for i in range(1,a+1):
            if (a>2):
                for j in range(2,i):
                    if i%j == 0:
                        break
                else:
                    print(i)
                    




# User input
num=int(input("Enter a number: "))
# Function call
natural_numbers_using_while_loop(num)
natural_numbers_using_for_loop(num)
prime_number(num)
display_prime_numbers(num)
        
