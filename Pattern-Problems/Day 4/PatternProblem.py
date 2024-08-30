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
        
        


    
pattern19(num)