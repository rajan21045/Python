b = "Hello World"
print(b[2:5])  
# prints characters from index 2 to 4
# output: llo

print(b[:5])
# prints characters from the beginning to index 4
# output: Hello

print(b[2:])
# prints characters from index 2 to the end
# output: llo World

# Using negative indexing
print(b[-5:-2])
# prints characters from index -5 to -3
# output: Wor

print(b[-5:])
# prints the last 5 characters
# output: World

print(b[:-2])
# prints all characters except the last 2
# output: Hello Wor

# revering the string
print(b[::-1])
# prints the string in reverse order
# output: dlroW olleH