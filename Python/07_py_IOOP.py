#classes consit of attributes and methods or function
#object is an instance of a class
#object=classname()
l=list()
l=[]#Using literal syntax
#Banking system
class Atm:
    #self is use to call the method or varible with in the class
    #self is object of the class
    #magic method __name__ is used to initialize the object
    def __init__(self):#constructor it is called when object is created
        #it is connect with database and fetch the data or connect with internet 
        self.balance=0
        self.pin=""
        self.create_pin()
        self.menu()
    #normal method
    def menu(self):
        print("1. Deposit")
        print("2. Change Pin")
        print("3. Check Balance")
        print("4. withdraw")
        print("5. Exit")
        n=int(input("Enter your choice: "))
        if n==1:
            self.deposit()
        elif n==2:
            self.change_pin()
        elif n==3:
            self.check_balance()
        elif n==4:
            self.withdraw()
        else:
            self.exit()
    def create_pin(self):# it the method to create pin and set balance
        self.pin=input("Enter your new pin: ")
        user_balance=int(input("Enter your balance: "))
        self.balance+=user_balance
        print("Pin created successfully")
        self.menu()
    def change_pin(self):
        old_pin=input("Enter your old pin: ")
        if old_pin==self.pin:
            new_pin=input("Enter your new pin: ")
            self.pin=new_pin
            print("Pin changed successfully")
        else:
            print("Incorrect pin")
        self.menu()
    def deposit(self):
        user_pin=input("Enter your pin: ")
        if user_pin==self.pin:
            amount=int(input("Enter the amount to deposit: "))
            self.balance+=amount
            print("Amount deposited successfully")
        else:
            print("Incorrect pin")
        self.menu()
    def withdraw(self):
        user_pin=input("Enter your pin: ")
        if user_pin==self.pin:
            amount=int(input("Enter the amount to withdraw: "))
            if amount<=self.balance:
                self.balance-=amount
                print("Amount withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect pin")
        self.menu()
    def check_balance(self):
        user_pin=input("Enter your pin: ")
        if user_pin==self.pin:
            print("Your balance is: ",self.balance)
        else:
            print("Incorrect pin")
        self.menu()
    
    def exit(self):
        print("Thank you for using the ATM")       
        
obj=Atm()#object creation
#Creating a Fraction class to perform basic arithmetic operations
class Fraction:
    def __init__(self,x=1,y=2):#parameterized constructor
        self.num=x
        self.den=y
    def __str__(self):#magic method to display the fraction
        return str(self.num)+"/"+str(self.den)
    def __add__(self,other):
        num=self.num*other.den+other.num*self.den
        den=self.den*other.den
        return Fraction(num,den)
    def __sub__(self,other):
        num=self.num*other.den-other.num*self.den
        den=self.den*other.den
        return Fraction(num,den)
    def __mul__(self,other):
        num=self.num*other.num
        den=self.den*other.den
        return Fraction(num,den)
    def __truediv__(self,other):
        num=self.num*other.den
        den=self.den*other.num
        return Fraction(num,den)
f1=Fraction(1,2) 
print("Fraction 1: ",f1)
f2=Fraction(3,4)
print("Fraction 2: ",f2)
f3=f1+f2
print("Addition: ",f3)
f4=f1-f2
print("Subtraction: ",f4)
f5=f1*f2
print("Multiplication: ",f5)
f6=f1/f2
print("Division: ",f6)
#Creating 2d coordinate class to perform basic arithmetic operations
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def distance_from_orign(self):
        return (self.x**2 + self.y**2) ** 0.5
    def distance_from_point(self,other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2) ** 0.5
class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
    def __str__(self):
        return str(self.A)+"x + "+str(self.B)+"y + "+str(self.C)+" = 0"
    def point_on_line(self,point):
        if  self.A*point.x + self.B*point.y + self.C == 0:
            return True
        else:
            return False
    def distance_from_point(self,point):
        return abs(self.A*point.x + self.B*point.y + self.C) / (self.A**2 + self.B**2) ** 0.5

        

p1=Point(3,4)
print("Point 1: ",p1)
print("Distance from origin: ",p1.distance_from_orign())
p2=Point(6,8)
print("Point 2: ",p2)
print("Distance from point 1: ",p1.distance_from_point(p2))
l=Line(1,2,3)
print("Line: ",l)
print("Is point 1 on line? ",l.point_on_line(p1))
print("Distance from point 1 to line: ",l.distance_from_point(p1))

#Refernce variable is a variable that refers to the same object in memory
class A:
    def __init__(self,x):
        self.x=x
a1=A(10)
a2=a1#a2 is reference variable that refers to the same object in memory as a1
print(a1.x)
print(a2.x)
#change the value of x using a2
a2.x=20
print(a1.x)
#Pass by reference
class B:
    def __init__(self,x):
        self.x=x#instance variable
def change_value(b):
    b.x=30
    print("Value changed to: ",b.x)
b1=B(10)
print(b1.x)
change_value(b1)
#Abstraction is the process of hiding the implementation details and showing only the functionality to the user
#Encapsulation is the process of wrapping the data and the code that manipulates the data into a single unit
#Inheritance is the process of creating a new class from an existing class
#Polymorphism is the process of using a single interface to represent different types of data
#----------------Encapsulation----------------
class Car:
    #private variable
    def __init__(self,make,model):
        self.make=make
        self.model=model
        self.__speed=0#private variable name=>_Car__speed
