'''
#Namespace
#it is a container for variables and functions.
# It is a way to organize code and avoid name conflicts. 
# In Python, we can create a namespace using a class or a module.
#type of namespace
#1. Global namespace: It is the namespace that contains all the built-in functions and variables. It is created when the Python interpreter starts and is destroyed when the interpreter exits.
#2. Local namespace: It is the namespace that is created when a function is called.
#3. Enclosing namespace: It is the namespace that is created when a function is defined inside another function.    
#4. Built-in namespace: It is the namespace that contains all the built-in functions and variables. It is created when the Python interpreter starts and is destroyed when the interpreter exits.
a=10 #global namespace
def func():
    b=20 #local namespace
    print(a) #global namespace
    print(b) #local namespace
func() 
#built-in namespace
import builtins
print(dir(builtins)) #built-in namespace
print(len("Hello")) #built-in namespace
l=[1,2,3,4,5]
max(l) #built-in namespace
def max():
    return "This is my own max function"
print(max(l)) #local namespace
#Enclosing namespace
def outer():
    x=10 #enclosing namespace
    def inner():
        print(x) #enclosing namespace
    inner()
outer()
#decorator
# A decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.
def decorator(func):
    def wrapper():
        print("***************")
        func()
        print("***************")
    return wrapper
@decorator
def say_hello():
    print("Hello, World!")
say_hello()

#type of decorator
#1 built in : It is a decorator that is applied to a function.
#@staticmethod, @classmethod, @property are examples of built-in decorators.
#2. Class decorator: It is a decorator that is applied to a class.
'''
#meaningful decorator
import time
def timer(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
    return wrapper
@timer
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    time.sleep(1) # Simulate a time-consuming task
    