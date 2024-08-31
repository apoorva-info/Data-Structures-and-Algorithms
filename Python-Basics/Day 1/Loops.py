# Iterating over a string using for loop

a = "Hello, how are you?"
for i in a:
    print(i)
print()
print()

# Break statement 
# Exits the loop prematurely

for i in range(10):
    if i == 6:
        break #Prints till 5 and then exits the for loop
    print(i)
print()
print()

# Continue Statement
# Skips the current iteration and continues with the next

for i in range(10):
    if i == 8:
        continue #skips 8 and continues with the next (9 in this code)
    print(i)
print()
print()

# Pass Statement
# Null Operation, it does nothing

for i in range(10):
    if i == 4:
        print("The number is ",i)
        pass
    print(i)
print()
print()

