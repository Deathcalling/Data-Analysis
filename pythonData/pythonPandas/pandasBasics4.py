import pandas as pd # Again, import all necessary libraries first. Sorry I am beating a dead horse, but it's super important.

df1 = pd.DataFrame({'HPI':[80,85,88,85], # These are some example dictionaries that we are turning into dataframes. Feel free to copy and paste these.
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

# Notice that a few of them differ in index, and/or columns. We can use concatenation to put some of these together.

concat = pd.concat([df1, df2]) # This way we can take two dataframes with different indexes, and put them together so their data flows smoothly in one dataframe.
print(concat)

concat = pd.concat([df2, df2, df3]) # In this way we added together a dataframe with different columns so in the end, we have all of our data, but we don't have it displayed in a smooth and easy to read way.
print(concat)

df4 = df1.append(df2) # Another way to force the issue, is to append a dataframe to another one, which just adds it to the end of another.
print(df4)

df4 = df1.append(df3) # Here we see that instead of turning the datafram into a nice readable format, we have the indexes being repeated and is not a nice way to display data.
print(df4)

s = pd.Series([80,2,50], index=['HPI','Int_rate','US_GDP_Thousands']) # And finally we can use the Series function from pandas to convert data into a single column with no index and concat them that way.
df4 = df1.append(s, ignore_index=True)
print(df4)
