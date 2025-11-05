file = open("new.txt", "w")
file.write("Hello, World!")
file.write("\nThis is a new file created using Python.")
file.close()

lines = ['Lumbini\n', 'ICT\n', 'Campus\n']
file = open("new.txt", "w")
file.writelines(lines)
file.close()

file = open("new.txt", "r")
content = file.read()
print(content)
file.close()

file = open("new.txt", "r")
line1 = file.readline()
line2 = file.readline()
lines3 = file.readlines()
print("Line1: ", line1)
print("Line2: ",line2)
print("Lines3: ", lines3)
file.close()

file = open("new.txt", "r+")
content = file.read()
print("Current Content:\n", content)
print(content)
# append new content
file.write("\nAppending new content to the file.")
file.seek(0)  # Move the cursor back to the beginning of the file
content = file.read()
print("Updated Content:\n")
print(content)
file.close()