#importing modules
import sys
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates



# ----------------------------------- Functions Section Start ----------------------------------- #
def unique(arr):
    ''' 
    takes an array as input and creates a new array from its unique values
    returns the array with unique values
    '''
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result




def cases_stat(province,provinceArray,caseArray):
    ''' 
    takes 3 input
        - name of the province 
        - full column of province name of the csv file
        - full column of cases of the csv file
            - caseArray can be many type depending on what is passed as parameter: cases of today/total cases/total tests etc
    returns the value of the cell where the province name is equal to the province sent as parameter
        - if province name is not equal to the province provided as parameter, the function returns 0 
        - if cell value is empty or contains non-integer information, the function returns 0
    '''
    if province in provinceArray:
        if math.isnan(caseArray[provinceArray.index(province)]):
            return 0
        else:
            return caseArray[provinceArray.index(province)] 
    else: 
        return 0   




def set_cutoff(arr, cutoff):
    '''
    - takes an array and cutoff point as input
    - sets all the values to 0 until the cutoff point is reached
    - keeps the values as it is once the cutoff point is reached
    '''
    foundCutoff = False  
    result = []
    for i in arr:
        if foundCutoff == False:  
            if i < cutoff:  
                result.append(0)
            else:
                result.append(i)
                foundCutoff = True
        else:
            result.append(i)
    return result
# ------------------------------------ Functions Section End ------------------------------------ #




# ----------------------------- Fetch Parameter from Console Starts ------------------------------ #
plotName = sys.argv[1]
placesList = []
if len(sys.argv) > 2: 
    # split string by comma and put the comma separated elements in an array
	placesList = sys.argv[2].split(",")       
	for i in range(0,len(placesList),1):
		placesList[i] = placesList[i].strip()     # remove whitespaces from array element

if len(sys.argv) > 3: 
	plotType = sys.argv[3]                         # set plot type as per the user input
else: 
	plotType = "line"                              # set plot type as line plot as default
# ------------------------------ Fetch Parameter from Console End ------------------------------- #




data = pd.read_csv('https://health-infobase.canada.ca/src/data/covidLive/covid19.csv',sep=',')          #Download csv file
dates = unique(data['date'])                                                                            # get unique date from dataframe


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




# --------------------------------- Create array depending on what to plot --------------------------------- #
if plotName == "total_cases":
    totalCases = data[['prname', 'date', 'numtotal']]
    numberOfRows = len(totalCases)

elif plotName == "total_tested":
    totalTested = data[['prname', 'date', 'numtested']]
    numberOfRows = len(totalTested)

elif plotName == "cases_per_day":
    casesPerDay = data[['prname', 'date', 'numtoday']]
    numberOfRows = len(casesPerDay)
# --------------------------------- Create array depending on what to plot --------------------------------- #




c = 0
places = []
cases = []
'''
Go through each data
find the number of total cases/total tests/new cases of that day for each province
append the number in the array of each province according to the number of cases of that province
at the end, each province array contains the number of cases of each day in that province
'''
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

    # clear both arrays for next iteration
    places.clear()
    cases.clear()
            



# -------------------------------- Convert dates from string type to datetime type -------------------------------- #
start = pd.to_datetime(dates[0], dayfirst=True)
end = pd.to_datetime(dates[len(dates) - 1], dayfirst=True)
dates = pd.date_range(start, end, periods=len(dates))
# -------------------------------- Convert dates from string type to datetime type -------------------------------- #




# ---------------------------------- Set cuttoff points for each province starts ---------------------------------- #
# execute this part only while plotting cases per day as it requires a cutoff point
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
# ------------------------------------ Set cuttoff points for each province end ----------------------------------- #
                    



# ----------------------------------------------- Plot data starts ------------------------------------------------ #

plottedYVals = []               # this array contains the highest y val for each province that are being plotted

fig = plt.figure(figsize=(10,10))

