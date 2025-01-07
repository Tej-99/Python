'''
Arithmetic operators include 
+ , - , * , / , % , // , **
'''

# Addition operator
val1 = 2
val2 = 3
res = val1 + val2
print(res)

# subtraction operator
val1 = 2
val2 = 3
res = val1 - val2
print(res)

# multiplication operator
val1 = 2
val2 = 3
res = val1 * val2
print(res)

# division operator
val1 = 2
val2 = 3
res = val1 / val2
print(res) # o/p: 0.666

# floor division operator - (returns largest integer less than or equal to a given number)
# it effectively "rounds down" a floating point number to the nearest integer.
val1 = 2
val2 = 3
res = val1 // val2
print(res) # o/p: 0 

# ceil 
# "rounds up" to the nearest integer
import math
val1 = 2
val2 = 3
res = val1 / val2
print(math.ceil(res)) # o/p: 1

# modulus operator - gives the remainder 
val1 = 2
val2 = 3
res = val1 % val2
print(res) # o/p : 2

# exponential opeator - power (x^y)
val1 = 2
val2 = 3
res = val1 ** val2
print(res)  # o/p : 8


'''
PEMDAS/BODMAS
**               - right to left
%, *, /, //      - left to right
+, -             - left ot right
'''

'''
result = 3 + 2 * 2 ** 2 / 2 - 1  
# Explanation: 3 + ((2 * (2 ** 2)) / 2) - 1   # first exponent and follow left to right for (%, *, /, //)
#              3 + ((2 * 4) / 2) - 1
#              3 + (8 / 2) - 1
#              3 + 4 - 1  # and at last follow left to right for (+, -)
#              7 - 1
#              6.0
'''