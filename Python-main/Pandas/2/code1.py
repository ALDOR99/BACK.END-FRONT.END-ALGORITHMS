# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:07:15 2021

@author: ali_d
"""

#Pandas

import pandas as pd
import numpy as np
from numpy.random import randn


#Pandas Serileri


data = np.array(["a","b","c","d"])

series = pd.Series(data,[100,101,102,103])

print(type(series))

#%%

DataDict = {"gorgi":35,"jake":95}
#
a=pd.Series(DataDict)
print(a)

print()

#
DataDict2 = {"fenole":70,"antre":75}
b=pd.Series(DataDict2)
print(b)

print()

#
DataDict3 = {"aldor":100,"uldor":100}
c = pd.Series(DataDict3)
print(c)



print(a+b)
#%%
DataDict4 = c.append(a)
print(DataDict4)

#%%

print(DataDict4["aldor"])

print(DataDict4["uldor"])


#%%Pandas DataFrame

#Column
#Feature
#row
#indeks


df =pd.DataFrame(data = randn(5,5),index=["a","b","c","d","e"],
                 columns=["columns1","columns2","columns3","columns4","columns5"])

print(df)
print()

#
print(df["columns1"])

print()

#
print(df["columns2"])


#%%

df["columns6"] = pd.Series(randn(5),["a","b","c","d","e"])
print(df)


#%%

df["columns7"] = (df["columns6"] + df["columns4"] - df["columns1"]) / df["columns2"] * df["columns3"]

print(df)


#%%Drop

df.drop("columns2",axis=1,inplace=True)

print(df)

#%%

print(df.index.names)
#FrozenList([None])

#%%

print(df.loc["c"])
print()
print(df.loc["a"])
print()
print(df.loc["e"])


#%%
print(df.iloc[0])
print()
print(df.iloc[1])
print()
print(df.iloc[2])
print()
print(df.iloc[3])
print()
#%%

print(df.loc["a","columns5"])
#%%

#df.loc[['a','columns5'] and ['c','columns4']]

#%%



df = pd.DataFrame(data = randn(4,4),index=["a","b","c","d"],
                 columns=["columns1","columns2","columns3","columns4"])

print(df)

a = df.loc[["a","d"],["columns4","columns2"]]

print(a)
























































