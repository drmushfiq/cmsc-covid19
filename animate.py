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




def update(num, x, y, line):
    '''
    Updates the next x and y value in the plot to animate
    '''
    line.set_data(x[:num], y[:num])
    return line,




def animatePlot(xArray,yArray,provinceName):
    '''
    Decorates the plot 
        - sets labels,ticks,title etc
        - runs the animation function
    '''
    fig, ax = plt.subplots(figsize=(10,10))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%y'))
    line, = ax.plot(xArray, yArray, 'g-', label=provinceName)
    plt.title("Number of Total Cases over Time", fontsize="20", color="green")
    plt.xlabel("Dates", fontsize="14")
    plt.ylabel("Number of Total Cases", fontsize="14")
    plt.xticks(rotation=45)                                                         # rotate x ticks by 45deg
    plt.ylim(ymin=0)                                                                # y axis starts from zero
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%y'))           # format date on x axis
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)             # remove scientific notation from y axis and use plain numbers
    plt.legend()
    animation.FuncAnimation(fig, update, len(xArray), fargs=[xArray, yArray, line], interval=20, blit=True, repeat=False)
    plt.show()
# ------------------------------------ Functions Section End ------------------------------------ #




# ----------------------------- Fetch Parameter from Console Starts ------------------------------ #
if len(sys.argv) > 1: placeName = sys.argv[1]                       # get name of the province which will be plotted          
if len(sys.argv) > 2: plotType = sys.argv[2]                         # set plot type as per the user input
else: plotType = "line"                                              # set plot type as line plot as default
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




totalCases = data[['prname', 'date', 'numtotal']]
numberOfRows = len(totalCases)
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
        if totalCases['date'][c] == date:
            places.append(totalCases['prname'][c].lower())
            cases.append(totalCases['numtotal'][c])
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
                    



# ----------------------------------------------- Plot data starts ------------------------------------------------ #
if placeName == "ontario": animatePlot(dates, ontario, "Ontario")
elif placeName == "british_columbia": animatePlot(dates, bc, "British Columbia")
elif placeName == "prince_edward_island": animatePlot(dates, pei, "Prince Edward Island")
elif placeName == "nova_scotia": animatePlot(dates, ns, "Nova Scotia")
elif placeName == "new_brunswick": animatePlot(dates, nb, "New Brunswick")
elif placeName == "quebec": animatePlot(dates, quebec, "Quebec")
elif placeName == "manitoba": animatePlot(dates, manitoba, "Manitoba")
elif placeName == "saskatchewan": animatePlot(dates, saskatchewan, "Saskatchewan")
elif placeName == "alberta": animatePlot(dates, alberta, "Alberta")
elif placeName == "newfoundland_and_labrador": animatePlot(dates, nfld, "Newfoundland And Labrador")
elif placeName == "yukon": animatePlot(dates, yukon, "Yukon")
elif placeName == "northwest_territories": animatePlot(dates, nt, "Northwest Territories")
elif placeName == "nunavut": animatePlot(dates, nunavut, "Nunavut")
elif placeName == "repatriated_travellers": animatePlot(dates, rt, "Repatriated Travellers")
# -------------------------------------------------- Plot data end --------------------------------------------------- #