#if plotting bar type
if plotType == "bar":
    plt.style.use('ggplot')
    if "ontario" in placesList:
    	plt.bar(dates, ontario, color='#D35400', width=1, edgecolor='black', label="Ontario")
    	plottedYVals.append(max(ontario))
    
    if "british_columbia" in placesList:
    	plt.bar(dates, bc, color='#FF8850', width=1, edgecolor='black', label="British Columbia")
    	plottedYVals.append(max(bc))
    
    if "prince_edward_island" in placesList:
    	plt.bar(dates, pei, color='#FFD500', width=1, edgecolor='black', label="Prince Edward Island")
    	plottedYVals.append(max(pei))
    
    if "nova_scotia" in placesList:
    	plt.bar(dates, ns, color='#5FA30D', width=1, edgecolor='black', label="Nova Scotia")
    	plottedYVals.append(max(ns))
    
    if "new_brunswick" in placesList:
    	plt.bar(dates, nb, color='#15F518', width=1, edgecolor='black', label="New Brunswick")
    	plottedYVals.append(max(nb))
    
    if "quebec" in placesList:
    	plt.bar(dates, quebec, color='#00FFF7', width=1, edgecolor='black', label="Quebec")
    	plottedYVals.append(max(quebec))
    
    if "manitoba" in placesList:
    	plt.bar(dates, manitoba, color='#00A2FF', width=1, edgecolor='black', label="Manitoba")
    	plottedYVals.append(max(manitoba))
    
    if "saskatchewan" in placesList:
    	plt.bar(dates, saskatchewan, color='#001BFF', width=1, edgecolor='black', label="Saskatchewan")
    	plottedYVals.append(max(saskatchewan))
    
    if "alberta" in placesList:
    	plt.bar(dates, alberta, color='#C900FF', width=1, edgecolor='black', label="Alberta")
    	plottedYVals.append(max(alberta))
    
    if "newfoundland_and_labrador" in placesList:
    	plt.bar(dates, nfld, color='#FF00E4', width=1, edgecolor='black', label="Newfoundland and Labrador")
    	plottedYVals.append(max(nfld))
    
    if "yukon" in placesList:
    	plt.bar(dates, yukon, color='#935116', width=1, edgecolor='black', label="Yukon")
    	plottedYVals.append(max(yukon))
    
    if "northwest_territories" in placesList:
    	plt.bar(dates, nt, color='#839192', width=1, edgecolor='black', label="Northwest Territories")
    	plottedYVals.append(max(nt))
    
    if "nunavut" in placesList:
    	plt.bar(dates, nunavut, color='#000000', width=1, edgecolor='black', label="Nunavut")
    	plottedYVals.append(max(nunavut))
    
    if "repatriated_travellers" in placesList:
    	plt.bar(dates, rt, color='#FF0000', width=1, edgecolor='black', label="Repatriated Travellers")
    	plottedYVals.append(max(rt))
    
    if "all" in placesList or len(placesList) == 0:
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

        # get maximum values of y axis for each province
    	plottedYVals.append(max(max(ontario), max(bc), max(pei), max(ns), max(nb), max(quebec), max(manitoba), 
		  max(saskatchewan), max(alberta), max(nfld), max(yukon), max(nt), max(nunavut), max(rt)))


# if plotting line type
elif plotType == "line":
    if "ontario" in placesList:
    	plt.plot(dates, ontario, color='#D35400', marker="o", label="Ontario")
    	plottedYVals.append(max(ontario))
    
    if "british_columbia" in placesList:
    	plt.plot(dates, bc, color='#FF8850', marker="o", label="British Columbia")
    	plottedYVals.append(max(bc))
    
    if "prince_edward_island" in placesList:
    	plt.plot(dates, pei, color='#FFD500', marker="o", label="Prince Edward Island")
    	plottedYVals.append(max(pei))
    
    if "nova_scotia" in placesList:
    	plt.plot(dates, ns, color='#5FA30D', marker="o", label="Nova Scotia")
    	plottedYVals.append(max(ns))
    
    if "new_brunswick" in placesList:
    	plt.plot(dates, nb, color='#15F518', marker="o", label="New Brunswick")
    	plottedYVals.append(max(nb))
    
    if "quebec" in placesList:
    	plt.plot(dates, quebec, color='#00FFF7', marker="o", label="Quebec")
    	plottedYVals.append(max(quebec))
    
    if "manitoba" in placesList:
    	plt.plot(dates, manitoba, color='#00A2FF', marker="o", label="Manitoba")
    	plottedYVals.append(max(manitoba))
    
    if "saskatchewan" in placesList:
    	plt.plot(dates, saskatchewan, color='#001BFF', marker="o", label="Saskatchewan")
    	plottedYVals.append(max(saskatchewan))
    
    if "alberta" in placesList:
    	plt.plot(dates, alberta, color='#C900FF', marker="o", label="Alberta")
    	plottedYVals.append(max(alberta))
    
    if "newfoundland_and_labrador" in placesList:
    	plt.plot(dates, nfld, color='#FF00E4', marker="o", label="Newfoundland and Labrador")
    	plottedYVals.append(max(nfld))
    
    if "yukon" in placesList:
    	plt.plot(dates, yukon, color='#935116', marker="o", label="Yukon")
    	plottedYVals.append(max(yukon))
    
    if "northwest_territories" in placesList:
    	plt.plot(dates, nt, color='#839192', marker="o", label="Northwest Territories")
    	plottedYVals.append(max(nt))
    
    if "nunavut" in placesList:
    	plt.plot(dates, nunavut, color='#000000', marker="o", label="Nunavut")
    	plottedYVals.append(max(nunavut))
    
    if "repatriated_travellers" in placesList:
    	plt.plot(dates, rt, color='#FF0000', marker="o", label="Repatriated Travellers")
    	plottedYVals.append(max(rt))

    if "all" in placesList or len(placesList) == 0:
    	plt.plot(dates, ontario, color='#D35400', marker="o", label="Ontario")
    	plt.plot(dates, bc, color='#FF8850', marker="o", label="British Columbia")
    	plt.plot(dates, pei, color='#FFD500', marker="o", label="Prince Edward Island")
    	plt.plot(dates, ns, color='#5FA30D', marker="o", label="Nova Scotia")
    	plt.plot(dates, nb, color='#15F518', marker="o", label="New Brunswick")
    	plt.plot(dates, quebec, color='#00FFF7', marker="o", label="Quebec")
    	plt.plot(dates, manitoba, color='#00A2FF', marker="o", label="Manitoba")
    	plt.plot(dates, saskatchewan, color='#001BFF', marker="o", label="Saskatchewan")
    	plt.plot(dates, alberta, color='#C900FF', marker="o", label="Alberta")
    	plt.plot(dates, nfld, color='#FF00E4', marker="o", label="Newfoundland and Labrador")
    	plt.plot(dates, yukon, color='#935116', marker="o", label="Yukon")
    	plt.plot(dates, nt, color='#839192', marker="o", label="Northwest Territories")
    	plt.plot(dates, nunavut, color='#000000', marker="o", label="Nunavut")
    	plt.plot(dates, rt, color='#FF0000', marker="o", label="Repatriated Travellers")
        
        # get maximum values of y axis for each province
    	plottedYVals.append(max(max(ontario), max(bc), max(pei), max(ns), max(nb), max(quebec), max(manitoba), 
    			  max(saskatchewan), max(alberta), max(nfld), max(yukon), max(nt), max(nunavut), max(rt)))




# set grid type depending on the type of plot
if plotType == "line":
	plt.grid()
elif plotType == "bar":
	plt.grid(color='w', linestyle='solid')

# set plot title and axis labels depending on what is being plotted
if plotName == "total_cases": 
	plt.title("Number of Total Cases over Time", fontsize="20", color="black")
	plt.ylabel("Number of Total Cases", fontsize="14")

elif plotName == "total_tested": 
	plt.title("Number of Tests over Time", fontsize="20", color="black")
	plt.ylabel("Number of Tests", fontsize="14")

elif plotName == "cases_per_day": 
	plt.title("Number of New Cases over Time", fontsize="20", color="black")
	plt.ylabel("Number of New Cases", fontsize="14")


plt.xlabel("Dates", fontsize="14")
plt.xticks(rotation=45)                                                         # rotate x ticks by 45deg
plt.ylim(ymin=0)                                                                # y axis starts from zero
yTickHighestValue = int(math.ceil(max(plottedYVals) / 10.0)) * 10               # get the highest value of all provinces on y axis 
yTickHighestValue += yTickHighestValue/10                                       # add one more tick as the initial tick starts from 0
yTicks = np.arange(0,yTickHighestValue,yTickHighestValue/10)                    # create an array from 0 to highest y with stepsize yMax/10
plt.yticks(np.round(yTicks))                                                    # set 10 ticks on y axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%y'))           # format date on x axis
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)             # remove scientific notation from y axis and use plain numbers
plt.legend()
plt.show()
# -------------------------------------------------- Plot data end --------------------------------------------------- #