# -*- coding: utf-8 -*-
#PC10 
#Monika Sivickaite, Jamie Marriott
# 20//04//15
"""
Created on Wed Apr 15 13:08:43 2020

@author: monika27
Pseudocode
- import libraries
            - matplotlib
            - nummpy
- import csv 
- set a style of the graph
- set up variables
- upload the file:
            - csv format
- read the data
- plot data
- format plot
- show the graph
- 
"""
#import lib
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import csv


# set a default style
style.use ('ggplot')

#set variables
x = [] #making an empty list
y = []

#analyzig data used for plot
with open ('TotalCases.csv') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[1]))
        y.append(int(row[2]))

#plot data      
plt.figure (figsize = (10,5))
plt.plot(x,y, c= 'blue', label = 'Growth of the cases!') #changed color to the blue one because most of the color blind people can't see red, green, yellow and orange

#formating the plot
plt.title("World COVID-19 cases vs the United States")
plt.xlabel('World Cases')
plt.ylabel('United States Cases')
plt.legend()

#show plot
plt.show()

