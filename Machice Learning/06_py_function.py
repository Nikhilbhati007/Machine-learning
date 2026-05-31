#Funtion
def greet(name):
#This function takes a name as an argument and prints a greeting message

    print("Hello, " + name + ". Good morning!")
greet("Alice")
greet("Bob")
#Function with return value
def add(a, b):
    return a + b
result = add(5, 3)
print("The sum is:", result)

#Type of Arguments
#Default Arguments
def greet(name="Guest"):
    print("Hello, " + name + ". Good morning!")
greet()
greet("Alice")
#Positional Arguments
def greet(name, message):
    print(message + ", " + name + ".")
greet("Alice", "Hello")
#Keyword Arguments
def greet(name, message):
    print(message + ", " + name + ".")
greet(message="Hi", name="Bob")
#Variable-length Arguments
#*args allows you to pass a variable number of non-keyword arguments to a function. The arguments are accessible as a tuple within the function.
def greet(*names):
    for name in names:
        print("Hello, " + name + ".")
greet("Alice", "Bob", "Charlie")
def Multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result
product = Multiply(2, 3, 4)
print("The product is:", product)
#**kwargs allows you to pass a variable number of keyword arguments to a function. The arguments are accessible as a dictionary within the function.
def greet(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)
greet(name="Alice", message="Hello")

#Arg<*args> and Kwargs<**kwargs>
def greet(*args, **kwargs):
    for name in args:
        print("Hello, " + name + ".")
    for key, value in kwargs.items():
        print(key + ": " + value)

#if we dont give return then python will return None

#local and global variable
x = 10  # Global variable
def my_function():
    x = 5  # Local variable
    print("Inside the function, x =", x)
my_function()
print("Outside the function, x =", x)
#To modify a global variable inside a function, you can use the global keyword
x = 10  # Global variable
def modify_global():
    global x  # Declare x as global to modify it
    x = 5  # Modify the global variable
    print("Inside the function, x =", x)
modify_global()
#Nested Functions
def outer_function():
    print("This is the outer function.")
    def inner_function():
        print("This is the inner function.")
    inner_function()  # Call the inner function
outer_function()  # Call the outer function
#Fuction are 1 first class citizens in python
def square(x):
    return x * x
type(square)  # Output: <class 'function'>
id(square)  # Output: Memory address of the function object
#can be assigned to a variable
sqr = square
print(sqr(5))  # Output: 25
#delete the function
#del square
#Now, trying to call square will result in a NameError
try:
    print(square(5))
except NameError as e:
    print(e)  # Output: name 'square' is not defined
#restore the function
l=[1,2,3,squre]
#function is immutable
#return a function from another function
def outer():
    def inner(a,b):
        return a+b
    return inner
my_inner_function = outer()(2,3)
print(my_inner_function())  # Output: 5

# give a input as the function
def greet(name):
    return "Hello, " + name + ". Good morning!" 
def process_greeting(func, name):
    return func(name)
greeting_message = process_greeting(greet, "Alice")
print(greeting_message)  # Output: Hello, Alice. Good morning!

#Lambda Function
#Lambda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not reused elsewhere in the code.
#they return the value of the expression they evaluate
add = lambda x, y: x + y
result = add(5, 3)
print("The sum is:", result)
a=lambda x: "even" if x%2==0 else "odd"
print(a(4))  # Output: even
#Map function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
#Filter function
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
#Reduce function
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

 


