num = int(input("Enter a number: "))

def countDigits(a):
    count=0
    while(a>0): #7789
        n = a%10 #9
        count=count+1
        a = a//10 #778
    print("The number of digits in the given numbers is ",count)
    
countDigits(num)