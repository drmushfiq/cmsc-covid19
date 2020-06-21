#importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates




def unique(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result


def cases_stat(place,placeArray,caseArray):
        if place in placeArray:
            return caseArray[placeArray.index(place)]
        else: 
            return 0   




#Download csv file:
#Getting csv data into a pandas dataframe
data = pd.read_csv('https://health-infobase.canada.ca/src/data/covidLive/covid19.csv',sep=',')

dates = unique(data['date'])

casesPerDay = data[['prname', 'date', 'numtotal']]

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
numberOfRows = len(casesPerDay)
for date in dates:
    places = []
    cases = []
    for cpd in range(c,numberOfRows,1):
        if casesPerDay['date'][c] == date:
            places.append(casesPerDay['prname'][c].lower())
            cases.append(casesPerDay['numtotal'][c])
            c+=1
        else:
            break
    
    
    # Fill province arrays with total cases in respective provinces
    ontario.append(cases_stat("ontario", places, cases))
    bc.append(cases_stat("british columbia", places, cases))
    pei.append(cases_stat("prince edward island", places, cases))
    ns.append(cases_stat("nova scotia", places, cases))
    nb.append(cases_stat("new brunswick", places, cases))
    quebec.append(cases_stat("quebec", places, cases))
    manitoba.append(cases_stat("manitoba", places, cases))
    saskatchewan.append(cases_stat("saskatchewan", places, cases))
    alberta.append(cases_stat("alberta", places, cases))
    nfld.append(cases_stat("newfoundland and labrador", places, cases))
    yukon.append(cases_stat("yukon", places, cases))
    nt.append(cases_stat("northwest territories", places, cases))
    nunavut.append(cases_stat("nunavut", places, cases))
    rt.append(cases_stat("repatriated travellers", places, cases))
    canada.append(cases_stat("canada", places, cases))
        
    places.clear()
    cases.clear()




# set start and end date
start = pd.to_datetime(dates[0])
end = pd.to_datetime(dates[len(dates) - 1])
dates = pd.date_range(start, end, periods= len(dates))




plt.figure(figsize=(15,10))
plt.plot(dates,ontario,'b-',label="Ontario")
plt.plot(dates,bc,'g-',label="British Columbia")
plt.plot(dates,pei,'r-',label="Prince Edward Island")
plt.plot(dates,ns,'c-',label="Nova Scotia")
plt.plot(dates,nb,'m-',label="New Brunswick")
plt.plot(dates,quebec,'y-',label="Quebec")
plt.plot(dates,manitoba,'k-',label="Manitoba")
plt.plot(dates,saskatchewan,'b-',label="Saskatchewan")
plt.plot(dates,alberta,'b-',label="Alberta")
plt.plot(dates,nfld,'k-',label="Newfoundland and Labrador")
plt.plot(dates,yukon,'b-',label="Yukon")
plt.plot(dates,nt,'r-',label="Northwest Territories")
plt.plot(dates,nunavut,'b-',label="Nunavut")
plt.plot(dates,rt,'b-',label="Repatriated Travellers")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%y'))
plt.xlabel("Dates", fontsize="14")
plt.ylabel("Number of Cases", fontsize="14")
plt.legend()
plt.grid()
plt.title("Number of Total Cases in Each Provinces", fontsize="20", color="blue")
plt.show()