# int
a = 10
print(type(a)) #<class'int'>


# float
f = 1.234
e = 1.2e3
print(type(f)) #<class'float'>
print(type(e)) #<class'float'>


# complex
# only j should be used for imaginary part instead of i
x = 10 + 20j
print(type(x)) #<class'complex'>
print(x.real)
print(x.imag)

# decimal form(base-10)
# it is a default number system in python (0-9)
dec = 10
print(dec)

# binary form(base-2)
# literal value should be prefixed with 0b or 0B (0,1)
bi = 0b1111   #15
bina = 0B101   #5
print(bi,bina)

# octal form(base-8)
# literal value should be prefixed with 0o or 0O (0-7)
oct = 0o1234567  #342391
print(oct)

# hexa decimal (base-16)
# literal value should be prefixed with 0x or 0X (0-9,a-f/A-F)
hex = 0x10   #16
hex1 = 0XFacE  #64206
print(hex,hex1)


# conversion are only for integral numbers
# bin()
print(bin(15)) #0b1111
print(bin(0xface)) #0b1111101011001110
print(bin(0o123)) #0b1010011

# hex()
# oct()
