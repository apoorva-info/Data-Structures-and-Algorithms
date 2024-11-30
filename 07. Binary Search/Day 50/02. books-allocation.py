# Goal:
# Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. 
# There are a ‘m’ number of students, and the task is to allocate all the books to the students.
# Allocate books in such a way that:

# Each student gets at least one book.
# Each book should be allocated to only one student.
# Book allocation should be in a contiguous manner.
# You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. 
# If the allocation of books is not possible, return -1

# Brute Force Approach
def fun(arr,i):
    count = 1
    pages_student = 0
    for j in arr:
        if pages_student + j <= i:
            pages_student += j
        else:
            count += 1
            pages_student = j
    return count

def books_allocation_brute(arr,n,m):
    if m > n:
        return -1
    else:
        low = max(arr)
        high = sum(arr)
        for i in range(low,high+1):
            count_students = fun(arr,i)
            if count_students == m:
                return i
# Time Complexity: O(sum - max) * O(n) 
# Space Complexity: O(1)

# Better Approach
def books_allocation_better(arr,n,m):
    if m > n:
        return -1 
    else:
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = (low + high)//2
            count_students = fun(arr,mid)
            if count_students > m:
                low = mid + 1
            else:
                high = mid - 1
        return low
# Time Complexity: O(log(sum - max)) * O(n) 
# Space Complexity: O(1)

# User Input
students = int(input("Enter the number of students: "))

num = int(input("Enter the total number of books: "))
books = []
for i in range(num):
    pages = int(input(f"Enter the number of pages in the {i+1} book: "))
    books.append(pages)
print(books)

# Function Call
# result = books_allocation_brute(books,num,students)
# print(result)
result = books_allocation_better(books,num,students)
print(result)