'''
string is a sequence of characters.python treats anything inside quotes as a string.
'''

s = 'earth'
print(s)


# creating a string
'''
strings can be created using either single or double quotes
'''
s1 = 'home'
s2 = "sweet home"
print(s1)
print(s2)

# multi line strings
s3 = '''pick a petal
off a flower
'''  #this prints an empty line after s3 as there's whitespace after flower and ''' in a new line.
s4 = """when i said
will be back"""
print(s3)
print(s4)


# accessing characters
'''
strings in python are sequence of characters, so we can access individual characters using indexing.
 e  a  r  t  h
 0  1  2  3  4
-5 -4 -3 -2 -1    
'''
s = "Solar System"
print(s[0]) #accessing first character
print(s[5]) #accessing 6th character space will be printed as the 6th character is space
print(s[-1]) #accessing last element using neagtive referencing
'''
accessing out of range causes 'IndexError'
'''


# slicing
'''
slicing is a way to extract portion of a string by specifying the start and end indexes.

string[start:end:step]
'''
s = "PeanutButter and Tears"
print(s[1:12]) 
print(s[:12])
print(s[13:])
print(s[::-1]) #reversing a string using -1 as step


# strings are immutable
s = "white ferrari"
# s[0] = 'W' 
# print(s)  #gives typeError as we can't change the string after they are created
s = 'W' + s[1:]
print(s)


# deleting a string
a = 'astronomy'
del a
# print(a) #it gives NameError as we deleted variable a


# updating a string
s = "hello world"
# updating by creating a new string
s1 = 'H' + s[1:]
# replacing "world" with "stranger"
s2 = s.replace("world","stranger")
print(s)
print(s1)
print(s2)


#string methods
# 1.len() it return the total number of characters in a string
s = "peaceminusone"
print(len(s)) #13

# 2. upper() it converts all the characters to uppercase
# 3. lower() it converts all the characters to lowercase
s = "Snow At The Beach"
print(s.upper()) #SNOW AT THE BEACH
print(s.lower()) #snow at the beach

# 4.strip() removes the leading and triling whitespaces from the string
# 5.replace(old,new) replaces all the occurrences of the specified substring with another
s = "   hey   "
s = s.strip()
print(s) #hey
print(s.replace('y','r')) #her

# we can concatenate strings using +operator and repeat them using *operator
s1 = "pink"
s2 = "white"
print ( s1+"+"+s2)

s = "$"
print(s*3)


# formatting using f-string
name = 'earth'
place = 3
print(f'Name: {name}, Place:{place}')


# using in for string membership testing
s = 'peaceminusone'
print("peace" in s) #True
print("Peace" in s) #False as python is case sensitive


# count() returns the number of times a specified substring appears in a string.
# string.count("substring",start,end)
s = "hello world"
print(s.count('o'))
print(s.count("o",0,5))


# find() returns the index of the first occurrence of a substring within a given string.
# if the substring is not found, it returns -1.
# string.find("substring",start,end)
s = "abcabcabc"
print(s.find('c')) #2
print(s.find('c',3,len(s))) #5
# we can use index() but it raises ValueError if not found