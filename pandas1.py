import pandas as pd

# create a series
s = pd.Series([1,2,3,4,5])
print("Series:\n", s)

# create a DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

dd = {
    'Name': ['Subesh', 'Smith', 'Rajan', 'Ritesh', 'Amir'],
    'Age': [25, 27, 25, 26, 25],
    'City': ['Bus-Park', 'Cancer-Gate', 'Kshetrapur', 'Lakeside', 'Newroad']
}
df1 = pd.DataFrame(dd)
print("\nDataFrame df1:\n", df1)

# Accessing specific columns from df1 called 'Age
age_column = df1['Age']
print("Age Column:\n",age_column)

# Accessing specific columns from df1 called 'Name' and 'City'
print("Age Colum And City Column:\n", df1[['Name', 'City']])

# Selecting rows by index position
first_row = df1.iloc[0]
print("\nFirst Row:\n", first_row)

# Selecting multiple rows by index position
first_two_rows = df.loc[0:1]
print("\nFirst Two Rows:\n", first_two_rows)

# Adding new column 'Salary'
df1['Salary'] = [50000, 60000, 55000, 52000, 58000]
print("\nDataFrame df1 after adding Salary column:\n", df1)

# Filtering Data: Rows where Age > 25
filtered_data = df1[df1['Age'] > 25]
print("\nFiltered Data (Age > 25):\n", filtered_data)

# using head to view first 3 rows
print("\nFirst 3 rows of df1:\n", df1.head(3))

# using tail to view last 3 rows
print("\nLast 3 rows of df1:\n", df1.tail(3))

# accessing DataFrame attributes
print("\nDataFrame Index :\n", df1.index)
print("\nDataFrame Columns :\n", df1.columns)
print("\nDataFrame Data Types: \n ", df1.dtypes)
print("\nDataFrame Shape :\n", df1.shape)
print("\nDataFrame Size:\n", df1.size)
print("\nDataFrame Values:\n", df1.values)
print("\nDataFrame Transpose:\n", df1.T)
print("\nDataFrame Info:\n", df1.info())

# For Series
ser = pd.Series([1,2,3], index=['a','b','c'], name ="Example Series")

# accessing Series attributes
print("\nSeries Index :\n", ser.index)
print("\nSeries Values:\n", ser.values)
print("\nSeries Data Type:\n", ser.dtype)
print("\nSeries Shape:\n", ser.shape)
print("\nSeries Size:\n", ser.size)
print("\nSeries Name:\n", ser.name)
print("\nSeries Transpose:\n", ser.is_unique)
print("\nSeries Info:\n", ser.isnull())
  
