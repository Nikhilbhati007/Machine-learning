'''
#Lists
L=[1,1.45,[1,2,3],(1,2),{1: 'one', 2: 'two'},'Python']
#creating a list
print(L)
#accessing list elements
L[0] #1
L[2] #[1, 2, 3]
L[2][1] #2
L[4][1] #'two'
#list slicing
L[0:3] #[1, 1.45, [1, 2, 3]]
L[3:5] #[(1, 2), {1: 'one', 2: 'two'}]
L[:4] #[1, 1.45, [1, 2, 3], (1, 2)]
#appending elements to a list
L.append('New Element')
print(L)
#inserting elements at a specific index
L.insert(2, 'Inserted Element')
print(L)
#extending a list with another list
L.extend([10, 20, 30])
print(L)

#removing elements from a list
L.remove(1.45)
print(L)
#popping an element from a specific index
L.pop(2)
print(L)
#clearing all elements from the list
L.clear()
print(L)

#List methods
my_list = [3, 1, 4, 1, 5]
n=len(my_list)
min_value = min(my_list)
max_value = max(my_list)
my_list.sort()#sorts the list in place
print(my_list)
sorted_list = sorted(my_list) #returns a new sorted list
my_list.reverse()
print(my_list)
my_list.append(9)
print(my_list)
my_list.insert(2, 2)
print(my_list)
my_list.remove(1)
print(my_list)
my_list.pop()
print(my_list)
my_list.clear()
print(my_list)
'''
#List comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)
#Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)
#Zip function
list1 = [1, 2, 3]
list2 = [1, 7, 9]
zipped = zip(list1, list2)
l=[i+j for i,j in zipped]
print(l)