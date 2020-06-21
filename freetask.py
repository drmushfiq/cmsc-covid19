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