'''
print() function prints the message to the screen or any other standard output device.
'''

print("hello world")

a = [1,2,'world']
print(a)


# syntax
'''
print(value(s),sep=' ',end="\n",file=file,flush=flush)
'''
'''
variables, strings, numbers or other data types can be passed as one or more parameters.
then these parameters are represented as strings by their respective str() function.
'''

planet = "earth"
place = 3

print("our home is",planet,"and it is",place,"rd planet in out solar system.")

# string literals
# \n
print("i am \nliving on the earth")
# "" prints empty line
print("")
print("new line")

# concatenate
print("dance "+"all "+"night") #need to add space if we want to separate the words
print("dance","all","night") #using , add space without specifying it.


# sep
'''
this print() function can accept any number of arugements.
to separate these positional arguments, the keyword "sep" is used
'''
a = 7
b= 12
c = 2024
print(a,b,c,sep='-')
# sep needs more than one argument
print("i'm from earth", sep='-') #this doesn't give you the output  "i'm-from-earth" as it is single argument


# end
'''
the end keyword is used to specify the content that is to be printed at the end of the execution of the print() function.
by default, it is set to "\n", which leads to the change of line after the execution of print() statement.
''' 
print("i'm earth")
print("my neighbours are mars", end='**')
print("and venus")

