txt = "Rajan Poudel. I Love Programming."

print(txt.upper())
# prints the string in uppercase letters
# Output: RAJAN POUDEL. I LOVE PROGRAMMING.

print(txt.lower())
# prints the string in lowercase letters
# Output: rajan poudel. i love programming.

# REMOVE WHITESPACES
# strip()
print(txt.strip())
# removes any whitespace from the beginning or the end
# Output: "Rajan Poudel. I Love Programming."

# replace()
print(txt.replace("Rajan", "Sita"))
# replaces a string with another string
# Output: Sita Poudel. I Love Programming.

# split()
print(txt.split("."))
# splits the string into a list
# Output: ['Rajan Poudel', ' I Love Programming', '']

print(txt.capitalize())
# capitalizes the first letter of the string
# Output: Rajan poudel. i love programming.

