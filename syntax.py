'''
syntax refers to the set of rules that defines how to write and organize code so that the python interpreter can understand and run it correctly.
'''


# indentation
'''
indentation refers to the use of whitespace at the beginning of the codeline.
it is used to define the code blocks.
'''
if 10 > 5:
    print("This is true!")
    print("indentation")
  
print("no indentation")  


# variables
'''
variables are essentially named references pointing to objects in memory.
no need of declaring data type to the variable as python dynamically determine the type.
'''
a = 10
print(type(a)) #<class 'int'>
b = 'python'
print(type(b)) #<class 'str'>


# identifiers
'''
identifiers are unique names that are assigned to variables, functions, classes and other entites.
they should start with a letter(a-z,A-Z) or an underscore(_) and followed by letters, numbers or underscores.
'''
first_name = "tony"
last_name = "stark"


# keywords
'''
keywords are reserved words that have special meaning and specific purpose in the language syntax.
they can't be used as indetifiers.
there are 33 reserved/keywords in python
'''
import keyword
print(keyword.kwlist,end='')

# for kword in keyword.kwlist:
#     print(kword,end=' ')  #using sep = '-' doesn't give False-None...output because we only passed one argument instead use
#     print(kword,end = '-')


# comments
'''
The purpose of comments is to explain the working of a code, they have no impact on the execution or outcome of a program.
'''
print("\n")

# multi line statements
# using backslash(\) (explicit continuation)
sentence = "this is a very long sentence that we want to "\
            "split over mutiple lines for better readability"
print(sentence)    

total = 1 + 2 + 3 + \
        4 + 5 + 6 + \
        7 + 8 + 9
print(total)                


# implicit continuation
# Line continuation within square brackets '[]'
numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

print(numbers)