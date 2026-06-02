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
'''
#iterator
#it is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__().
