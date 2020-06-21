import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def unique(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result

#Download csv file:
#getting csv data into a pandas dataframe
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
    placesHaveCases = []
    casesOfPlaces = []
    for cpd in range(c,numberOfRows,1):
        if casesPerDay['date'][c] == date:
            placesHaveCases.append(casesPerDay['prname'][c].lower())
            casesOfPlaces.append(casesPerDay['numtotal'][c])
            c+=1
        else:
            break
    
# Fill province arrays with total cases in respective provinces
    ontario.append(case_stats("ontario",places,cases))
    bc.append(case_stats("british columbia",places,cases))
    pei.append(case_stats("prince edward island",places,cases))
    ns.append(case_stats("nova scotia",places,cases))
    nb.append(case_stats("new brunswick",places,cases))
    quebec.append(case_stats("quebec",places,cases))
    manitoba.append(case_stats("manitoba",places,cases))
    saskatchewan.append(case_stats("saskatchewan",places,cases))
    alberta.append(case_stats("alberta",places,cases))
    nfld.append(case_stats("newfoundland and labrador",places,cases))
    yukon.append(case_stats("yukon",places,cases))
    nt.append(case_stats("northwest territories",places,cases))
    nunavut.append(case_stats("nunavut",places,cases))
    rt.append(case_stats("repatriated travellers",places,cases))
    canada.append(case_stats("canada",places,cases))
        
    places.clear()
    cases.clear()