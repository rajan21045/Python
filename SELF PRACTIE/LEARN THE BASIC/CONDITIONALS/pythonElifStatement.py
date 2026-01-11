# The Elif Keyword
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
# In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".

# Multiple Elif Statements
# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.
mark = 75
if mark >=90:
  print("Grade: A")
elif mark >=80:
  print("Grade: B")
elif mark>=70:
  print("Grade: C")
elif mark >= 60:
  print("Grade: D")
# In this example, the program checks each condition in order. Since mark is 75, it prints "Grade: C" (the first condition that evaluates to true).

# How Elif Works
# When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.
# Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.

# Example
# Categorizing age groups:
age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

# When to Use Elif
# Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.

# Example
# Day of the week checker:
day = 3
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")