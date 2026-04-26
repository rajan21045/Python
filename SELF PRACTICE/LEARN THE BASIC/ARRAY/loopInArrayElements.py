# loopInArrayElements.py
# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

# Adding Array Elements
# You can use the append() method to add an element to an array.
# Example
# Add one more element to the cars array:
cars.append("Honda")
cars.append("Volvo")
print(cars)

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
# Example
# Delete the second element of the cars array:
cars.pop(1)
print(cars)

# You can also use the remove() method to remove an element from the array.
cars.remove("Volvo")
print(cars)

# reverse()	- Reverses the order of the list
cars.reverse()
print(cars)

# count() - Returns the number of elements with the specified value
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)


# sort() - Sorts the list
points.sort()
print(points)