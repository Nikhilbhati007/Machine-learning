#type of error
# SyntaxError
Print("Hello World") #SyntaxError: invalid syntax
# NameError
print(x) #NameError: name 'x' is not defined
# ZeroDivisionError
print(10/0) #ZeroDivisionError: division by zero
# IndexError
my_list = [1, 2, 3]
print(my_list[5]) #IndexError: list index out of range
# KeyError
my_dict = {"name": "Alice", "age": 30}
# ValueError
int("abc") #ValueError: invalid literal for int() with base 10: 'abc'
# FileNotFoundError
with open("non_existent_file.txt", "r") as file:
    content = file.read() #FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
#attributeError
print(my_dict["height"]) #KeyError: 'height'
#exception handling
try:
    print(10/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
L=[1,2,3]
try:
    print(L[5])
except IndexError:
    print("Index out of range!")
try:
    int("abc")
except Exception as e:
    print("An error occurred:", e)
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file was not found!")
except Exception as e: #generic exception handling
    print("An error occurred:", e.with_traceback)

#Finally and else block
#irrespective of whether an exception occurs or not, the finally block will always execute. 
# The else block will execute only if no exceptions are raised in the try block.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print("The result is:", result)
finally:
    print("This block will always execute, regardless of exceptions.")
#raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
try:    
    result = divide(10, 0)
    print("The result is:", result)
except ValueError as e:
    print("An error occurred:", e)

class Bank:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        return self.balance
try:
    my_bank = Bank(100)
    new_balance = my_bank.withdraw(150)
    print("New balance:", new_balance)
except ValueError as e:
    print("An error occurred:", e)
#custom exception:To done my task that our apllication demands
class SecurityError(Exception):
    def __init__(self, message="Invalid email or password!"):
        self.message = message
        super().__init__(self.message)
    def logout(self):
        return "You have been logged out due to security reasons."
class Google:
    def __init__(self, email,password,name,device):
        self.email = email
        self.password = password
        self.name = name
        self.device = device
    def login(self,email,password,device):
        if self.email != email or self.password != password:
            raise SecurityError("Hacker alert! Invalid email or password!")
        if self.device != device:
            raise ValueError("Unrecognized device!")
        return "Login successful!"
try:
    my_google = Google("nikhilbhati1827ai@gmail.com","Nikhil@123","Nikhil Bhati","Laptop")
    result = my_google.login("nikhilbhati1827i@gmail.com","Nikhil@123","Mobile")
    print(result)
except SecurityError as se:
    print("Security error:", se)
    print(se.logout())
except ValueError as ve:
    print("Value error:", ve)
finally:
    print("Login attempt completed.")

    