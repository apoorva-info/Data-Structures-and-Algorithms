def print_the_character_n_times(character , num , count = 0):
    if count == num:
        return
    print(character)
    print_the_character_n_times(character,num , count + 1)


# User-Input
character =  input("Enter a character: ")
num = int(input("Number of times you would like to print the character: "))
print_the_character_n_times(character , num)
