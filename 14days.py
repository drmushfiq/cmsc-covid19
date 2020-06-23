#importing modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
import sys
import os
from datetime import datetime


#------------------------------------DATA PREP AND EXCEPTION HANDLING----------------------------------------#

#Download csv file:
#Getting csv data into a pandas dataframe
data = pd.read_csv('https://health-infobase.canada.ca/src/data/covidLive/covid19.csv',sep=',')

#saving given arguments into variables
province=str(sys.argv[1])
casesOrDeath=sys.argv[2].lower()
date=str(sys.argv[3])


#converting province code from arguments init province name
if(province.upper()=='NL'):
	province='Newfoundland and Labrador'
elif(province.upper()=='PE'):
	province='Prince Edward Island'
elif(province.upper()=='NS'):
	province='Nova Scotia'
elif(province.upper()=='NB'):
	province='New Brunswick'
elif(province.upper()=='QC'):
	province='Quebec'
elif(province.upper()=='ON'):
	province='Ontario'
elif(province.upper()=='MB'):
	province='Manitoba'
elif(province.upper()=='SK'):
	province='Saskatchewan'
elif(province.upper()=='AB'):
	province='Alberta'
elif(province.upper()=='YT'):
	province='Yukon'
elif(province.upper()=='BC'):
	province='British Columbia'
elif(province.upper()=='NT'):
	province='Northwest Territories'
elif(province.upper()=='NU'):
	province='Nunavut'
else:
	print("Invalid Province Code Entered. Try again with proper province code please (e.g. NL, ON, NB etc)")
	exit(0)


provinceDF=data.loc[data['prname'] == province] 									#creating a dataframe consisting only the rows of the given province
provinceDF=provinceDF.reset_index() 												#resetting the index of the new dataframe

provinceDF['date']=provinceDF['date'].replace(['/'], '-') 							#converting all dates to the same format

#Exception handling for invalid dates.
try:
	indexOfGivenDate=provinceDF.index[provinceDF.date == date].tolist()[0] 			#saving the index number of the given date's row so that it can be iterated.
	rowOfGivenDate=provinceDF.iloc[indexOfGivenDate] 								#getting the row of the given date in a variable
	sevenDaysDF=provinceDF.iloc[indexOfGivenDate-7:indexOfGivenDate+1] 				#creating a separate dataframe with the rows of 7days
except IndexError:
	print("Given date doesn't exist in the data. Please make sure date format is dd-mm-yyyy")
	exit(0)

#Exception handling for invalid cases/deaths.
if(str(casesOrDeath)=="cases" or str(casesOrDeath)=="deaths"): 						#checking valid inputs
	print("calculating "+casesOrDeath+" for "+province+" on "+date)
else:	
	print("Invalid input. Write 'cases' to get doubling days for case or write 'deaths' to get doublind days for deaths.")
	exit(0)

if(casesOrDeath=='cases'): 															#checking weather to get case rate or death rate
	caseOrDeathTotal=rowOfGivenDate['numtotal'] 									#storing total cases if its for cases
else:
	caseOrDeathTotal=rowOfGivenDate['numdeaths'] 									#storing total deaths if its for deaths


#------------------------------------DATA PREP AND EXCEPTION HANDLING END---------------------------------------#



#-----------------------------------------FUNCTIONS-----------------------------------------------#


'''
	The function calculates how much more or less cases/deaths are increasing each day 
	compared to the previous day. It checks it for 7days, finds the average increase per day
	and returns it.
'''
def averageIncrease():
	previouseTotal=provinceDF.iloc[indexOfGivenDate-8] 							#getting the 8day before total of cases/deaths to calculate next days
	if(casesOrDeath=='cases'): 													#checking weather to get case rate or death rate
		previouseTotal=previouseTotal['numtoday']
	else:
		previouseTotal=previouseTotal['deathstoday']
	increaseRate=0 																#setting an initial value of increaseRate variable.
	
	#loop to iterate over 7days of data
	for i, row in sevenDaysDF.iterrows(): 
		if(casesOrDeath=='cases'): 												#checking weather to get case rate or death rate
			increaseRate=increaseRate+(row['numtoday']-previouseTotal)
			previouseTotal=row['numtoday']
		else:
			increaseRate=increaseRate+(row['deathstoday']-previouseTotal)
			previouseTotal=row['deathstoday']
	else:
		increaseRate=increaseRate/len(sevenDaysDF) 								#getting the average of the increase rate in past 7days from the given date
	return int(round(increaseRate))


