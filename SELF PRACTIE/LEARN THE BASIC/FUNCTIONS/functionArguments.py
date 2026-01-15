def my_function(fname):
    print(f"Hello {fname}")

my_function("Rajan")
my_function("Prabin")
my_function("Ujjwal")


# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# Number of Arguments
# By default, a function must be called with the correct number of arguments.
# If your function expects 2 arguments, you must call it with exactly 2 arguments.

# Example
# This function expects 2 arguments, and gets 2 arguments::
def hh(fname, lname):
   print(f"Hello {fname} {lname}")

hh("Rajan", "Poudel")


# Keyword Arguments
# You can send arguments with the key = value syntax.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.
# However, positional arguments must come before keyword arguments:

# Example
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)