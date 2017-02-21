import quandl # You know how it goes. And the below code is parsed from pandas basics 3.
import pandas as pd
import pickle

'''
# In these lines we make our quandl API Key and we parse the Wiki for the list of the states, like before.
api_key = 'j1EEWenU5vZ21HxjQWAo'

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

main_df = pd.DataFrame() # Here we are making an empty dataframe variable for later use.

for abbv in fiddy_states[0][0][1:]: # Now we use a for loop to iterate through the fifty states dataframe and assign the state abbreviations to our tickers for quandl.
    query = "FMAC/HPI_"+str(abbv)
    df = quandl.get(query, authtoken=api_key) # With this we can get the dataframe from quandl with our newly made ticker.
    df.columns = [abbv] # Quandl needs the name of a cloumn to differentiate from others, so lets just set each one to the value of abbv.

    if main_df.empty: # This checks through our main_df dataframe to see if its empty or not, and assigns the dataframes accordingly.
        main_df = df
    else:
        main_df = main_df.join(df)

print(main_df.head(0)) # Well, it works, and it's nice, but imagine having to parse and build this dataset every time... It would take a long time to get any work done.

# Next we are going to pickle our dataframe so we can use it anytime, without having to do that whole process again.
pickle_out = open('fiddy_states.pickle', 'wb') # First we open a .pickle file so we can write to it.
pickle.dump(main_df, pickle_out) # Then we dump the info we want into a file we want, which is the .pickle we just made.
pickle_out.close() # Lastly, we close the opened pickle jar :^)
'''

# Now this is all fine and dandy, however, in the workplace we will want to streamline this to make it more effecient.
# On that note, lets make this easier to handle...
api_key = 'j1EEWenU5vZ21HxjQWAo'

def state_list(): # Now we make this return what we need. Only the first index, and the first column, skipping over the first item.
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]


def grab_initial_state_data(): # Here we can just call this whole function once to make our little pickle file.
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.columns = [abbv]
        print(query) # This just lets us see what happened with query. Not necessary.

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


#grab_initial_state_data() # Now we call the function to generate the pickle for us.

# The best part of this is that we can call on the state_list function to grab the fifty states any time we want.
# And we can use the grab_initial_state_data function to just generate and pickle all of the quandl HPI data for the fifty states!!!

pickle_in = open('fiddy_states.pickle', 'rb')
HPI_data = pickle.load(pickle_in) # With these lines we open up the pickle jar, and take out a pickle :^D
print(HPI_data)

# Pandas does come with it's own pickle, which is supposed to be faster for large datasets, however I am not sure about that.
# Either way, if you are in pandas, the pandas pickle is undoubtedly easier to write, condensing three lines into one.
HPI_data.to_pickle('pandaspickle.pickle') # If it was in the for loop it would be, main_df.to_pickle('picklename.pickle').
HPI_datapandas = pd.read_pickle('pandaspickle.pickle') # This one line does what the three lines of the pickle_in does. Same as the pickle_out.
print(HPI_datapandas)
