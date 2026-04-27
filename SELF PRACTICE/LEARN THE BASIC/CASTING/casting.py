# Specify a Variable Type
# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

# Floats
num1 = 10
convertedNum = float(num1)
print(convertedNum)
x1 = float(1)     # x1 will be 1.0
y1 = float(2.8)   # y1 will be 2.8
z1 = float("3")   # z1 will be 3.0
w1 = float("4.2") # w1 will be 4.2
print(x1, y1, z1, w1)

# Integers:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x, y, z)

# Strings:
x2 = str("s1") # x2 will be 's1'
y2 = str(2)    # y2 will be '2'
z2 = str(3.0)  # z2 will be '3.0'
print(x2, y2, z2)