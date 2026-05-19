# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# Example
# Sort the list alphabetically:
myAlphaList = ["Ram", "Shyam", "Hari", "Ashok", "Anuj"]
print(f"The Original Alphabetically List Is {myAlphaList}")
myAlphaList.sort()
print(f"The Ascending Sorted Alphabetically List Is {myAlphaList}")
print()

# Example
# Sort the list numerically:
myNumericList = [1, 4, 2, 5, 3]
print(f"The Original Numerically List Is {myNumericList}")
myNumericList.sort()
print(f"The Ascending Sorted Numerically List Is {myNumericList}")
print()




# Sort Descending
# To sort descending, use the keyword argument reverse = True:

# Example
# Sort the list descending:
myNumericList.sort(reverse= True)
myAlphaList.sort(reverse= True)
print(f"The Descending Numerically List Is {myNumericList}")
print(f"The Descending Alphabetically List Is {myNumericList}")
print()




# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):

# Example
# Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n -50)

myNumericList.sort(key = myfunc)
print(myNumericList)



# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Example
# Case sensitive sorting can give an unexpected result:
thislist1 = ["banana", "Orange", "Kiwi", "cherry"]
thislist1.sort()
print(thislist1)

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:

# Example
# Perform a case-insensitive sort of the list:
thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist2.sort(key = str.lower)
print(thislist2)




# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.

# Example
# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)