import pandas as pd

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myVar = pd.Series(a)
print(myVar)
print(myVar[0])

b = [1,2,3]
myvar = pd.Series(b, index=["X", "Y", "Z"])
print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}
myvarr = pd.Series(calories)
print(myvarr)