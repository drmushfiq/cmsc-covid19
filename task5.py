#importing modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
import sys
from datetime import datetime


#Download csv file:
#Getting csv data into a pandas dataframe
data = pd.read_csv('https://health-infobase.canada.ca/src/data/covidLive/covid19.csv',sep=',')

#saving given arguments into variables
province=str(sys.argv[1])
casesOrDeath=sys.argv[2].lower()
date=str(sys.argv[3])


provinceDF=data.loc[data['prname'] == province] #creating a dataframe consisting only the rows of the given province
provinceDF=provinceDF.reset_index() #resetting the index of the new dataframe

rowOfGivenDate=provinceDF.index[provinceDF.date == date] #finding the row of the given date
indexOfGivenDate=rowOfGivenDate.tolist()[0] #saving hte index number of the given date's row so that it can be iterated.
sevenDaysDF=provinceDF.iloc[indexOfGivenDate-7:indexOfGivenDate] #creating a separate dataframe with the rows of 7days before the given date

#the function takes a dataframe as an input and returns average increase of the last 7days
def average(DF):
	avg=0 #setting an initial value of avg variable.

	for i, row in sevenDaysDF.iterrows(): #loop to iterate over 7days of data
		if(casesOrDeath=='cases'): #checking weather to get case rate or death rate
			avg=avg+row['numtoday'] #sum of total case increase each day
		else:
			avg=avg+row['deathstoday'] #sum of total death increase each day
	avg=avg/len(sevenDaysDF) #getting the average of the increase case/death in past 7days from the given date
	return avg

print(average(sevenDaysDF))