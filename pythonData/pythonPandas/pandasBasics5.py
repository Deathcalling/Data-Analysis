import pandas as pd # Ok, I think you get it now.

df1 = pd.DataFrame({'HPI':[80,85,88,85], # Here we have the same examples as before, except with one change in df3.
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

print(pd.merge(df1,df3, on='HPI')) # As you can see, we can merge our dataframes on a certain column, similar to how we would handle this in SQL.

print(pd.merge(df1,df2, on=['HPI', 'Int_rate'])) # We can also merge the data on two columns in this way.

df4 = pd.merge(df1,df3, on='HPI') # If you have a large amount of data, it might be a good idea to join instead of merge, since we would have many different dataframes to work with that may already have set indexes.
df4.set_index('HPI', inplace=True)
print(df4)

df1.set_index('HPI', inplace=True) # If both the indexes are already set HPI, we could then use join to merge the two dataframes.
df3.set_index('HPI', inplace=True)

joined = df1.join(df3)
print(joined)

# Here lets re-define df1 and df3 so we can try using join and merge in different circumstances.
df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

# Now we have two dataframes with similar columns, except a couple differences. Let's try and merge these.
merged = pd.merge(df1, df3, on='Year')
merged.set_index('Year', inplace=True)
print(merged) # Notice how we now have a merged table that is missing the values 2002, and 2005,
              # The reason for this is because merge only uses data that exists in both dataframes.

merged = pd.merge(df1,df3, on='Year', how='left') # Here we use the how parameter to join it from the left side.
merged.set_index('Year', inplace=True)
print(merged) # That gave us all the data from df1, but not df2, lets try the other side.

merged = pd.merge(df1,df3, on='Year', how='right') # Here we use how to select join on the right instead.
merged.set_index('Year', inplace=True)
print(merged) # Now we have all the data from df3, but not df1.

merged = pd.merge(df1, df3, on='Year', how='outer') # With this example we chose to outer join, which selects a union of all the keys.
merged.set_index('Year', inplace=True)
print(merged) # Now we see a table with all of the data from both the left and right dataframe.

merged = pd.merge(df1,df3, on='Year', how='inner') # Last but not least, we can use inner to merge.
merged.set_index('Year', inplace=True)
print(merged) # As you can see, with inner we get back a new table that contains only shared data between the two dataframes.

# Now we can try this with a join, for instances where the indexes of dataframes have already been set.
df1.set_index('Year', inplace=True)
df3.set_index('Year', inplace=True)

joined = df1.join(df3, how='outer') # Now that df1 and df3 were already set to have the index on Year, we can use join to merge the data.
print(joined)

# In the next tutorial we are going to go back to our quandl data from pandaBasics3.py, go ahead and copy/paste that into a new file, or just use the same one.
