import pandas as pd # Start with our library to use

df = pd.read_csv('Python/pythonData/pythonPandas/ZILL-Z84501_MLP.csv') # Use pandas to read a dataframe that I took from Quandl.
print(df.head()) # Remember we don't have to print every time, it is just to visualize the practice code.

df.set_index('Date', inplace=True) # Similar to the first basics file, this is a way to set an index to display.

df.to_csv('newcsv.csv') # With this we can take only the index we want and write it to a new file

df = pd.read_csv('newcsv.csv', index_col=0) # Reading the file and setting the column to 0
print(df.head())

df.columns = ['Plano_HPI'] # Naming one of the columns
print(df.head())

df.to_csv('newcsv3.csv')
df.to_csv('newcsv4.csv', header=False) # If you don't want the header to be in the file right away, you can set header to false

df = pd.read_csv('newcsv4.csv', names=['Date','PLano_HPI'], index_col=0) # Here we can read from newcsv4, naming the columns, and setting the index to 0
print(df.head())

df.to_html('example.html') # Here we can use panda to convert our dataframe to an html file.

df = pd.read_csv('newcsv4.csv', names=['Date', 'Plano_HPI']) #Here we made a new csv without setting the index immediately
print(df.head())

df.rename(columns={'Plano_HPI':'75075_HPI'}, inplace=True) # In this line we changed the name of only one column from Plano, to the ZIP code of Plano
print(df.head())
