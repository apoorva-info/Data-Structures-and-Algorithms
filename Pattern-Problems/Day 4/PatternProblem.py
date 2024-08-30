num = int(input("Enter a number: "))

def pattern19(a):
        for i in range(a,0,-1):
                for j in range(1,i+1):
                    print("*", end="")
                print(" " * (2*(a-i)),end="")
                for j in range(1,i+1):
                    print("*", end="")
                print()
                
        for i in range(1,a+1):
                for j in range(1,i+1):
                    print("*", end="")
                print(" " * (2*(a-i)),end="")
                for j in range(1,i+1):
                    print("*", end="")
                print()
                    
                        
            
        print()

def pattern20(a):
        for i in range(1,a+1):
            for j in range(1,i+1):
                  print("*",end="")
            print(" " * (2*(a-i)),end="")
            for j in range(1,i+1):
                  print("*",end="")
            print()
        for i in range(a-1,0,-1):
            for j in range(1,i+1):
                  print("*",end="")
            print(" " * (2*(a-i)),end="")
            for j in range(1,i+1):
                  print("*",end="")
            print()

def pattern21(a):
    for i in range(1,a+1):
        print("*",end="")
    print()
    for i in range(1,a-2+1):
        print("*",end="")
        print(" " * (a-2),end="")
        print("*",end="")
        print()
    for i in range(1,a+1):
        print("*",end="")
    print()

def pattern22(a):
    n=int(a/2)
    for i in range(1,2*a-2):
        for j in range(1,2*a-2):
             top = i
             left = j
             right = (2*a-2)-j
             bottom = (2*a-2)-i
             print(a - min(min(top,bottom),min(left,right)),end="")
        print()
    




        
    

    
pattern22(num)