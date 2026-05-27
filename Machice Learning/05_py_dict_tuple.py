#Tuples
#creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
#accessing elements in a tuple
#indexing
print(my_tuple[0]) #Output: 1
print(my_tuple[1]) #Output: 2
print(my_tuple[2]) #Output: 3
#s1licing
print(my_tuple[1:4]) #Output: (2, 3, 4)
#tuples are immutable
#my_tuple[0] = 10 #This will raise an error
#operation and methods
#concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple) #Output: (1, 2, 3, 4, 5, 6)
#repetition
repeated_tuple = tuple1 * 2
print(repeated_tuple) #Output: (1, 2, 3, 1, 2, 3)
#length of a tuple
print(len(my_tuple)) #Output: 5
#counting occurrences
print(my_tuple.count(2)) #Output: 1
#index of an element
print(my_tuple.index(3)) #Output: 2
#--------------------------------DICTIONARIES
#dictionaries are unordered collections of key-value pairs
#keys must be unique and immutable, while values can be of any data type
#creating a dictionary
#1-D dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict)
#2-D dictionary
my_dict_2d = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25}
}
print(my_dict_2d)
#accessing values in a dictionary       
print(my_dict['name']) #Output: Alice
print(my_dict['age']) #Output: 30
print(my_dict['city']) #Output: New York
#adding a new key-value pair
my_dict['country'] = 'USA'
print(my_dict) #Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
#updating a value
my_dict['age'] = 31
print(my_dict) #Output: {'name': 'Alice', 'age': 31,
#'city': 'New York', 'country': 'USA'}
#Adding a new key-value pair
my_dict['country'] = 'USA'
#pop method to remove a key-value pair and return the value
removed_value = my_dict.pop('city')
print(removed_value) #Output: New York
#popitem method to remove and return an arbitrary key-value pair
removed_item = my_dict.popitem()
print(removed_item) #Output: ('country', 'USA') 
#clearing a dictionary
#deleting a key-value pair
del my_dict['city'] 
print(my_dict) #Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

#dictionary methods
#keys
print(my_dict.keys()) #Output: dict_keys(['name', 'age', 'country'])
#values
print(my_dict.values()) #Output: dict_values(['Alice', 31, 'USA'])
#items
print(my_dict.items()) #Output: dict_items([('name', 'Alice'), ('age', 31), ('country', 'USA')])
#dictionary comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict) #Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#---------------------------------Set
#sets are unordered collections of unique elements
#creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)
#adding an element to a set
my_set.add(6)
print(my_set) #Output: {1, 2, 3, 4, 5, 6}
#removing an element from a set
my_set.remove(3)
print(my_set) #Output: {1, 2, 4, 5, 6}
#set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
#union
union_set = set1.union(set2) #s1 | s2
print(union_set) #Output: {1, 2, 3, 4, 5}
#intersection
intersection_set = set1.intersection(set2)#s1 & s2
print(intersection_set) #Output: {3}
#difference
difference_set = set1.difference(set2) #s1 - s2
print(difference_set) #Output: {1, 2}
#symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2) #s1 ^ s2
print(symmetric_difference_set) #Output: {1, 2, 4, 5}
#frozen set
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set) #Output: frozenset({1, 2, 3, 4, 5})
#it is immutable and does not support add or remove operations
#all Read fuction will work else it will raise an error.
#2D frozenset
frozen_set_2d = frozenset([(1, 2), (3, 4), (5, 6)])
print(frozen_set_2d) #Output: frozenset({(1, 2), (3, 4), (5, 6)})
