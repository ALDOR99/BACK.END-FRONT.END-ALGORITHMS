# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:59:31 2021

@author: ali_d
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from subprocess import check_output


data = pd.read_csv("pokemon.csv")

print(data.head())
#ilk 5 data incelemesi

print(data.columns)
#datamın sütunlarının isimlerinin isimlerini verir
print()

print(data.shape)
#satır ve sutun sayısımı verir
print()


print(data.info())
#datamın bilgisini verir
print()

#%%Exploratory data analysis (EDA)

print(data['Type 1'].value_counts(dropna =False))
#

a = (data.describe())
print()
print(data.describe)
print()

b=(data.corr())
print()

#correlation map
f,ax =plt.subplots(figsize =(9,9))
sns.heatmap(data.corr(), annot=True, linewidths=.5,fmt =".1f",ax=ax)
plt.show()
#%%Visual exploratory data analysis

data.boxplot(column="Attack",by="Legendary")
plt.show()

#%% Tidy data

data_new = data.head()
print(data_new)

melted = pd.melt(frame=data_new,id_vars = 'Name', value_vars= ['Attack','Defense'])
print(melted)

print()

melted2 = pd.melt(frame=data_new,id_vars="Name",value_vars=["HP","Speed"])
print(melted2)
print()
#%% Pivoting data

print(melted.pivot(index ="Name",columns="variable",values="value"))

print()

print(melted2.pivot(index ="Name",columns="variable",values="value"))


#%%Concatenating data

data1 = data.head()

data2 = data.tail()


conc_data_row =  pd.concat([data1,data2],axis=0,ignore_index=True)


print(conc_data_row)
print()


#%%

data1 = data['Attack'].head()
data2= data['Defense'].head()

conc_data_col = pd.concat([data1,data2],axis=1)
print(conc_data_col)

print()
conc_data_col = pd.concat([data1,data2],axis=0)
print(conc_data_col)
print()
#%%Data types


print(data.dtypes)
print()

#%% Missing data and testing with assert

print(data["Type 2"].value_counts(dropna=False))
print(data["Type 2"].value_counts(dropna=True))
#nan olan verileri göstermez

data1 = data.copy()

data1["Type 2"].dropna(inplace = True)

data1["Type 2"].fillna("Xman",inplace = True)

#%% Manipulating Data Frames with Pandas

#Index objects and labeled data

data = data.set_index("#")
#%%
print(data.index.name)
print(data.columns.name)
print()

data.index.name = "index_name"
print(data.head())

data3 = data.copy()

data3.index = range(100,900,1)
print(data3.head())

#%% Hierarchical indexing

data1 = data.set_index(["Type 1","Type 2"])
print(data1.head())

#%% Pivoting data frames

melted.pivot(index = "Name",columns="variable",values="value")

#%% Concatenating data

data1 = data.head()
data2 = data.tail()

conc_data_row = pd.concat([data1,data2],axis = 0,ignore_index = True)
print(conc_data_row)
print()


data1 = data["Attack"].head()
data2 = data["Defense"].head()

conc_data_col = pd.concat([data1,data2],axis = 1)

print(conc_data_col)


lg1 = data["Speed"].tail(3)
lg2 = data["Legendary"].tail(3)

brl_data_col = pd.concat([lg1,lg2],axis=1)
print(brl_data_col)

#%% Data types

# data['Type 1'] = data['Type 1'].astype('category')
# data['Speed'] = data['Speed'].astype('float')


print(data.dtypes)

#%%Missing data and testing with assert

data["Type 2"].value_counts(dropna =False) 



#%% Manipulating Data Frames with Pandas

#Index objects and labeled data

data= data.set_index("#")

print(data.index.name)
data.index.name = "index_name" # lets change it
data.head()

#%%

print(data.head())

ll = data.copy()

ll.index = range(100,900,1)
print(ll.head())




































