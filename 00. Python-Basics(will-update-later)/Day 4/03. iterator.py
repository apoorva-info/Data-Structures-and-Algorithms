# Iterator: Object that contains countable number of values
# In python, iterator is the object that implements iterable protocols which consists of __iter__() and __next__()

# fruits = ['apple', 'banana', 'cherry']
# x = iter(fruits)
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))