'''
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
'''

    