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


def set_cutoff(arr, cutoff):
	foundCutoff = False
	result = []
	for i in arr:
		if i < cutoff:
			if foundCutoff == False:
				result.append(0)
			else:
				result.append(i)
		else:
			result.append(i)
	return result




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


# setting cutoff points
ontario = set_cutoff(ontario, 100)
bc = set_cutoff(bc, 30)
pei = set_cutoff(pei, 15)
ns = set_cutoff(ns, 10)
nb = set_cutoff(nb, 10)
quebec = set_cutoff(quebec, 70)
manitoba = set_cutoff(manitoba, 2)
saskatchewan = set_cutoff(saskatchewan, 4)
alberta = set_cutoff(alberta, 10)
nfld = set_cutoff(nfld, 5)
yukon = set_cutoff(yukon, 2)
nt = set_cutoff(nt, 2)
nunavut = set_cutoff(nunavut, 0)
rt = set_cutoff(rt, 3)
canada = set_cutoff(canada, 40)
                    

# plot results of provinces
fig = plt.figure(figsize=(15,10))
plt.style.use('ggplot')
plt.bar(dates, ontario, color='#D35400', width=1, edgecolor='black', label="Ontario")
plt.bar(dates, bc, color='#FF8850', width=1, edgecolor='black', label="British Columbia")
plt.bar(dates, pei, color='#FFD500', width=1, edgecolor='black',  label="Prince Edward Island")
plt.bar(dates, ns, color='#5FA30D', width=1, edgecolor='black', label="Nova Scotia")
plt.bar(dates, nb, color='#15F518', width=1, edgecolor='black', label="New Brunswick")
plt.bar(dates, quebec, color='#00FFF7', width=1, edgecolor='black', label="Quebec")
plt.bar(dates, manitoba, color='#00A2FF', width=1, edgecolor='black', label="Manitoba")
plt.bar(dates, saskatchewan, color='#001BFF', width=1, edgecolor='black', label="Saskatchewan")
plt.bar(dates, alberta, color='#C900FF', width=1, edgecolor='black', label="Alberta")
plt.bar(dates, nfld, color='#FF00E4', width=1, edgecolor='black', label="Newfoundland and Labrador")
plt.bar(dates, yukon, color='#935116', width=1, edgecolor='black', label="Yukon")
plt.bar(dates, nt, color='#839192', width=1, edgecolor='black', label="Northwest Territories")
plt.bar(dates, nunavut, color='#000000', width=1, edgecolor='black', label="Nunavut")
plt.bar(dates, rt, color='#FF0000', width=1, edgecolor='black', label="Repatriated Travellers")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%y'))
plt.xlabel("Dates", fontsize="14")
plt.ylabel("Number of New Cases", fontsize="14")
plt.legend()
plt.grid(color='w', linestyle='solid')
plt.title("Number of New Cases in Each Provinces", fontsize="20", color="blue")
plt.show()