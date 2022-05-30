# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:04:42 2021

@author: ali_d
"""

#Hızlı Baslangıc


import pandas as pd

import numpy as np

import matplotlib.pyplot as plt



# Nesne Oluşturma
s = pd.Series([1,2,3,5,np.nan,7,8])

print(s)

print()

dates = pd.date_range(20130101,periods=6)
print(dates)


df = pd.DataFrame(np.random.randn(6,4),index=dates)

print(df)

print("-"*30)
#%%
df2 = pd.DataFrame({"A":1.0,
                    "B": pd.Timestamp("20130102"),
                    "C": pd.Series(1,index=list(range(4)),dtype="float32"),
                    "D": np.array([3]*4,dtype="int32"),
                    "E": pd.Categorical(["test","train","test","train"]),
                    "F":"foo"})

print(df2)
print("-"*30)

print(df2.dtypes)

#data yapısı

#Verileri Görüntüleme

print(df2.head())
#
print()
#
print(df2.tail(3))
#
print()
#
print(df2.index)
#
print()
#
print(df2.columns)
#
print()
#
print(df2.values)
#
print("-"*30)
#
print(df2.describe())
#verilerinizin hızlı bir istatistik özetini gösterir
#
print("-"*40)


#Verilerinizi transpoze etme:

a = (df2.T)
#Verilerinizi transpoze ettik
print(a)

#Bir eksene göre sıralıyalım

s1 = (df2.sort_index(axis=1, ascending=False))
s2 = (df2.sort_index(axis=0,ascending=True))

print("-"*30)
#%%

dates = pd.date_range(20130101,periods=6)

df = pd.DataFrame(np.random.randn(6,4),index=dates)

print(df)

#Değerlere göre sıralama

s3 = df.sort_values(by=2)

s3 = df.sort_values(by=1)

s3 = df.sort_values(by=3)

#%% Seçmek
# at, .iat, .loc, .iloc ve .ix 
# Alma
print(df2["A"])
print(df2.A)
print()

#Satırları dilimleyerek [] ile seçme.

print(df2[0:2])
print("-"*30)

#Etiket Seçimi

print(df.loc[dates[0]])
print()
print(df.loc[dates[1]])
print()

#Etikete göre çok eksenli seçme
print(df.loc[:,[1,2]])
print(df.loc[:,[0,3]])

print()

#%% Pozisyona Göre Seçme

data = {"one":[1,2,3,4,5],
        "two":[6,7,8,9,10],
        "three":[11,12,13,14,15],
        "four":[16,17,18,19,20]}

DataX = pd.DataFrame(data=data)

print(DataX)

print("-"*30)
#print(DataX.loc["one"])
print()
print(DataX.iloc[1])
#
print()


#
print(DataX.iloc[2:4,0:2])
#
print("-"*30)

print(DataX.iloc[0:2])
#0ve 2harıc gerı kalanları alıyıorum

print("-"*30)
#
print(DataX.iloc[0:2,0:2])
print("-"*30)
#
print(DataX.iloc[0:2,:4])
#0dan 2 hariç geri kalanları alkıyorum
#4de kadar olan tum columns ları alıyorum

#
print("-"*40)

print(DataX.iloc[[1,2,3],[0,2]])
print("-"*30)

#
print(DataX.iloc[[3,4],[3]])
#
print("-"*30)
print(DataX.iloc[[3],[3]])
print()

#
print(DataX.iloc[:,1:3])

#%% Boolean Dizi Oluşturma

print(DataX[DataX.one >0])

#
print()

print(DataX[DataX.two>1])

print()

print(DataX[DataX > 0])

print(DataX[DataX > 1])

print(DataX[DataX > 3])
print(DataX[DataX > 10])
print(DataX[DataX > 14])
print(DataX[DataX > 16])
print(DataX[DataX > 20])

print("-"*30)




    































































































