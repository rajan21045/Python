'''
Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:
'''
myDict = {
    "name": "Rajan Poudel",
    "age": 25,
    "country": "Nepal",
    "city": "Gaindakor"
}

x = myDict["name"]
print(x)

# There is also a method called get() that will give you the same result:
age = myDict.get("age")
print(age)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
keys = myDict.keys()
print(keys)


# Get Values
# The values() method will return a list of all the values in the dictionary
values = myDict.values()
print(values)

myDict["age"] = 21
print(values)

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
items = myDict.items()
print(items)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")