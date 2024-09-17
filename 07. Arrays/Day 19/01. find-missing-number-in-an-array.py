from array import array
def missing_number(arr,n):
    for i in range(1,n+1):
        if i not in arr:
            return i






# User Input
user_array = array('i',[2,5,4,3,1])
len_of_user_array = 5
result = missing_number(user_array,len_of_user_array)
print(f"Missing number: {result}")
