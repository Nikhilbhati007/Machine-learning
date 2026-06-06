
#operators
a = 10 # Assignment operator
# Arithmetic operators
x = 5
y = 3
print("Addition:", x + y)        # Output: 8    
print("Subtraction:", x - y)     # Output: 2
print("Multiplication:", x * y)  # Output: 15
print("Division:", x / y)        # Output: 1.666666666666
print("Floor Division:", x // y) # Output: 1
print("Modulus:", x % y)         # Output: 2
print("Exponentiation:", x ** y) # Output: 125
# Comparison operators
print("Equal to:", x == y)       # Output: False
print("Not equal to:", x != y)   # Output: True
print("Greater than:", x > y)    # Output: True
#logical operators
a = True
b = False
print("Logical AND:", a and b)  # Output: False
print("Logical OR:", a or b)    # Output: True
print("Logical NOT:", not a)     # Output: False
#Bitwise operators
x = 5  # In binary: 0101
y = 3  # In binary: 0011
print("Bitwise AND:", x & y)  # Output: 1 (In binary: 0001)
print("Bitwise OR:", x | y)   # Output: 7 (In binary
print("Bitwise XOR:", x ^ y)  # Output: 6 (In binary: 0110)
print("Bitwise NOT:", ~x)      # Output: -6 (In binary:
#memebership operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in the list?", 3 in my_list)   # Output: True
print("Is 6 in the list?", 6 in my_list)   # Output: False
print("Is 3 not in the list?", 3 not in my_list)   # Output: False
print("Is 6 not in the list?", 6 not in my_list)   # Output: True
#Program 1
num=int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit
    temp//=10#temp=temp//10
print("The sum of the digits is:", sum) 
#if-else
num=int(input("Enter a number: "))
if num%2==0:
    print("The number is even.")
elif num%2!=0:
    print("The number is odd.")
else:
    print("The number is invalid.")

#Module in Python
#math module
import math
print("Square root of 16:", math.sqrt(16))  # Output: 4.0
print("Value of pi:", math.pi)  # Output: 3.141592653589793
#keyword Module
import keyword
print("Python keywords:", keyword.kwlist) 
#random module
import random
print("Random integer between 1 and 10:", random.randint(1, 10))
#datetime module
import datetime
now = datetime.datetime.now()
print("Current date and time:", now)

#loop
#for loop
for i in range(5):
    print("Iteration:", i)
#while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1
#while with else
count = 0
while count < 5:
    print("Count:", count)
    count += 1
else:
    print("Loop finished.")
