"""
Set
Sets are used to store multiple items in a single variable.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.
"""
#Sets are written with curly brackets.
#Example
#Create a Set:

newSet = {"Rajan", "Ashok", "Sasin", "Prabin", "Anuz"}
print(newSet)

"""
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.
"""

# Get the Length of a Set
# To determine how many items a set has, use the len() function.

# Example
# Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}
print(f"Number of items in the set: {len(thisset)}")

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Set 3: {set3}")


myset2 = {"apple", "banana", "cherry"}
print(type(myset2))