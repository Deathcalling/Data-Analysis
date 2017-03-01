import quandl # Libraries... etc...
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot') # I am going to use ggplot since I like it a tad better than the last one we used. You can use whatever style you want to use.

api_key = 'j1EEWenU5vZ21HxjQWAo' # The API key. Insert your own one here.

def state_list(): # Our state list grabber
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial_state_data(): # Our state data creator
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

    main_df.to_pickle('fiddy_states3.pickle')

def HPI_Benchmark(): # And again, our benchmark of the USA average data for the same amount of years as our state data
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    return df

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

HPI_data = pd.read_pickle('fiddy_states3.pickle') # The pickle is un-pickled... once... more...
HPI_State_Correlation = HPI_data.corr() # Correlation between the data we have in our Dataframe. I am not goin to print it out again, but i will just leave it here for now.
TX1yr = HPI_data['TX'].resample('A').mean() # On this line we resample our data, where there is an A, that is an alias and it is simply a way to tell pandas how you want to resample it. A list is below in comments to show what all of the little keywords/letters are.
HPI_data['TX'].plot(ax=ax1, label='Monthly TX HPI') # This is going to plot for us, only the information from TX
TX1yr.plot(color='k', ax=ax1, label='Yearly TX HPI')# And this will plot a resampled data line for the year end of TX

plt.legend(loc=4) # Unlike in previous tutorials we are going to keep the legend for this graph since we only have two types of data to graph.
plt.show() # Now you should see we have our regular monthly data from Quandl, and now we also have a resampled line that is plotted year by year instead!

'''
Resample rule:
xL for milliseconds
xMin for minutes
xD for Days

Alias	Description
B	business day frequency
C	custom business day frequency (experimental)
D	calendar day frequency
W	weekly frequency
M	month end frequency
BM	business month end frequency
CBM	custom business month end frequency
MS	month start frequency
BMS	business month start frequency
CBMS	custom business month start frequency
Q	quarter end frequency
BQ	business quarter endfrequency
QS	quarter start frequency
BQS	business quarter start frequency
A	year end frequency
BA	business year end frequency
AS	year start frequency
BAS	business year start frequency
BH	business hour frequency
H	hourly frequency
T	minutely frequency
S	secondly frequency
L	milliseonds
U	microseconds
N	nanoseconds

How:
mean, sum, ohlc
'''
