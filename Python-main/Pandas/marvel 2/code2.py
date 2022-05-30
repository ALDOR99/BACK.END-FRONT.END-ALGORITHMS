# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 10:41:09 2021

@author: ali_d
"""

#code 2

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv("marvel_characters_info.csv")

print(df.head())
#%%

df1 = pd.read_csv("marvel_characters_info.csv",skiprows=[1])
#ilk satırı atlamak ıcın kullanılır
#%%
df2 = pd.read_csv("marvel_characters_info.csv",skiprows=[0])


print(df.columns)
#%%

df3 = pd.read_csv("marvel_characters_info.csv",header=None)
#%%
#Veri Filtreleme


male = df[df["Gender"] == "Male"]
#
power = male[male["EyeColor"] =="blue"]
#
height = power[power["Height"]>=191]
#
heir =  height[height["HairColor"]=="Blond"]
print()

# Eşsiz verileri alma
print(df["Gender"].unique())
print("-"*30)

# Birden fazla koşula göre alma
# `()` kullanımlaıdır yoksa `&` işlemi beklendiği gibi çalışmaz

x = df[(df["Height"]>=191) & (df["Weight"]>=400)]
print(x.head())

# Koşulun sonucuna göre `True - False` dizisi döndürür

print(df["Gender"] =="Famele")

print()

print((df["Gender"] =="Famele").head())

print("-"*30)

#
print((df["Gender"] =="Famele").dtype)

print("-"*30)




vb = df[df["Race"].str.contains("Human")]

print(vb.head())


vb1 = df[df["EyeColor"].str.contains("brown")]
#
# Birden fazla değerde arama (regex aramasıdır. | veya demek)

#df32 = df[df['Publisher'].str.contains('|'.join(opioids), case=False)


xq1 = df[df['Gender'].str.lower().isin([x.lower() for x in df])]

#
print("-"*40)



#%% Fonksiyonlar ve Birleştirme İşlemleri

log_review_count = np.log([df["Height"]])
print(log_review_count)

#%% # Ortalama hesaplama (tek değer döndürür)
mean_review_count = df["Height"].mean()
print(mean_review_count)


#%% GroupBy Kullanımı

# stars_by_city = df.groupby("Alignment")
# print(stars_by_city)



sr = df.sort_values("Height")
print(sr.head())

print()


jk=df.set_index("ID").sort_index()
print(jk.head())

print("-"*40)

unique_df = df.sort_values('Height').groupby('Race').last().reset_index()


#%% Veri Kümelerinin Birleştirilmesi


alfa = df["Alignment"] = df["Gender"].apply(lambda x: x)

#%%

alfa1 = df.merge(df, on=['Height', 'Race',"EyeColor"])
print(alfa1)
alfa2 = df.merge(df, on=['Height', 'Race'],how="left")
print()
alfa3 = df.merge(df, on=['Height', 'Race'],how="right")
print()


#%%
print(df["Gender"].unique())
print()

h2 = dict(zip(df['Height'].unique(),list()))

df['Height'] = df['Height'].replace(h2)

"!!!Warning!!!!"

#%%













































