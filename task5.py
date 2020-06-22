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


provinceDF=data.loc[data['prname'] == province] #creating a dataframe consisting only the rows of the given province
provinceDF=provinceDF.reset_index() #resetting the index of the new dataframe

provinceDF['date']=provinceDF['date'].replace(['/'], '-') #converting all dates to the same format

#Exception handling for invalid dates.
try:
	indexOfGivenDate=provinceDF.index[provinceDF.date == date].tolist()[0] #saving the index number of the given date's row so that it can be iterated.
	rowOfGivenDate=provinceDF.iloc[indexOfGivenDate] #getting the row of the given date in a variable
	sevenDaysDF=provinceDF.iloc[indexOfGivenDate-7:indexOfGivenDate] #creating a separate dataframe with the rows of 7days
except IndexError:
	print("Given date doesnt exist in the data. Please make sure date format is dd-mm-yyyy")
	exit(0)

#Exception handling for invalid cases/deaths.
if(str(casesOrDeath)=="cases" or str(casesOrDeath)=="deaths"): #checking valid inputs
	print("calculating "+casesOrDeath+" for "+province+" on "+date)
else:	
	print("Invalid input. Write 'cases' to get doubling days for case or write 'deaths' to get doublind days for deaths.")
	exit(0)

if(casesOrDeath=='cases'): #checking weather to get case rate or death rate
	caseOrDeathTotal=rowOfGivenDate['numtotal'] #sum of total case increase each day
else:
	caseOrDeathTotal=rowOfGivenDate['numdeaths'] #sum of total death increase each day

#------------------------------------DATA PREP AND EXCEPTION HANDLING END---------------------------------------#



#-----------------------------------------FUNCTIONS-----------------------------------------------#


#the function takes a dataframe as an input and returns average increase of the last 7days
def average(DF):
	avg=0 #setting an initial value of avg variable.

	for i, row in sevenDaysDF.iterrows(): #loop to iterate over 7days of data
		if(casesOrDeath=='cases'): #checking weather to get case rate or death rate
			avg=avg+row['numtoday'] #sum of total case increase each day
		else:
			avg=avg+row['deathstoday'] #sum of total death increase each day
	if(avg==0): #checking if average 0
		avg=0 #setting to zero 
	else:
		avg=avg/len(sevenDaysDF) #getting the average of the increase case/death in past 7days from the given date
	return avg


#the function calculates the doubling days from the average and the current number of cases/deaths of the given date
def predictDoublingDays(avg, currentNumber):
	if(avg==0): #checking if avg is 0
		return 0 #if avg is 0 that means it hasnt increased at all in 7days so at that rate it wont ever double up
	doublingDays=int(round(currentNumber/avg)) #calculating how many days it will take to double up
	if (doublingDays==0): #checking if the doubling days is 0 
		doublingDays=1 #if the doubling days is 0 it should say it takes 1day to double
	return int(round(currentNumber/avg))


#--------------------------------------FUNCTIONS END---------------------------------------------#




#--------------------------------------DIVER PROGRAM---------------------------------------------#

avg=average(sevenDaysDF) #getting the average
doublingDays=predictDoublingDays(avg,int(caseOrDeathTotal)) #getting the doubling days of cases from the function


#--------------------------------------DIVER PROGRAM END----------------------------------------#




#-----------------------------------------STORAGE-----------------------------------------------#

#storing the outputs into a file
if(os.path.exists("storage.txt")): #checking if file already exists
	with open('storage.txt', 'a') as f: #if it exists opening with append
		f.write(str(date)+","+str(province)+","+str(casesOrDeath)+","+str(caseOrDeathTotal)+","+str(int(round(avg)))+","+str(doublingDays)) #storing necessary info
		f.write("\n")
		f.close()
else:
	with open('storage.txt', 'w+') as f: #if file doesnt exist creating file
		f.write("date,province,cases/deaths,total,rate_of_spread,days_to_double") #adding columns on top of the file
		f.write("\n")
		f.write(str(date)+","+str(province)+","+str(casesOrDeath)+","+str(caseOrDeathTotal)+","+str(int(round(avg)))+","+str(doublingDays)) #storing necessary info
		f.write("\n")
		f.close()
	
#--------------------------------------STORAGE END---------------------------------------------#