car1=Car("Toyota","Camry")
car1.__speed=100#it will not change the value of speed because it is private variable
#Getter and setter method to access the private variable
class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
        self.__speed=0
    def get_speed(self):
        return self.__speed
    def set_speed(self,speed):
        if speed>=0:
            self.__speed=speed
        else:
            print("Speed cannot be negative")
#collection of objects is called data structure
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age    
s1=Student("John",20)
s2=Student("Jane",21)
students=[s1,s2]#list of objects
print(students)
for student in students:
    print("Name: ",student.name)
    print("Age: ",student.age)  
#static variable is a variable that is shared among all the objects of a class
class Employee:
    Emp_id=0 #static variable
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Employee.Emp_id+=1#incrementing the value of static variable
e1=Employee("John",30)
print(e1.Emp_id)
e2=Employee("Jane",25)
print(e2.Emp_id)
Employee.Emp_id=100#changing the value of static variable
#-----------------Inheritance----------------
#Aggregation is a special form of association where the objects have a has-a relationship
class Engine:
    def __init__(self,horsepower):
        #self.horsepower=horsepower
        self.__horsepower=horsepower#private variable
    def get_horsepower(self):
        return self.__horsepower
    
class Car:
    def __init__(self,make,model,engine):
        self.make=make
        self.model=model
        self.engine=engine#has-a relationship
engine1=Engine(200)
car1=Car("Toyota","Camry",engine1)
print("Car: ",car1.make,car1.model)
print("Engine horsepower: ",car1.engine.get_horsepower())
#inheritance is a process of creating a new class from an existing class
#udemy course
#parent class
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def display(self):
        print("Name: ",self.name)
        print("Email: ",self.email)
    def login(self):
        print(self.name,"logged in")
#child class
class Admin(User):  
    def __init__(self,name,email,admin_level):
        super().__init__(name,email)#calling the constructor of parent class
        self.admin_level=admin_level
    def display(self):
        super().display()#calling the display method of parent class
        print("Admin Level: ",self.admin_level)
#child class
class Student(User):
    def __init__(self,name,email,visit_count):
        super().__init__(name,email)
        self.visit_count=visit_count
    def display(self):
        super().display()
        print("Visit Count: ",self.visit_count)
admin1=Admin("John","jon123@gmail.com",1)
student1=Student("Jane","jane123@gmail.com",5)
admin1.display()
student1.display()
# pirvate methods and variables are not inherited by child class but we can access them using getter and setter method
#method overriding
class User:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print("Name: ",self.name)
        print("ID: ",self.id)
class Admin(User):
    def display(self):
        print("Admin Level: ",self.admin_level)
        super().display()#calling the display method of parent class
admin1=Admin("John",123)
admin1.admin_level=1
admin1.display()
#Super Keyword
class A:
    def __init__(self,x):
        self.x=x
    def display(self):
        print("Value of x: ",self.x)
class B(A):
    def __init__(self,x,y):
        super().__init__(x)#calling the constructor of parent class
        self.y=y
    def display(self):
        print("Value of y: ",self.y)
        super().display()#calling the display method of parent class
b1=B(10,20)
b1.display()
#type of inheritance
#Single Inheritance is a type of inheritance where a child class inherits from a single parent class
#Multilevel Inheritance
class A:
    def __init__(self,x):
        self.x=x
    def display(self):
        print("Value of x: ",self.x)
class B(A):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def display(self):
        print("Value of y: ",self.y)
        super().display()
class C(B):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
    def display(self):
        print("Value of z: ",self.z)
        super().display()
c1=C(10,20,30)
c1.display()
#Heirarchical Inheritance
class A:
    def __init__(self,x):
        self.x=x
    def display(self):
        print("Value of x: ",self.x)
class B(A): 
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def display(self):
        print("Value of y: ",self.y)
        super().display()
class C(A):
    def __init__(self,x,z):
        super().__init__(x)
        self.z=z
    def display(self):
        print("Value of z: ",self.z)
        super().display()       
b1=B(10,20)
c1=C(10,30)
b1.display()
c1.display()
#Multiple Inheritance
class A:
    def __init__(self,x):
        self.x=x
    def display(self):
        print("Value of x: ",self.x)
class B:
    def __init__(self,y):
        self.y=y
    def display(self):
        print("Value of y: ",self.y)
class C(A,B):
    def __init__(self,x,y,z):
        A.__init__(self,x)
        B.__init__(self,y)
        self.z=z
    def display(self):
        print("Value of z: ",self.z)
        A.display(self)
        B.display(self)
c1=C(10,20,30)
c1.display()
#daimond problem
class A:
    def __init__(self,x):
        self.x=x
    def display(self):
        print("Value of x: ",self.x)

class C:
    def __init__(self,z):
        self.z=z
    def display(self):
        print("Value of z: ",self.z)
class B(A,C):
    pass
b1=B(10,20)
b1.display()#it will give error because it is not clear which display method to call
#------------------Polymorphism----------------
#method overloading is a process of defining multiple methods with the same name but different parameters
class A:
    def display(self,x):
        print("Value of x: ",x)
    def display(self,x,y):
        print("Value of x: ",x)
        print("Value of y: ",y)
#------------------Abstraction------------------
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2

