# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 18:40:02 2021

@author: ali_d
"""

import numpy as np
import pandas as pd

from numpy.random import randn

#code 2 
#DataFrame Filtreleme İşlemleri


df = pd.DataFrame(data = randn(4,4),index=["a","b","c","d"],
               columns=["columns1","columns2","columns3","columns4"])

print(df)


#%%

a1 = df>0.2
#koşulu sağlıyorsa ‘True’ değilse ‘False’ değerini döndürür

print(a1)
print()

print(a1[a1])


#%%

a2 = df[df>0.5]

print(df[df>0.5])

#%%
#
a3 = df["columns1"] > 0
print(a3)

print()

a4 = df[df["columns3"] > 0]
print(a4)

print()

a5 = df[df["columns4"]>-0.2]
print(a5)
print()

#
a6 = df[df["columns4"]>-0.4]
print(a6)
#%%
a7 = df[df["columns1"]>0 & (df["columns3"]>0)]

print(a7)

print("-"*40)

a8 = df[df["columns1"]>0 | (df["columns4"] > 1)]

print(a8)
#%%
print(df)

df["columns5"] = ["newvalue1","newvalue2","newvalue3","newvalue4",]

print()
print(df)
print("-"*30)
print(df.set_index("columns5",inplace=True))
#%%
print(df.index.names)
print(type(df.index.names))
#
print(df.columns.names)

#%% Multi İndex

index1 = ["grup1","grup1","grup2","grup2","grup3","grup3"]
index2 = ["index1","index2","index3","index1","index2","index3","index1","index2","index3"]

aa = list(zip(index1,index2))

print(aa)

print()

hierarchy = pd.MultiIndex.from_tuples(aa)
print(hierarchy)


df = pd.DataFrame(randn(6,3),hierarchy,columns = ['Column1','Colum2','Column3'])

print(df)



print()
print(df.xs("grup1"))

#%% Bozuk Ve Kayıp Verilerle Ugraşabilmek
# ‘Not a Number’

arr = np.array([[10,20,np.nan],[3,np.nan,np.nan],[13,np.nan,4]])


df = pd.DataFrame(arr,index=["a","b","c"],columns=["b1","b2","b3"])

print(df)
print()
#print(df.dropna())

a= (df.dropna(axis = 1))
#index satırında en az bir NaN var ise siler

print()
b = df.dropna(thresh=2)
print(b)
# ‘En az iki düzgün veri var ise silme’ anlamına gelmektedir"
print()

print(df.fillna(value = 0))
print()

print(df.sum())
print("-"*30)

print(df.sum().sum())
print()

print(df.fillna(value = (df.sum().sum()/5)))
print()

print(df.size)
#Kaç adet veri olduğunu sorgular.

print(df.isnull().sum())
#‘Hangi ‘Column’da kaç adet ‘NaN’ var
print(df.isnull().sum().sum())
#kac adet nan degerı var

print(df.size - df.isnull().sum())




































































