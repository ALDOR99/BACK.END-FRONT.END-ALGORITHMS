# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:55:44 2021

@author: ali_d
"""

#Zaman verileri ile çalışma 

import numpy as np
import pandas as pd


# HTML'den veri alma
pop_growth = pd.read_html('https://web.archive.org/web/20170127165708/https://www.census.gov/population/international/data/worldpop/table_population.php', attrs={'class': 'query_table'}, parse_dates=[0])[0]


#null verilerini kaldırma

pop_growth.dropna(inplace=True)
print()

#indeksi yıla gore ayarlarsak resample metodunu kullanabılrız


pop_growth.set_index('Year', inplace=True)

pop_growth.resmple("10AS").mean()


# Kayıp veriler için ototmatik tamamlama yapma

pop_growth.resample('1Q').bfill()
pop_growth.resample('1Q').ffill()

#%%Pandas Zaman Değişkeni (Timestamp)


print(pd.Timestamp('January 8, 2017'))
print(pd.Timestamp('01/08/17 20:13'))
print(pd.Timestamp(1.4839*10**18))
print("-"*30)
# Zamanlar arasında çıkartma yapılabilir (191 days 09:16:00)
print(pd.Timestamp('Feb. 11 2016 2:30 am') - pd.Timestamp('2015-08-03 5:14 pm'))

# Zamanlar arasında gelişmiş hesaplamalar
from pandas.tseries.offsets import BDay, Day, BMonthEnd

print(pd.Timestamp('January 9, 2017') - Day(4)) # Gün
print(pd.Timestamp('January 9, 2017') - BDay(4)) # İş günü (Business day)
print(pd.Timestamp('January 9, 2017') + BMonthEnd(4)) # Aydaki iş bitiş günü

# Zaman aralıkları oluşturma (8 güner arayla zaman oluşturma)
pd.date_range(start='1/8/2017', end='3/2/2017', freq='B')

# Python datetime ile uyumludur
import datetime
pd.Timestamp('May 1, 2017') - datetime.datetime(2017, 1, 8) # Timedelta('113 days 00:00:00')

#!!!!!

#%% Pandas ile Görselleştirme

# 30 çubuklu histogram ile çizme
pop_growth['Annual Population Change'].apply(np.log).hist(bins=30)

# Çizgi grafiği çizdirme
pop_growth['Annual Growth Rate (%)'].plot()


#%%

df = pd.DataFrame(
    [
     ("bird","Falconiformes",389.0),
     ("bird", "Psittaciformes", 24.0),
     ("mammal", "Carnivora", 80.2),
     ("mammal", "Primates", np.nan),
     ("mammal", "Carnivora", 58),
     ],
    index = ["Falcon","parrot","lion","monkey","leopard"],
    columns = ("class","order","max_speed"),
    )
print(df)
print("-"*30)
# default is axis=0

grouped = df.groupby("class")
print(grouped)

print("-"*40)
grouped = df.groupby("order", axis="columns")
print(grouped)

print("-"*40)
grouped = df.groupby(["class", "order"])
print(grouped)
#%%

df4 = pd.DataFrame(
    {
     "A":["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
     "B":["one", "one", "two", "three", "two", "two", "one", "three"],
     "C": np.random.randn(8),
     "D":np.random.randn(8),
     }
    )

grouped = df4.groupby("A")

print(grouped)

grouped = df4.groupby(["A","B"])


df4 = df4.set_index(["A", "B"])



grouped1= df4.groupby(level=df4.index.names.difference(["B"]))


print(grouped1.sum())

print("-"*40)

def get_letter_type(letter):
    if letter.lower() in "aeiou":
        return "vowe1"
    else:
        return "consonant"
grouped2 = df4.groupby(get_letter_type,axis=1)

print("-"*40)

print(df4.groupby(["A","B"]).sum())




#%%
lst = [1,2,3,1,2,3]

s = pd.Series([1,2,3,10,20,30],lst)

grouped =s.groupby(level=0)

print(grouped.first())


print()

print(grouped.last())
print()

print(grouped.sum())
print()

print()

df3 = pd.DataFrame({"X":["B","B","A","A"],"Y":[1,2,3,4]})

print(df3.groupby(["X"]).sum())

print("-"*30)

print(df3.groupby(["X"], sort=False).sum()) 


#%%

df4 = pd.DataFrame({"X":["A","B","A","B"],"Y":[1,4,3,2]})

print(df4.groupby(["X"]).get_group("A"))

#%%


print(df4.groupby(["X"]).get_group("B"))

#%%GroupBy dropna

df_list = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]


df_dropna = pd.DataFrame(df_list,columns=["a","b","c"])

print(df_dropna)
print()

print(df_dropna.groupby(by=["b"], dropna=True).sum())
#%%
























































