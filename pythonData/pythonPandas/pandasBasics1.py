import pandas as pd #Here we import all necessary modules for us to use.
import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style #This simply tells python that we want to make matplotlib look a bit nicer.
style.use('ggplot') #Here we tell python what kind of style we would like to use for matplotlib

#Now I just made a dictionary to represent a dataframe type of datastructure
web_stats = {'Day' : [1,2,3,4,5,6],
            'Visitors' : [43,56,76,46,54,34],
            'Bounce_Rate' : [65,23,34,45,87,65]}

stats = pd.DataFrame(web_stats) #Turned our dictionary into a dataframe

print(stats) #Head and tail display the first five and last five of a dataframe
print(stats.head(2))
print(stats.tail(2))

print(stats.set_index('Day')) #Another way to get the same result, telling python we want stats to show the index of Day.

stats2 = stats.set_index('Day')

print(stats2.head())

print(stats['Bounce_Rate']) #more ways to display data
print(stats.Visitors)

print(stats[['Bounce_Rate','Visitors']]) # One way to get two or more different columns.

print(stats.Visitors.tolist()) #Here we told python to turn this column of data into a list.

print(np.array(stats[['Bounce_Rate','Visitors']])) # Using numpy we can make a dataset into an array!

stats3 = pd.DataFrame(np.array(stats[['Bounce_Rate','Visitors']])) # And just like we can turn dataframes to arrays, we can also turn arrays to dataframes!!!

print(stats3)

stats.plot()

plt.show()
