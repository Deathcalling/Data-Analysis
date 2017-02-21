import pandas as pd # To start, import necessary libraries.
import quandl # In order to use quandl how I display below, you will need to pip install the lxml module as well as BeautifulSoup4.

# Here we use the quandl module in order to take dataframes from quandl's vast amounts of data. This one is for the house pricing index of the city of Kokomo.
df = quandl.get("FMAC/HPI_KOKIN", authtoken="j1EEWenU5vZ21HxjQWAo", start_date="1999-01-31")
print(df.head())
# This would be hard to get a dataframe from each state by clicking all of them indivually, so alternatively we can do something else.

# This is another way to get data from the web. We can use pandas read_html function to parse website for data.
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#print(fiddy_states) # If we ask for the data in this way, we will get returned a list of all the different frames that may or may not be useful to us.
                    # However, since we only want the list of the states, we need to target just the first dataframe like this.
print(fiddy_states[0]) # We use the index of 0, just like a list, in order to get the first dataframe.

# If you noticed, the first item in the first column is the word 'Abbreviation', well we don't want that, just the states.
# So we can skip over it when we iterate through the column with this [1:]
for abbv in fiddy_states[0][0][1:]: # We selected the index of 0 for the list of dataframes, then the index of 0 for the column we wanted, then chose the starting point after the first item.
    print(abbv)

for abbv in fiddy_states[0][0][1:]:
    print('FMAC/HPI_' + abbv) # Here we add the key selector for our quandl data to the beginning of the state Abbreviation.
                              # Now we can grab all of the housing price index data at once without typing out each and every one.
