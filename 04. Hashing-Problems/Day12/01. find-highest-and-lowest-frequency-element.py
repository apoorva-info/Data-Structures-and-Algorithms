# This code finds the element with the highest and lowest frequency in an array using a 
# dictionary (map).
# It counts the frequency of each element during the pre-computation step and then fetches the 
# elements with the maximum and minimum frequency.

# Prompt the user to enter the size of the array
size = int(input("Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input(f"Enter the element at array[{i}]: "))
    array.append(element)

# Pre Computation:
frequency_dict = {}
for i in range(size):
    if array[i] in frequency_dict:
        frequency_dict[array[i]] += 1
    else:
        frequency_dict[array[i]] = 1


# Fetch
# max_key = max(frequency_dict, key=frequency_dict.get)
# max_key_value = frequency_dict[max_key]
# min_key = min(frequency_dict, key=frequency_dict.get)
# min_key_value = frequency_dict[min_key]


# Fetch the highest frequency element
max_key_value = max(frequency_dict.values())
for key,value in frequency_dict.items():
    if value == max_key_value:
        print(f"Highest frequency element: {key} , Frequency: {max_key_value}.")

# Fetch the lowest frequency element
min_key_value = min(frequency_dict.values())
for key,value in frequency_dict.items():
    if value == min_key_value:
        print(f"Lowest frequency element: {key} , Frequency: {min_key_value}.")






    