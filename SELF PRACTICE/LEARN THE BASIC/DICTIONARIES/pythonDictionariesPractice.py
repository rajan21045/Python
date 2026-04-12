'''
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("Printing Dictionaries: ")
print(thisdict)



'''
Dictionary Items
Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
'''
print()
print("Dictionaries Items: ")
print(thisdict["brand"])


'''
Dictionary Length
To determine how many items a dictionary has, use the len() function:
'''
print(f"Length of the thisdict dictionary is {len(thisdict)}")

# Dictionary Items - Data Types
print(type(thisdict))

thisdict2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict2)