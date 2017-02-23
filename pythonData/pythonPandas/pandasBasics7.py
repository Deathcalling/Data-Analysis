import quandl
import pandas as pd # Once again, we have our libraries.
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = 'j1EEWenU5vZ21HxjQWAo' # All of this is our functions from our last tutorial.

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.columns = [abbv]
        print(query)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

HPI_data = pd.read_pickle('fiddy_states.pickle') # Hre we use the pandas pickle function to unpickle our fifty states HPI data.

HPI_data['TX2'] = HPI_data['TX']*2 # In this example we are going to display the manipulation of data by assigning another column, to the dataframe as Texas' HPI doubled.
print(HPI_data[['TX','TX2']].head()) # Now we are going to print the head of both to the console so you can see the outcome.
HPI_data.plot() # Here we use matplotlib's pyplot in order to map out our data.
plt.legend().remove() # On this line we are removing the legend, which normally would tell us what each line on the graph represents, but we don't need it right now.
plt.show() # And finally we tell pyplot to display the graph for us with the show() function.
# Also, as a side note, you will notice one of the lines is much higher than the others. This is because that one is the TX2 column we added earlier.

# As you can see, all the prices converge at the year 2000... This works, but it doesn't visualize the data nicely like a percent change would.

def grab_initial_state_data(): # Here we are going to modify our function from before to use pandas' built in function of pct_change()
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.columns = [abbv]
        print(query)
        df = df.pct_change() # Here is the part we want that has the biggest difference!
        print(df.head())

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    main_df.to_pickle('fiddy_states2.pickle') # We are going to re-pickle to another file, instead of re-opening and modifying our last file.

#grab_initial_state_data() # Call the fucntion to generate a new pickle. Then comment it out, unless you want to make a new pickle every time!

HPI_data = pd.read_pickle('fiddy_states2.pickle') # Now we do like we did earlier, and unpickle our data and assign it to a variable.

HPI_data.plot() # Displaying the plot again, and removing the legend.
plt.legend().remove()
plt.show() # Now you should see a graph with the percentage change of all the HPIs starting from their last reported value.

# If we want a traditional percent change chart we can do something a little differently.

def grab_initial_state_data(): # Again, all of this is pretty much the same.
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.columns = [abbv]
        print(query)
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0 # This line is what gives us a traditional percent change by using the percentage change formula.

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    main_df.to_pickle('fiddy_states3.pickle') # Let's pickle that to a new file again, we may want to use the other two later on.

#grab_initial_state_data() # Now call it again to create a new pickle.

HPI_data = pd.read_pickle('fiddy_states3.pickle') # Unpickling, are you getting the hang of this yet?

HPI_data.plot() # And for the thrid time in this tutorial, we plot the data!
plt.legend().remove()
plt.show() # And now we have a nice and easy to understand visualization of the percentage change of the HPI itself!

def HPI_Benchmark(): # This function is for us to compare our data against some sort of benchmark, I chose to use the United States HPI as a benchmark.
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0 # We use the percentage change formula again here to display the data the same way as the fifty states.
    return df

fig = plt.figure() #
ax1 = plt.subplot2grid((1,1), (0,0)) # This line creates a grid for where we want to start.

HPI_data = pd.read_pickle('fiddy_states3.pickle') # Unpickling... again :)
benchmark = HPI_Benchmark() # Next we assign our function to a variable.
HPI_data.plot(ax=ax1) # Here we tell pyplot to actually plot our grid.
benchmark.plot(color='k', ax=ax1, linewidth=10)  # And finally we tell pyplot to plot our benchmark onto the new grid we made.

plt.legend().remove()
plt.show()

# Next we are going to create a correlation table through pandas' built in corr() function so we might see the relationship of the states' market deviation.

HPI_data = pd.read_pickle('fiddy_states3.pickle') # Well by now you should notice that we don't need to keep writing this, but I am just doing it to re-iterate the pandas pickle function and how it works.
HPI_State_Correlation = HPI_data.corr()
print(HPI_State_Correlation) # Now we can see the correlation between all fifty states.

print(HPI_State_Correlation.describe()) # This is a super useful function that is built in to pandas that will show for each state what the minimum, maximum, standard, mean, and quartered percentages of the correlations the state had.
