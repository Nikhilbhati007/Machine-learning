'''
#Text file
#If file is not created then it will be created
f = open("myfile.txt", "w")
f.write("Hello World")
f.close()
#f.write("Hello World") #This will give error because file is closed
#Write multiple lines
f = open("myfile.txt", "w")
lines = ["Hello World\n", "Welcome to Python\n", "File Handling\n"]
f.writelines(lines)
f.close()
#how exactly open() works
#open() is a built-in function in Python that is used to open a file and return
#intro to append mode
f = open("myfile.txt", "a")
f.write("This is an appended line.\n")
f.close()
#Read file
f = open("myfile.txt", "r")
#content = f.read()
content=f.read(10) #This will read next 10 characters
print(content)
f.close()
#Read file line by line
f = open("myfile.txt", "r")
for line in f:
    print(line, end="")
f.close()   
#readlines() method
f = open("myfile.txt", "r")
lines = f.readlines()
print(lines)
print(f.readline())
f.close()
'''
#with statement
#it close the file automatically after the block of code is executed
with open("myfile.txt", "a") as f:
    f.write("This is an appended line using with statement.\n")
with open("myfile.txt", "r") as f:
    content = f.read()
    print(content)
    
