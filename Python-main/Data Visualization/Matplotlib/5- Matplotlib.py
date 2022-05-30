# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 22:31:29 2021

@author: ali_d
"""
#5

#Scatter Plots

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.image as mpimg


#Scatter Plots

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x, y, label="skitscat Raggedy",color="k",s=25,marker="o")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Interesting Graph\nCheck it out")
plt.legend()
plt.show()




#%%Stack Plots

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]

plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nStack Plots')
plt.show()


#%%

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]


plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)

plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()


#%%





















