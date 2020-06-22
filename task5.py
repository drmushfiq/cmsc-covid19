#importing modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
import sys
import os
from datetime import datetime


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


provinceDF=data.loc[data['prname'] == province] #creating a dataframe consisting only the rows of the given province
provinceDF=provinceDF.reset_index() #resetting the index of the new dataframe

indexOfGivenDate=provinceDF.index[provinceDF.date == date].tolist()[0] #saving the index number of the given date's row so that it can be iterated.
rowOfGivenDate=provinceDF.iloc[indexOfGivenDate] #getting the row of the given date in a variable
sevenDaysDF=provinceDF.iloc[indexOfGivenDate-7:indexOfGivenDate] #creating a separate dataframe with the rows of 7days

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


avg=average(sevenDaysDF) #getting the average
if(casesOrDeath=='cases'): #checking if input is cases or deaths
	doublingDays=predictDoublingDays(avg,int(rowOfGivenDate['numtotal'])) #getting the doubling days of cases from the function
else:
	doublingDays=predictDoublingDays(avg,int(rowOfGivenDate['numdeaths'])) #getting the doubling days of deaths from the function


#storing the outputs into a file
if(os.path.exists("storage.txt")): #checking if file already exists
	with open('storage.txt', 'a') as f: #if it exists opening with append
		f.write(str(date)+","+str(province)+","+str(casesOrDeath)+","+str(doublingDays)) #storing necessary info
		f.write("\n")
		f.close()
else:
	with open('storage.txt', 'w+') as f: #if file doesnt exist creating file
		f.write("date,province,cases/deaths,days to double") #adding columns on top of the file
		f.write("\n")
		f.write(str(date)+","+str(province)+","+str(casesOrDeath)+","+str(doublingDays)) #storing necessary info
		f.write("\n")
		f.close()
	