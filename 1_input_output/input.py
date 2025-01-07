val = input()
print("the value is",val)
'''
whatever you enter as input, the input function converts it into a string.
'''

# multiple inputs
'''
.split() method splits the string based on whitespace
'''
x,y,z = input("enter the numbers: ").split()
print(x)
print(y)
print(z)

# map()
'''
map() function is used to apply a given function to every item of an iterable, such as list or tuple and returns a map object. 
'''
a = map(int,input().split())
b= list(a)
print(a)

# we can specify multiple variables in the same line
a = 10; b = 20; c = 0
print(a,b,c)