'''
#Multiply
def multiply(a,b):
    if b == 0:
        return 0
    elif b < 0:
        return -multiply(a,-b)
    else:
        return a + multiply(a,b-1)
print(multiply(5,3)) #15
print(multiply(5,-3)) #-15
#fabonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10)) #55
#highly time consuming
#memoization
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10)) #55
#iterator
#it is the object which perform iteration over a sequence, such as a list, tuple, or string.
#it is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__().
#iterable
#it is an object that can be iterated over, meaning it can return an iterator when the iter() function is called on it.
l=[1,2,3]
type(iter(l)) #<class 'list_iterator'>
#l is iterable
a=10
print(dir(a))#to check iterable or not
print(dir(l))#if __iter__ is present then it is 
#check iterator
print(dir(l)) #if __next__ and __iter__is present then it is an iterator
#but l is not an iterator, it is an iterable
it=iter(l) #it is an iterator
print(dir(it)) #it has __iter__ and __next__
#understanding for loop 
num=[1,2,3]
for i in num:
    print(i)
#step-1: it fetch the iterator 
it_num=iter(num)
#step-2: it calls the __next__() method of the iterator to get the next item in the sequence
print(it_num.__next__()) #1
print(it_num.__next__()) #2
print(it_num.__next__()) #3
def my_for_loop(iterable):
    it = iter(iterable)
    while True:
        try:
            item = next(it)
            print(item)
        except StopIteration:
            break
my_for_loop([1, 2, 3])
my_for_loop("Hello")
num=[1,2,3]
it=iter(num)
print(id(it)) #memory address of the iterator
print(id(iter(it))) #memory address of a new iterator
#both iterators are different objects with different memory addresses, but they will iterate over the same sequence of numbers.
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return MyRangeIterator(self.start, self.end)
class Myrangeiterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current
'''
#Generators
#It simple way to create iterators using a function that uses the yield statement to produce a sequence of values.
def gen_demo():
    yield 1
    yield 2
    yield 3
g=gen_demo()
#print(next(g)) #1
#print(next(g)) #2
#print(next(g)) #3
#for i in gen_demo():
  #  print(i)
#Yeild vs return
print(g) #<generator object gen_demo at 0x000001E2B8C9B5C0>
print(next(g)) #1   
print(next(g)) #2
print(next(g)) #3
#after the last yield, the generator is exhausted and raises StopIteration if you try to call next() again.
print(next(g)) #StopIteration   
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(5)
for number in counter:
    print(number) #1,2,3,4,5
#generator expression
squares = (x**2 for x in range(10))
for square in squares:
    print(square) #0,1,4,9,16,25,36,49,64,81
gen = (x**2 for x in range(10))
print(next(gen)) #0
print(next(gen)) #1
print(next(gen)) #4
print(next(gen)) #9