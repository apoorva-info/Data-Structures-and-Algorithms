# Recursive function to print a given character 'num' times
# Example:
# Input 1: character = '*', num = 3
# Output 1:
# *
# *
# *

def print_the_character_n_times(character, num, count=0):
    # Base case: if the count matches the number of times, stop the recursion
    if count == num:
        return
    print(character)
    
    # Recursive call with incremented count
    print_the_character_n_times(character, num, count + 1)

# Prompt the user to enter a character and the number of times to print it
character = input("Enter a character: ")  # Takes the character input from the user
num = int(input("Number of times you would like to print the character: "))  # Takes the number of repetitions as input

# Call the recursive function with the user-provided inputs
print_the_character_n_times(character, num)

# Time Complexity = O(n)