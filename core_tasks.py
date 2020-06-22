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

province=str(sys.argv[1])
casesOrDeath=sys.argv[2]
date=str(sys.argv[3])



# april 24

# tota 628 rate 7.5

# aprl 25

# 628*7.5/100

# 675


# (7.5/628)*675


#date = datetime.strptime(date, "%d/%m/%Y")
#cur_date=datetime.strptime(date, "%d/%m/%Y")

# dates=[]
# numberOfDays=[]
# curTotal=0

provinceDF=data.loc[data['prname'] == sys.argv[1]]
# provinceDF=provinceDF.reset_index()

# days=0
# for i, row in provinceDF.iterrows():
# 	if(i==0):
# 		dates.append(row['date'])
# 		numberOfDays.append(1)
# 		curTotal=row['numtotal']
# 	elif(row['date']==sys.argv[3]):
# 		break
# 	else:
# 		days=days+1
# 		if(row['numtotal']>=2*curTotal):
# 			dates.append(row['date'])
# 			numberOfDays.append(days)
# 			days=0
# 			curTotal=row['numtotal']


# print(dates)
# print(numberOfDays)


# plt.plot(dates, numberOfDays, color='black');
# plt.plot(dates, numberOfDays, 'o', color='blue');
# plt.xticks(fontsize=5)
# plt.xticks(fontsize=5)
# plt.xlabel("Date's", fontsize=16)
# plt.ylabel('Number of Days', fontsize=16)
# plt.savefig('myfig')

provinceDF=provinceDF.reset_index()

row_of_given_date=provinceDF.index[provinceDF.date == sys.argv[3]]

index_of_given_date=row_of_given_date.tolist()[0]

seven_days=provinceDF.iloc[index_of_given_date-7:index_of_given_date]

avg=0

for i, row in seven_days.iterrows():
    avg=avg+row['numtoday']
    print(avg)

# for i in seven_days:
# 	avg=avg+seven_days['numtoday'].astype(int)
# 	print(avg)

avg=avg/len(seven_days)
print(avg)

# print(provinceDF)

# for i in arr:
# 	if()
# 	cur_date=(pd.Timestamp(cur_date) - pd.DateOffset(days=1)).strftime('%d/%m/%Y')
# 	s=cur_date.strftime(cur_date, "%d/%m/%Y")
# 	print(data.loc[data['date'] == s])
	


#res = (pd.to_datetime(date) - pd.Timedelta('1 day')).strftime('%d/%m/%Y')


# def rateOfSpread:
