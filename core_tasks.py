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




def cases_stat(place,placeArray,caseArray):
    if place in placeArray:
        if math.isnan(caseArray[placeArray.index(place)]):
            return 0
        else:
            return caseArray[placeArray.index(place)]
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




plotName = sys.argv[1]
placeName = sys.argv[2]
if len(sys.argv) > 3: 
	plotType = sys.argv[3]
else: 
	plotType = "line"




#Download csv file:
#Getting csv data into a pandas dataframe
data = pd.read_csv('https://health-infobase.canada.ca/src/data/covidLive/covid19.csv',sep=',')
dates = unique(data['date'])


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


if plotName == "total_cases":
    totalCases = data[['prname', 'date', 'numtotal']]
    numberOfRows = len(totalCases)

elif plotName == "total_tested":
    totalTested = data[['prname', 'date', 'numtested']]
    numberOfRows = len(totalTested)

elif plotName == "cases_per_day":
    casePerDay = data[['prname', 'date', 'numtoday']]
    numberOfRows = len(casePerDay)


c = 0
places = []
cases = []
for date in dates:
    for i in range(c,numberOfRows,1):
        if plotName == "total_cases":
            if totalCases['date'][c] == date:
                places.append(totalCases['prname'][c].lower())
                cases.append(totalCases['numtotal'][c])
                c+=1
            else:
                break

        elif plotName == "total_tested":
            if totalTested['date'][c] == date:
                places.append(totalTested['prname'][c].lower())
                cases.append(totalTested['numtested'][c])
                c+=1
            else:
                break

        elif plotName == "cases_per_day":
            if casesPerDay['date'][c] == date:
                places.append(casesPerDay['prname'][c].lower())
                cases.append(casesPerDay['numtoday'][c])
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
start = pd.to_datetime(dates[0], dayfirst=True)
end = pd.to_datetime(dates[len(dates) - 1], dayfirst=True)
dates = pd.date_range(start, end, periods=len(dates))




# setting cutoff points
if plotName == "cases_per_day":
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

if plotType == "bar":
    plt.style.use('ggplot')
    if placeName.lower() == "ontario":
    	plt.bar(dates, ontario, color='#D35400', width=1, edgecolor='black', label="Ontario")
    
    elif placeName.lower() == "british_columbia":
    	plt.bar(dates, bc, color='#FF8850', width=1, edgecolor='black', label="British Columbia")
    
    elif placeName.lower() == "prince_edward_island":
    	plt.bar(dates, pei, color='#FFD500', width=1, edgecolor='black', label="Prince Edward Island")
    
    elif placeName.lower() == "nova_scotia":
    	plt.bar(dates, ns, color='#5FA30D', width=1, edgecolor='black', label="Nova Scotia")
    
    elif placeName.lower() == "new_brunswick":
    	plt.bar(dates, nb, color='#15F518', width=1, edgecolor='black', label="New Brunswick")
    
    elif placeName.lower() == "quebec":
    	plt.bar(dates, quebec, color='#00FFF7', width=1, edgecolor='black', label="Quebec")
    
    elif placeName.lower() == "manitoba":
    	plt.bar(dates, manitoba, color='#00A2FF', width=1, edgecolor='black', label="Manitoba")
    
    elif placeName.lower() == "saskatchewan":
    	plt.bar(dates, saskatchewan, color='#001BFF', width=1, edgecolor='black', label="Saskatchewan")
    
    elif placeName.lower() == "alberta":
    	plt.bar(dates, alberta, color='#C900FF', width=1, edgecolor='black', label="Alberta")
    
    elif placeName.lower() == "newfoundland_and_labrador":
    	plt.bar(dates, nfld, color='#FF00E4', width=1, edgecolor='black', label="Newfoundland and Labrador")
    
    elif placeName.lower() == "yukon":
    	plt.bar(dates, yukon, color='#935116', width=1, edgecolor='black', label="Yukon")
    
    elif placeName.lower() == "northwest_territories":
    	plt.bar(dates, nt, color='#839192', width=1, edgecolor='black', label="Northwest Territories")
    
    elif placeName.lower() == "nunavut":
    	plt.bar(dates, nunavut, color='#000000', width=1, edgecolor='black', label="Nunavut")
    
    elif placeName.lower() == "repatriated_travellers":
    	plt.bar(dates, rt, color='#FF0000', width=1, edgecolor='black', label="Repatriated Travellers")
    
    else:
    	plt.bar(dates, ontario, color='#D35400', width=1, edgecolor='black', label="Ontario")
    	plt.bar(dates, bc, color='#FF8850', width=1, edgecolor='black', label="British Columbia")
    	plt.bar(dates, pei, color='#FFD500', width=1, edgecolor='black', label="Prince Edward Island")
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


elif plotType == "line":
    if placeName.lower() == "ontario":
    	plt.plot(dates, ontario, color='#D35400', label="Ontario")
    
    elif placeName.lower() == "british_columbia":
    	plt.plot(dates, bc, color='#FF8850', label="British Columbia")
    
    elif placeName.lower() == "prince_edward_island":
    	plt.plot(dates, pei, color='#FFD500', label="Prince Edward Island")
    
    elif placeName.lower() == "nova_scotia":
    	plt.plot(dates, ns, color='#5FA30D', label="Nova Scotia")
    
    elif placeName.lower() == "new_brunswick":
    	plt.plot(dates, nb, color='#15F518', label="New Brunswick")
    
    elif placeName.lower() == "quebec":
    	plt.plot(dates, quebec, color='#00FFF7', label="Quebec")
    
    elif placeName.lower() == "manitoba":
    	plt.plot(dates, manitoba, color='#00A2FF', label="Manitoba")
    
    elif placeName.lower() == "saskatchewan":
    	plt.plot(dates, saskatchewan, color='#001BFF', label="Saskatchewan")
    
    elif placeName.lower() == "alberta":
    	plt.plot(dates, alberta, color='#C900FF', label="Alberta")
    
    elif placeName.lower() == "newfoundland_and_labrador":
    	plt.plot(dates, nfld, color='#FF00E4', label="Newfoundland and Labrador")
    
    elif placeName.lower() == "yukon":
    	plt.plot(dates, yukon, color='#935116', label="Yukon")
    
    elif placeName.lower() == "northwest_territories":
    	plt.plot(dates, nt, color='#839192', label="Northwest Territories")
    
    elif placeName.lower() == "nunavut":
    	plt.plot(dates, nunavut, color='#000000', label="Nunavut")
    
    elif placeName.lower() == "repatriated_travellers":
    	plt.plot(dates, rt, color='#FF0000', label="Repatriated Travellers")

    else:
    	plt.plot(dates, ontario, color='#D35400', label="Ontario")
    	plt.plot(dates, bc, color='#FF8850', label="British Columbia")
    	plt.plot(dates, pei, color='#FFD500', label="Prince Edward Island")
    	plt.plot(dates, ns, color='#5FA30D', label="Nova Scotia")
    	plt.plot(dates, nb, color='#15F518', label="New Brunswick")
    	plt.plot(dates, quebec, color='#00FFF7', label="Quebec")
    	plt.plot(dates, manitoba, color='#00A2FF', label="Manitoba")
    	plt.plot(dates, saskatchewan, color='#001BFF', label="Saskatchewan")
    	plt.plot(dates, alberta, color='#C900FF', label="Alberta")
    	plt.plot(dates, nfld, color='#FF00E4', label="Newfoundland and Labrador")
    	plt.plot(dates, yukon, color='#935116', label="Yukon")
    	plt.plot(dates, nt, color='#839192', label="Northwest Territories")
    	plt.plot(dates, nunavut, color='#000000', label="Nunavut")
    	plt.plot(dates, rt, color='#FF0000', label="Repatriated Travellers")


plt.xlabel("Dates", fontsize="14")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%y'))
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.legend()

if plotType == "line":
	plt.grid()
elif plotType == "bar":
	plt.grid(color='w', linestyle='solid')

if plotName == "total_cases": 
	plt.ylabel("Number of Total Cases", fontsize="14")
	plt.title("Number of Total Cases over Time", fontsize="20", color="black")

elif plotName == "total_tested": 
	plt.ylabel("Number of Tests", fontsize="14")
	plt.title("Number of Tests over Time", fontsize="20", color="black")

elif plotName == "cases_per_day": 
	plt.ylabel("Number of New Cases", fontsize="14")
	plt.title("Number of New Cases over Time", fontsize="20", color="black")

plt.show()