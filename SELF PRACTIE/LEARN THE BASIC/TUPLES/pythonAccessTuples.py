# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

fruits = ("Apple", "Banana", "Cherry", "Dragon Fruit", "Elderberry")

print(fruits[0])  # Output: Apple
print(fruits[1])  # Output: Banana

# Negative Indexing
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.
print(fruits[-1])  # Output: Elderberry

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
print(fruits[2:5])  # Output: ('Cherry', 'Dragon Fruit', 'Elderberry')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Example
# This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple1[:4])

# Example
# This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Range of Negative Indexes
print(thistuple[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

# Example
# Check if "apple" is present in the tuple:
thistuple3 = ("apple", "banana", "cherry")
if "apple" in thistuple3:
  print("Yes, 'apple' is in the fruits tuple")