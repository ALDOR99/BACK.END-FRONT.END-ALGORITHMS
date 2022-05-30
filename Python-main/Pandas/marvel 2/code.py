# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:40:42 2021

@author: ali_d
"""


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv("charcters_stats.csv")

#name = isim
#alignment = hizalama
#ıntelligence = Zeka
#strength = kuvvet
#speed = hız
#durability =  dayanıklılık
#Power = güç
#combat = mücadele
#total = Toplam
#%%
a = df.head(10)
#ilk 5 verımı a degıskenıne atadım

print(a["Name"])
# Name columns

#
print()
print(a[["Name","Alignment"]])
#Name ve Alignment sütünları 
print()

#
print(a.iloc[1])
#1. indexteki veriler

print()

#
print(a.iloc[5])

print()

#
print(a.iloc[9])

print("-"*30)

#
print(a.iloc[9,1])
print(a.iloc[3,2])

print(a.iloc[5,5])
print("-"*30)


###Data Filtreleme

w = df["Power"]
# power sutunumda bulunanları verilerimi w degıskenıme aktardım

w1 = w[w>90]
# w degiskenıme aktardıgım power verileri
#powerı 90 buyuk olanları filtreledim

print(w1.head())
#ilk beşi
#şimdi 90 gucunden buyuk olan ilk veri indeks numarı 5i inceleyelim
print()

print(df.iloc[5])
# name = Abraxas

print(df.iloc[11])
#name = Air Walker
print()
print(df.iloc[12])
#name = Alan Scoot
print()
print(df.iloc[16])
#name = Amazo
print()
print(df.iloc[26])
#name = Anti-Monitor
print()


wx = df[df["Speed"]>80]
#burda datamın speed verısı 80den buyuk olanları fıltreledım
print(wx.head())
#burda ise filtrelediğim datamın ilk 5 verisini aldım

print()


wd = df["Combat"]>80
#combat verisi 80den buyuk olanları filtreledim
print(wd.head())
#il 5 verisini yazdırdım
print("-"*40)


ax1 = df[df["Power"]==100]
#burda power puanı 100e esıt olanları fıltreledim
print(ax1.head())


print("-"*40)

as1=df[(df['Power']> 90) & (df['Speed']> 90)]

#burda dataframem ıcınde power sevıyesı 90dan buyuk ve 
#speed sevıyesı 90dan buyuk olan verılerı filtreleyip
#as1 degıskenıme aktardım

print(as1.head())
print("-"*40)
print("-"*40)

as2=df[(df['Power']>70) & (df['Speed']>70) & (df["Durability"]>70)]        

#burda power,speed ve Durability verılerının den buyuk olanlarını filtreledim
print(as2.iloc[1])
print("-"*40)

print(as2.iloc[2])
print("-"*40)

print(as2.iloc[1])
print("-"*40)

print(as2.iloc[1])
print("-"*40)

ff =df[(df['Combat']>70) | (df['Strength']>70) | (df["Total"]>70)] 
print(ff.iloc[2])       
print(ff.iloc[3])
print(ff.iloc[5])
print(ff.iloc[7])
print(ff.iloc[6])
print("-"*30)


#yeni bir sütun ekleyelim

print(df.columns)

df["Power_Speed"] = (df["Power"] + df["Speed"])
#burda datamın ıcıne yenı bır sutun olusturdum ve datamın hız ve guclerının
#toplam degerlerini aktardım

print(df.columns)
#burda ekledıgım column gorunmekte
print("-"*40)
#
ag = df.sum()
#burda her sütunumun toplam değerlerını alıyorum

#ag1 = df.sum().sum()
#burda string deger oldugu ıcın hata donecektır
#bunu yapmamız ıcın verıden stıng degerıne sahıb sutunları drop
#etmemiz gereklı
#DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')


#df = df.drop(columns = "Name",axis=1,)

df12 = df.drop(columns=["Name","Alignment"],axis=1)
#burda Name ve Alignment sütunlarını droplayarak verıden cıkardım
#boylelıkle elımde sadece int degerlerınden olusan bır verı tablosu kaldı
#simdi tum tablonun toplam degerıne bakalım
print("-"*30)
L1 = df12.sum().sum()
print(L1)
#bu sekılde datamda toplam ne kadar verı varsa hepsının toplam degerını bulduk
print("-"*30)

print(df.size)
#kac adet verı

print("-"*30)

print(df.isnull())
print("-"*30)


print(df.isnull().sum())
print("-"*30)
#%%
PowerGroupBy = df.groupby("Power")
print(PowerGroupBy)

alis =(PowerGroupBy["Power"].sum())

print("-"*30)

print(alis.min())
#
print()
#
print(alis.max())
#%%


delta = (df.groupby("Speed").count())
print(delta.max())
print(delta.min())


#%%

br1 = df["Power"].head(10)
br2 = df["Name"].head(10)

print(br1)

print(br2)

birleştir = pd.concat([br2,br1],axis=1)
print(birleştir)

#%%
birleştir1 = pd.concat([br2,br1],axis=0)
print(birleştir1)

#%%
print(df['Power'].unique())

aaa = df[(df['Alignment'] == 'good') & (df['Power'] > 80)].head()
####
print()
(df['Alignment'] == 'good').head()
print("-"*40)
(df['Alignment'] == 'good').dtype # dtype('bool')
#%%

#df[df['Combat'].fillna(False)].head()
#

sfs = df[df['Alignment'].str.contains('good')]
























































































