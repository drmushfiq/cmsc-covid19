#importing modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#------------------------------------DATA PREP----------------------------------------#

#Download csv file:
#Getting csv data into a pandas dataframe
data = pd.read_csv('https://health-infobase.canada.ca/src/data/covidLive/covid19.csv',sep=',')

#Getting stored value from txt file into a pandas dataframe
doublingDays=pd.read_csv("storage.txt", sep=',')

#------------------------------------DATA PREP END-------------------------------------#



#------------------------------------DATA PLOTTING----------------------------------------#

fig = plt.figure(figsize=(12,8)) #creating a figure\

#looping through the storage dataframe
for i, row in doublingDays.iterrows():
	#ploting with x axis having province name, date, cases or death and on y axis having days to double
	if(str(row['cases/deaths'])=='cases'): #checking if plotting for cases or deaths
		plt.bar(row['province']+"\n"+row['date']+"\n"+row['cases/deaths'],row['days_to_double'], color = [(.200,.100,.700)])  #blue colored bars for cases
	else:
		plt.bar(row['province']+"\n"+row['date']+"\n"+row['cases/deaths'],row['days_to_double'], color= [(.700,.100,.150)]) #red colored bars for deaths


plt.title('Days to double') #setting graph title
plt.ylabel('Days') #y axis label
plt.show() #showing the plot

plt.savefig('doublingdays') #saving the figure as doublingdays.png


#------------------------------------DATA PLOTTING END------------------------------------#


