'''
chaning comparision operators are used to check multiple conditions in a single expression

SYNTAX : a operator1 b operator2 c

it reurns boolean values : True or Flase

x < y <= z is equivalent to x < y and y <= z
'''

x = 5
print(1 < x < 10) #True
print(10 < x < 20) #False
print(x < 10 < x*10 < 100) #True
print(10 > x <= 9) #True
print(5 == x > 4)  #True

