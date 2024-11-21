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
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for i in myiter:
    print(i)
