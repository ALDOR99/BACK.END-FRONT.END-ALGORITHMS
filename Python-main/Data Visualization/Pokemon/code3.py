# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:13:25 2021

@author: ali_d
"""
#code3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from subprocess import check_output


data = pd.read_csv("pokemon.csv")


data1 = (data[data["Attack"]>50].head())
data2 = (data[data["Speed"]>90].head())


fig, axes = plt.subplots(nrows=2,ncols=1)
data.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),ax = axes[0])
data.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),ax = axes[1],cumulative = False)
plt.savefig('graph.png')
plt

#%%


fig, axes = plt.subplots(nrows=2,ncols=1)

data.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),ax = axes[0],color="red",grid=True,alpha=0.5)
data.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),ax = axes[1],cumulative = True,alpha=0.9)
#plt.savefig('graph.png')
plt.show()

#%%

print(data.describe())

#%% MANIPULATING DATA FRAMES WITH PANDAS¶


print(data)
print()
print(data["HP"][1])
print(data["HP"][2])
print(data["HP"][3])
print(data["HP"][4])
print()

print(data.loc[1,["HP"]])


# using loc accessor
print(data.loc[2,["HP"]])

print(data.loc[3,["Defense"]])

# Selecting only some columns

#
print(data[["HP","Attack"]])

#%% SLICING DATA FRAME
#dilimleme

a = data.loc[1:10,"HP":"Defense"]

b = data.loc[10:20,"HP":"Defense"]
print(b)


# From something to end
c = data.loc[1:10,"Speed":]

print(c)
print("-"*30)
# FILTERING DATA FRAMES

boolean =data.HP > 200

d  = (data[boolean])
print((data[boolean]))

# Combining filters

first_filter = data.HP>150
second_filter = data.Speed>40
al = data[first_filter & second_filter]
print(al.head())

print("-"*40)

# Filtering column based others
print(data.HP[data.Speed<15])


print(data.loc[495])

print(data.Speed[data.HP<100])

print("-"*30)

#TRANSFORMING DATA


def div(n):
    return n/2
print(data.HP.apply(div))

def aa(m):
    return m/2
print(data.Speed.apply(aa))
print("-"*30)


print(data.HP.apply(lambda n : n/2))

print(data.Attack.apply(lambda c : c/2))

data["total_power"] = data.Attack + data.Defense
print()
print(data.head())










































