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
#with statement
#it close the file automatically after the block of code is executed
with open("myfile.txt", "a") as f:
    f.write("This is an appended line using with statement.\n")
with open("myfile.txt", "r") as f:
    content = f.read()
    print(content)
#benefits of with statement
big_list = ['hello' for i in range(1000000)]
with open("bigfile.txt", "w") as f:
    for item in big_list:
        f.write(item + "\n")
with open("bigfile.txt", "r") as f:
    chunk_size = 1000
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        print(chunk, end="")
#seek and tell

with open("myfile.txt", "r") as f:
    print(f.tell()) #This will give the current position of the file pointer
    content = f.read(10)
    print(content)
    print(f.tell()) #This will give the current position of the file pointer
    f.seek(0) #This will move the file pointer to the beginning of the file
    print(f.tell()) #This will give the current position of the file pointer
#Binary file
with open("myfile.txt", "rb") as f:
    content = f.read()
    print(content)
#serialization and deserialization
#serialization:converting a Python object into a byte stream(JSON, XML, etc.)
import json
data = {"name": "John", "age": 30, "city": "New York"}
with open("data.json", "w") as f:
    json.dump(data, f)
#deserialization:converting a byte stream(JSON) back into a Python object
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data)
#in tuple
data_tuple = ("John", 30, "New York")
with open("data_tuple.json", "w") as f:
    json.dump(data_tuple, f)
with open("data_tuple.json", "r") as f:
    loaded_data_tuple = json.load(f)
    print(loaded_data_tuple)
'''
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    @property
    def show_object(self):
        return {"name": self.name, "age": self.age, "city": self.city}  
import json
with open("person.json", "w") as f:
    person = Person("John", 30, "New York")
    json.dump(person.show_object, f)
with open("person.json", "r") as f:
    loaded_person_dict = json.load(f)
    loaded_person = Person(**loaded_person_dict)
    print(loaded_person.name, loaded_person.age, loaded_person.city)
#pickle module
import pickle
with open("person.pkl", "wb") as f:
    person = Person("John", 30, "New York")
    pickle.dump(person, f)
with open("person.pkl", "rb") as f:
    loaded_person_pickle = pickle.load(f)
    print(loaded_person_pickle.name, loaded_person_pickle.age, loaded_person_pickle.city)