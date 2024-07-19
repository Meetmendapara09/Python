import pandas as pd

# Creating a Pandas Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])

print("Pandas Series:")
print(s)

# Creating a Pandas DataFrame
dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

print("\nPandas DataFrame:")
print(df)

# Basic DataFrame operations
print("\nDataFrame shape:")
print(df.shape)

print("\nDataFrame head (first 3 rows):")
print(df.head(3))

print("\nDataFrame tail (last 3 rows):")
print(df.tail(3))

print("\nDataFrame column names:")
print(df.columns)

print("\nDataFrame index:")
print(df.index)

# Accessing DataFrame elements
print("\nDataFrame column 'A':")
print(df['A'])

print("\nDataFrame row at index '20230102':")
print(df.loc['20230102'])

print("\nDataFrame element at position (0, 1):")
print(df.iloc[0, 1])

# Descriptive statistics
print("\nDescriptive statistics of DataFrame:")
print(df.describe())

# Transposing
print("\nTransposed DataFrame:")
print(df.T)

# Sorting by index or values
print("\nSorted DataFrame by index:")
print(df.sort_index(axis=0, ascending=False))

print("\nSorted DataFrame by values in column 'B':")
print(df.sort_values(by='B'))

# Selection using Boolean indexing
print("\nSelection using Boolean indexing:")
print(df[df['A'] > 0])

# Setting values
df.at[dates[0], 'A'] = 0
print("\nModified DataFrame after setting value:")
print(df)

# Missing data handling (dropping or filling NaN values)
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1.0
print("\nDataFrame with missing values (NaN):")
print(df1)

print("\nDataFrame with NaN rows dropped:")
print(df1.dropna())

print("\nDataFrame with NaN values filled with 0:")
print(df1.fillna(value=0))

# Operations (mean, max, min, cumulative sum, etc.)
print("\nMean across DataFrame:")
print(df.mean())

print("\nMax value in each column:")
print(df.max())

print("\nMin value in each row:")
print(df.min(axis=1))

print("\nCumulative sum:")
print(df.cumsum())

# Applying functions to DataFrame
print("\nApplying function (square root) to DataFrame:")
print(df.apply(np.sqrt))

# Concatenation of DataFrames
df2 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('EFGH'))
print("\nConcatenated DataFrame (along columns):")
print(pd.concat([df, df2], axis=1))

# Grouping and aggregation
df3 = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                    'B': ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)})
print("\nGrouped and aggregated DataFrame:")
print(df3.groupby('A').sum())

# Time series operations
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000', periods=1000))
print("\nTime series operations (resampling):")
print(ts.resample('M').mean())

# Reading from and writing to files (CSV)
df.to_csv('data.csv')
df_from_csv = pd.read_csv('data.csv')
print("\nDataFrame read from CSV file:")
print(df_from_csv.head())

# Reading from and writing to Excel files
df.to_excel('data.xlsx', sheet_name='Sheet1')
df_from_excel = pd.read_excel('data.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print("\nDataFrame read from Excel file:")
print(df_from_excel.head())
