#importing modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#------------------------------------DATA PREP----------------------------------------#

#Download csv file:
#Getting csv data into a pandas dataframe
data = pd.read_csv('https://health-infobase.canada.ca/src/data/covidLive/covid19.csv',sep=',')

#Getting stored value from txt file into a pandas dataframe
doublingDays=pd.read_csv("storage.txt", sep=',')

#------------------------------------DATA PREP END-------------------------------------#



