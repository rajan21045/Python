# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
friendNames  = {"Rajan", "Ashok", "Sasin", "Prabin", "Anuz"}
print("The set named friendNames contains the following names:")
for x in friendNames:
  print(x)

print("\n")
# Check if "Sasin" is present in the set:
if "Sasin" in friendNames:
    print("Sasin is in the set friendNames")

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
