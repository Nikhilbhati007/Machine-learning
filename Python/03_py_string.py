
#Sum of series :1/1! + 1/2! + 1/3! + 1/4! + 1/5!
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n=int(input("Enter the number of terms: "))
sum_series = 0
i=1
while i<=n:
    sum_series += 1/factorial(i)
    i+=1
print("Sum of the series is:", sum_series)
#Pattern Printing
n=int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
#Question 2
n=int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    for k in range(i-1,0,-1):
        print(k, end=' ')
    print()
#loop control statement
#Break
for i in range(1, 11):
    if i == 5:
        break
    print(i)
#Continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
#pass
for i in range(1, 11):
    if i == 5:
        pass
    print(i)
#strings
#creation
str1 = "Hello, World!"
str2 = "'Python' Programming"
print(str1)
print(str2)
#string indexing
str1[0] #H
str1[7] #W
str1[-1] #!
str1[-6] #W
#string slicing 
str1[0:] #Hello World!
str1[:12] #Hello World  
str1[7:12] #World
str1[::2] #Hlo ol!
str1[1::2] #el,Wrd 
print(str1[::-1]) #revese string !dlroW ,olleH
#String in python are immutable
del str1 #This will raise an error as str1 is deleted
#operations on string
str3 = "Hello"
str4 = "World"
#Concatenation
str5 = str3 + " " + str4
print(str5) #Hello World
#Repetition
str6 = str3 * 3
print(str6) #HelloHelloHello
#Membership
print('H' in str3) #True
print('h' in str3) #False
print('W' not in str3) #True
#comparison
print(str3 == str4) #False
print(str3 != str4) #True
#logical operators
print(str3 == "Hello" and str4 == "World") #True
print(str3 == "Hello" or str4 == "Python") #True

#String methods
str7 = "  Hello, World!  "
print(str7.strip()) #Hello, World!
print(str7.lower()) #  hello, world!
print(str7.upper()) #  HELLO, WORLD!
print(str7.replace("Hello", "Hi")) #  Hi, World!
print(str7.split()) #['Hello,', 'World!']
print(str7.join(['Hello', 'World'])) #HelloHello, World!Hello
#string Function
str8 = "Python Programming"
print(len(str8)) #18
print(str8.count('o')) #2
print(str8.find('Programming')) #7
print(str8.startswith('Python')) #True
print(str8.endswith('Programming')) #True
print(max(str8)) #y
print(min(str8)) #
print(sorted(str8)) #False
#formatted string
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.") #My name is Alice and I am 30 years old.
print("My name is {} and I am {} years old.".format(name, age)) #My name is Alice and I am 30 years old.
