# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

# Example
# If Statement
a = int(input("Enter The First Number: "))
b = int(input("Enter The Second Number: "))

if a > b:
    print(f"{a} Is Greater Than {b}.")

c = 222
d = 2222
if d>c:
    print(f"{d} Is Greater Than {c}.")

# How If Statements Work
# The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.

# Example
# Checking if a number is positive:

number = 15
if number > 0:
  print("The number is positive")

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
# Example
# If statement, without indentation (will raise an error):
# a = 33
# b = 200
# if b > a:
# print("b is greater than a") you will get an error


# Note: You can use spaces or tabs for indentation, but you must use the same amount of indentation for all statements within the same code block.

# Multiple Statements in If Block
# You can have multiple statements inside an if block. All statements must be indented at the same level.

# Example
# Multiple statements in an if block:
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

# Using Variables in Conditions
# Boolean variables can be used directly in if statements without comparison operators.

# Example
# Using a boolean variable:

is_logged_in = True
if is_logged_in:
  print("Welcome back!")