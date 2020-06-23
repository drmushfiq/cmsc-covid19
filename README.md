# CMSC 6950 Project
==================================================

About
-----

The repository contains two types of programs - plotting and predicting. Each of these has two program files. The first plotting program can be used to plot total number of covid19 cases, total tests and number of cases per day in different provinces of Canada. The second one plots total cases over time but animates the plot. The repository also contains two program - one to predict when the total number of cases/deaths will be doubled given a province name and a date and the other one predicts what will be the number of cases after 14 days of a given date as input. 

All plots and predictions were made using the csv file available in the government website of Canada. No other parameters were taken into account.

Run the programs
-----------

Clone the git repository with:

``git clone https://github.com/drmushfiq/cmsc-covid19``

cd to the cmsc-covid19 directory:
``cd cmsc-covid19``

- Graph Plotting:
  - Run ``python3 plots.py <whatToplot> <nameOfProvince(s)> <plotType>``
  - whatToPlot: choose one of the three values 
  		- total_cases / total_tested / cases_per_day
  - nameOfProvince(s): choose any of the following(s) 
  		- ontario / british_columbia / prince_edward_island / nova_scotia / new_brunswick / quebec / manitoba / saskatchewan / alberta / newfoundland_and_labrador / yukon / northwest_territories / nunavut / repatriated_travellers 
  		- To plot cases of only one province - choose only one of these values
  		- To plot cases of more than one provinces - choose mutiple values separated by comma
  		- To plot cases of all provinces - type "all" instead
  - plotType: line / bar
  		- if bar is selected, bar graph is plotted
  		- if line is selected or left empty, line graph is plotted. Default is line graph
  - Example commands:
	  - $ python3 plots.py total_cases all line
	  - $ python3 plots.py total_cases manitoba bar
	  - $ python3 plots.py total_cases newfoundland_and_labrador,new_brunswick,saskatchewan line

- Animate Plots:
  - This program is used to display plot with animation
  - Run ``python3 animate.py <nameOfProvince>``
  - nameOfProvince(s): choose any of the following(s) 
  		- ontario / british_columbia / prince_edward_island / nova_scotia / new_brunswick / quebec / manitoba / saskatchewan / alberta / newfoundland_and_labrador / yukon / northwest_territories / nunavut / repatriated_travellers 
  		- You can only choose one province 
  		- You cannot use "all" or type multiple provinces in this program
  - Example commands:
	  - $ python3 animate.py ontario
	  - $ python3 animate.py alberta 

 - Doubling rate
 	- Run ``python3 task5.py <codeOfProvince> <cases/death> <date>``
 		- codeOfProvince: choose one of the followings: (NL,PE,NS,NB,QC,ON,MB,SK,AB,YT,BC,NT,NU)
	- Takes 3 arguments: Province code, whether to check for number of cases or deaths, Date
	- Check "storage.txt" for result
	- Example: ``python3 task5.py ON cases 08-04-2020``

 - Plotting the doubling rate
 	- Run ``task6.py``
	- Does not require any arguments to run. It rather uses the 'storage.txt' file generated from task 5 and creates a bar graph with all instances of data that are in the storage.txt file. 

 - 14days.py:
 	- Run ``python3 task5.py <codeOfProvince> <cases/death> <date>``
 		- codeOfProvince: choose one of the followings: (NL,PE,NS,NB,QC,ON,MB,SK,AB,YT,BC,NT,NU)
 	- Takes 3 arguments: Province code, whether to check for number of cases or deaths, Date
 	- Provide the prediction of cases/death after 14 days of the given date 
	- Check "storage.txt" for result
	- Example: ``python3 14days.py ON cases 08-04-2020``