'''
	The function takes 3 inputs:
		- rate of increase
		- given date
		- total number of cases or deaths on the given day
	
	The function genarates 14days of data based on increase rate
	And returns two lists:
		- list of date of each of these next 14 days
		- list of how much should increase each day
	
'''
def predictTotalIn14Days(increaseRate, date, total):
	
	#setting initial values
	increase=[]
	future_date=[]
	newdate=pd.Timestamp(date).strftime('%d-%m-%Y')
	currentToday=provinceDF.iloc[indexOfGivenDate]

	if(casesOrDeath=='cases'): 													#checking weather to get case rate or death rate
		currentToday=currentToday['numtoday'] 									#storing current total cases
	else:
		currentToday=currentToday['deathstoday'] 								#storing current total deaths
	
	#loop to iterate over 14days
	for i in range(14): 
		currentToday=currentToday+increaseRate 									#adding the increase rate with the number of new cases/deaths
		total=total+currentToday 												#adding the predicted new case/death with the total
		increase.append(total) 													#appending each days increase in a list

		newdate=(pd.Timestamp(newdate) + pd.DateOffset(days=1)) 				#calculating the date of current day by adding a day
		future_date.append(newdate.strftime('%d-%m-%Y'))				 		#appending the calculated date
		
	return (future_date, increase)



#--------------------------------------FUNCTIONS END---------------------------------------------#




#--------------------------------------DIVER PROGRAM---------------------------------------------#


increaseRate=averageIncrease() 																		#getting the average increaserate
future_date, increase=predictTotalIn14Days(increaseRate,rowOfGivenDate['date'], caseOrDeathTotal) 	#getting the doubling days of cases from the function

totalAfter14days=str(increase[-1]) 																	#getting the last value of the list which is total after 14days

#showing output
print("Total "+casesOrDeath+" on "+str(date)+": "+str(caseOrDeathTotal))
print("Total "+casesOrDeath+" after 14days: "+totalAfter14days)


#--------------------------------------DIVER PROGRAM END----------------------------------------#





#-----------------------------------------PLOTTING DATA-----------------------------------------------#

allDates=sevenDaysDF['date'].tolist()+future_date 								#adding the list of previous seven dates with the new 14 dates

if(casesOrDeath=='cases'): 														#checking weather to get case rate or death rate
	allTotals=sevenDaysDF['numtotal'].tolist()+increase 						#adding the list of previous total cases with the list of new cases
else:
	allTotals=sevenDaysDF['numdeaths'].tolist()+increase 						#adding the list of previous total deaths with the list of new deaths



fig = plt.figure(figsize=(12,8)) 														#creating a figure

if(casesOrDeath=='cases'): 																#checking weather to plot case rate or death rate
	plt.plot(sevenDaysDF['date'], sevenDaysDF['numtotal'], 'o', label="last 7days"); 	#ploting previous 7days cases with dots
else:
	plt.plot(sevenDaysDF['date'], sevenDaysDF['numdeaths'], 'o', label="last 7days"); 	#ploting previous 7days deaths with dots

plt.plot(allDates, allTotals); 															#plotting the combination of 7days and next 14days with a line
plt.plot(future_date, increase, 'o', label="predicted 14days"); 						#ploting predicted 14days of cases/deaths with dots



plt.title('Total after 2 weeks: '+totalAfter14days) 							#setting graph title to be the total number after 14days
plt.xticks(fontsize=8, rotation=50) 											#setting font and rotation for x axis
plt.yticks(fontsize=10) 														#setting font for y axis
plt.xlabel("Date", fontsize=16) 												#setting label x axis
plt.legend(loc="upper left") 													#setting location of legends
plt.ylabel('Number of '+casesOrDeath, fontsize=16) 								#setting label for cases


plt.show() 																		#show the plot
plt.savefig('14daysPrediction') 												#save the plot in 14daysPrediction.png


#-----------------------------------------PLOTTING DATA END-----------------------------------------------#
