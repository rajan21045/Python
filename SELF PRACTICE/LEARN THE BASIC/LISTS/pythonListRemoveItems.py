# Python - Remove List Items
myList = [1, 2, 3, 2, 5, 8, 9]
myList1 = [1, 2, 3, 2, 5, 8, 9]

# Remove Specified Item
# The remove() method removes the specified item.
# If there are more than one item with the specified value, the remove() method removes the first occurrence:
myList.remove(2)
print(myList) 

# Remove Specified Index
# The pop() method removes the specified index.
# Remove the second item:
myList.pop(1)
print(myList) 
# If you do not specify the index, the pop() method removes the last item.
myList.pop()
print(myList) 

# The del keyword also removes the specified index:
# Remove the first item:
del myList1[0]
print(myList1)

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print(thislist) 