'''
logical operators are used to combine conditional statements, allowing you to perform operations based on multiple conditions.
'''
# Truth Table
''' 
x     Y      X and Y    X or Y    not(X)     not(Y)

T     T        T          T        F          F
T     F        F          T        F          T
F     T        F          T        T          F
F     F        F          F        T          T

'''

'''
no value or 0 is considered as False
any value other than 0 is considered as True
'''

# AND 
'''
boolean and operator returns True if both the operands are True else it returns False
'''
# in AND operator if the first expression is evaluates to be False, then the further expression is not evaluated.
a = 10
b = 10
c = -10
if a > 0 and b > 0 :
    print("The numbers are greater than 0")
if a > 0  and b > 0 and c > 0 :
    print("The numbers are greater than 0") 
else:
    print("Atleast one number is not greater than 0")
    
    
# OR
'''
The Boolean OR operator returns True if either of the operands is True.
'''
# if the first expression is evaluated to be True,then the further expressions are not evaluated.
a = 10
b = -10
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
    

# NOT
'''
The Boolean NOT operator works with a single boolean value. If the boolean value is True it returns False and vice-versa.
''' 
a = 10

if not a:
    print("Boolean value of a is True")  # this won't be evaluated as (a) is True and (not a) is False 
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5") #this won't be evaluated as the expression inside the parathesis is True but as there's not operator it will become False
else:
    print("10 is divisible by either 3 or 5") 
    