#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Due February 28, 2020
Created on Wed Feb 26 15:10:08 2020
by Hannah Walcek
Assignment 06 - Graphing Data with Python

This python program reads in a data file and generates summary figures for 
that file.
"""
#importing necessary packages
import numpy as np
import matplotlib.pyplot as plt
import sys

#assigning text file information to data and ensuring columns are labelled
#sys.argv[1] is the command line argument for the first value which will be the
#desired text file
data = np.genfromtxt(sys.argv[1],
                        names = True)

#subplot function allows multiple plots (in this case 3) to be placed in the
#same area
plt.subplot(3,1,1)
#first plot which generates Mean, Max, and Min streamflow in the colors black,
#red, and blue respectively
plt.plot(data['Year'], data['Mean'], color = 'black', label = 'Mean')
plt.plot(data['Year'], data['Max'], color = 'red', label = 'Max')
plt.plot(data['Year'], data['Min'], color = 'blue', label = 'Min')
#labelling the y axis
plt.ylabel('Streamflow (cfs)')
#creating legend
plt.legend()

#second plot which generates tqmean with grean triangles
plt.subplot(3,1,2)
plt.plot(data['Year'], data['Tqmean']*100, 'g^')
#labelling the y axis
plt.ylabel('Tqmean (%)')

#third plot which shows the R-B Index in bar form
plt.subplot(3,1,3)
plt.bar(data['Year'], data['RBindex'])
#labelling the y axis
plt.ylabel('R-B Index (ratio)')
#labelling the x axis
plt.xlabel('Year')

#saves figure to pdf of the user's choosing
plt.savefig(sys.argv[2])