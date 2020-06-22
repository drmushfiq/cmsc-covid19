#importing modules
import sys
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates




def unique(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result


def cases_stat(place,placeArray,caseArray,cutoff=0):
    if place in placeArray:
        if math.isnan(caseArray[placeArray.index(place)]):
            return 0
        else:
            if caseArray[placeArray.index(place)] >= cutoff:
                return caseArray[placeArray.index(place)]
            else:
                return 0
    else: 
        return 0   




#Download csv file:
#Getting csv data into a pandas dataframe
data = pd.read_csv('https://health-infobase.canada.ca/src/data/covidLive/covid19.csv',sep=',')
dates = unique(data['date'])
caseToday = data[['prname', 'date', 'numtoday']]

# Declare arrays for each province
ontario = []
bc = []
pei = []
ns = []
nb = []
quebec = []
manitoba = []
saskatchewan = []
alberta = []
nfld = []
yukon = []
nt = []
nunavut = []
rt = []
canada = []

c = 0
numberOfRows = len(caseToday)
for date in dates:
    places = []
    cases = []
    for ct in range(c,numberOfRows,1):
        if caseToday['date'][c] == date:
            places.append(caseToday['prname'][c].lower())
            cases.append(caseToday['numtoday'][c])
            c+=1
        else:
            break
    
    
    # Fill province arrays with total cases in respective provinces
    ontario.append(cases_stat("ontario", places, cases, 100))
    bc.append(cases_stat("british columbia", places, cases, 30))
    pei.append(cases_stat("prince edward island", places, cases, 15))
    ns.append(cases_stat("nova scotia", places, cases, 10))
    nb.append(cases_stat("new brunswick", places, cases, 10))
    quebec.append(cases_stat("quebec", places, cases, 70))
    manitoba.append(cases_stat("manitoba", places, cases, 2))
    saskatchewan.append(cases_stat("saskatchewan", places, cases, 4))
    alberta.append(cases_stat("alberta", places, cases, 10))
    nfld.append(cases_stat("newfoundland and labrador", places, cases, 5))
    yukon.append(cases_stat("yukon", places, cases, 2))
    nt.append(cases_stat("northwest territories", places, cases, 2))
    nunavut.append(cases_stat("nunavut", places, cases, 0))
    rt.append(cases_stat("repatriated travellers", places, cases, 3))
    canada.append(cases_stat("canada", places, cases, 40))
        
    places.clear()
    cases.clear()
    

# set start and end date
start = pd.to_datetime(dates[0])
end = pd.to_datetime(dates[len(dates) - 1])
dates = pd.date_range(start, end, periods= len(dates))
                    

# plot results of provinces
plt.figure(figsize=(15,10))
plt.plot(dates,ontario,'#D35400',label="Ontario")
plt.plot(dates,bc,'#FF8850',label="British Columbia")
plt.plot(dates,pei,'#FFD500', label="Prince Edward Island")
plt.plot(dates,ns,'#5FA30D',label="Nova Scotia")
plt.plot(dates,nb,'#15F518',label="New Brunswick")
plt.plot(dates,quebec,'#00FFF7',label="Quebec")
plt.plot(dates,manitoba,'#00A2FF',label="Manitoba")
plt.plot(dates,saskatchewan,'#001BFF',label="Saskatchewan")
plt.plot(dates,alberta,'#C900FF',label="Alberta")
plt.plot(dates,nfld,'#FF00E4',label="Newfoundland and Labrador")
plt.plot(dates,yukon,'#935116',label="Yukon")
plt.plot(dates,nt,'#839192',label="Northwest Territories")
plt.plot(dates,nunavut,'#000000',label="Nunavut")
plt.plot(dates,rt,'#FF0000',label="Repatriated Travellers")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%y'))
plt.xlabel("Dates", fontsize="14")
plt.ylabel("Number of New Cases", fontsize="14")
plt.legend()
plt.grid()
plt.title("Number of New Cases in Each Provinces", fontsize="20", color="blue")
plt.show()