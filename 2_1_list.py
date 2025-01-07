'''
list is a built in dynamic sized array that is used to store an ordered collection of items.
*If we want to represnt a group of values as a single entity where insertion order required to preserve and duplicates are allowed then we should go for the list data type*
'''
# creating a list
# list of integers
a = [1,2,3,4,5]
#  list of strings
b = ['apple','mango','cherry']
# mixed data types
c = [1,'hello',3.14,True]
print(a)
print(b)
print(c)

# using the list() constructor
'''
we can also create a list by passing an iterable (like a string, tuple, or another list) to the list() function.
'''
a = list((1,2,3,'apple',4.5))
print(a)
a = list('apple')
print(a) #this gives the output as ['a', 'p', 'p', 'l', 'e']

# creating a list with repeated elements
a = [2] * 5
b = [0] * 7
print(a)
print(b)

# accessing list elements
a = [10,20,30,40,50]
print(a[0]) #first element 10
print(b[-1]) #last element 50

# adding elements into list
'''
append - adds an element at the end of the list.
extend - adds multiple elements to the end of the list
insert(index,value) - adds an element at a specific position
'''
# Initializing an empty list
a = []
a.append(10)  #adding 10 to the end of the list
print(a)
a.insert(0,'apple') #inserting apple at the index 0
print(a)
a.extend([15,20,50])
print(a)

# updating elements into list
a = [10,20,30,40,50]
a[1] = 25 #changing the second element
print(a)

# removing elements from list
'''
remove : removes the first occurrence of an element
pop : removes the element at a specific index or the last element if no index is specified.
del statement : deletes an element at a specifeid index.
'''
a = [10,20,30,40,50]
# removing the first occurenece of 30
a.remove(30)
print("after remove(30):",a)
# removes the element at index 1
popped_val = a.pop(1)
print("popped element:",popped_val)
print("after pop(1):",a)
# deletes the first element
del a[0]
print("after del a[0]:",a)


# iterating over lists
a = ['apple','banana','cherry']
for item in a:
    print(item, end = ' ')    

print()

# nested lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# accessing element at row 3, coumn 2
print(matrix[2][1])


# multi dimensional list
'''
accessing a multi dimensional list
'''
# approach 1
a = [[2,4,6,8,10],[3,6,9,12,15],[4,8,12,16,20]]
print(a)

# approach 2
a = [[2,4,6,8,10],[3,6,9,12,15],[4,8,12,16,20]]
for record in a:
    print(record)

# approach 3
a = [
    [2,4,6,8,10],
    [1,3,5,7,9],
    [8,6,4,2,0],
    [7,5,3,1,0]
]
# print(len(a))
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end =' ')
    print() 
 