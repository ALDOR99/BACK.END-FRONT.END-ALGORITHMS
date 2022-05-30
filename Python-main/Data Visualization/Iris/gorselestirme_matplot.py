# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:10:05 2021

@author: ali_d
"""

import numpy as np
import pandas as pd
#
import matplotlib.pyplot as plt

data = pd.read_csv("Iris.csv")



print(data.head())
print()
print(data.tail(10))
#
print(data.corr())
print()

print(data.describe())
#
print(data.info())

print()
print(data["Species"].head(10))
print()
print(data["Species"].unique())
print()

data.tail()
aa=data.columns
####################
#%% Line Plot

data.SepalLengthCm.plot(kind = 'line', color = 'r',label = 'SepalLengthCm',linewidth=1,alpha = 0.9,grid = True,linestyle = '-')

plt.legend(loc='upper right')
plt.xlabel("Id")
plt.ylabel("Sepal Cm")
#bu x eksenimiz
plt.title("Türler arasındaki çanak yaprak uzunluğu kıyaslaması")
#baslıgımızada line plot yazdırdık
plt.show()          




#%%
data.SepalWidthCm.plot(kind = "line",color="b",label="SepalWidthCm",linewidth=1,alpha = 0.9,grid = True,linestyle = '-')
plt.legend()
plt.xlabel("Id")
plt.ylabel("Sepal Cm")
plt.title("Türler arasındaki çanak yaprak genişliği kıyaslaması")
plt.show()
#%%
data.PetalLengthCm.plot(kind="line",color="g",label="PetalLengthCm",linewidth=1,alpha = 0.9,grid = True,linestyle = '-')

plt.legend()
plt.xlabel("Id")
plt.ylabel("Petal Cm")
plt.title("Taç yaprağı uzunluk kıyaslaması")
plt.show()

#%%
data.PetalWidthCm.plot(kind="line",color="black",label="PetalWidthCm",linewidth=1,alpha = 0.9,grid = True,linestyle = '-')
plt.legend()
plt.xlabel("Id")
plt.ylabel("Petal Cm")
plt.title("Taç yaprağı genişlik  kıyaslaması")
plt.show()

#%%
x = [data.SepalLengthCm.plot(kind = 'line', color = 'r',label = 'SepalLengthCm',linewidth=1,alpha = 0.9,grid = True,linestyle = '-'),plt.legend(loc='upper right'),plt.xlabel("Id"),plt.ylabel("Sepal Cm"),plt.title("Türler arasındaki çanak yaprak uzunluğu kıyaslaması"),plt.show()]

y = [data.SepalWidthCm.plot(kind = "line",color="b",label="SepalWidthCm",linewidth=1,alpha = 0.9,grid = True,linestyle = '-'),plt.legend(),plt.xlabel("Id"),plt.ylabel("Sepal Cm"),plt.title("Türler arasındaki çanak yaprak genişliği kıyaslaması"),plt.show()]
#%% scatter
data.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")
#%%

data.plot(kind="scatter",x="PetalLengthCm",y="PetalWidthCm")
plt.show()
#%%

data.plot(kind="scatter",x="PetalLengthCm",y="PetalWidthCm")
data.show()

#%%
data.plot(kind="scatter",x="SepalLengthCm",y="PetalWidthCm",alpha=0.8,grid = True,color="red")
data.show()
#%%




































