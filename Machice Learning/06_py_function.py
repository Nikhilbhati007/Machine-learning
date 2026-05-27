'''
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
#Lambda Function
add = lambda x, y: x + y
result = add(5, 3)
print("The sum is:", result)
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
'''
#Nested Functions
def outer_function():
    print("This is the outer function.")
    def inner_function():
        print("This is the inner function.")
    inner_function()  # Call the inner function
outer_function()  # Call the outer function


 


