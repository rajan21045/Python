# To change the value of a specific item, refer to the index number:
thislist = ["Rajan Poudel", "Ujjwal Poudel", "Ashok Poudel"]
thislist[0] = "Ram Shyam"
print(thislist)

# Change the values "banana" and "cherry" with the values "watermelon" and "grapes":
thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:3] = ["watermelon", "grapes"]
print(thislist1)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist2 = ["apple", "banana", "mango"]
thislist2[1:2] = ["orange", "kiwi"]
print(thislist2)

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
thislist3 = ["apple", "banana", "mango"]
thislist3.insert(2, "cherry")
print(thislist3)