# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 23:22:51 2021

@author: ali_d
"""


#Hızlı Baslangıc 2 

import numpy as np
import pandas as pd


data = {
        "one":[1,2,3,4,5],
        "two":[6,7,8,9,10],
        "three":[11,12,13,14,15],
        "four":[16,17,18,19,20],
        "five":[21,22,23,24,25],
        }
Datax = pd.DataFrame(data=data)
print(Datax.head())

print("-"*30)


Datax1 = Datax.copy()

Datax1["six"] = ["one","one","two","three","four"]
print(Datax1)
print()

print(Datax1[Datax1["six"].isin(["two","four"])])
print()
print(Datax1[Datax1["six"].isin(["two","three"])])
print()

#%% Ayarlar


s1 = pd.Series([1,2,3,4,5,6,7],
               index=pd.date_range('20130102',
                                   periods=7))

print(s1)
print()

Datax["F"] = s1

#%%

#Datax.at[dates[0],"one"] = 0

 #konumuna gore
 
print(Datax.iat[0,2] == 0)
print(Datax.iat[0,3] == 5)

print(Datax.iat[0,5] == 2)
#%%


a = Datax.loc[:,"one"] = np.array([5] * len(Datax))

print(a)
#%%

Datax3 = Datax.copy()

#Datax3[Datax3 >6]=-Datax
print(Datax3)


#%%
print(Datax3[Datax3>2])

print(Datax3[Datax3 >4])

Datax3[Datax3 > 0] =-Datax3

print("-"*30)

#%% Kayıp Veri

data = {
        "a":[np.nan,1,2,3,4],
        "b":[np.nan,1,2,3,4],
        "c":[np.nan,np.nan,np.nan,np.nan,np.nan],
        "d":[np.nan,np.nan,np.nan,np.nan,np.nan]

        }


vr = pd.DataFrame(data=data)

print(vr)
print("-"*30)

vr1 = vr.copy()

print(vr1.dropna(axis=1))
print(vr1)

print(vr1["c"])
print(vr1.drop(columns="c",axis=1))
print()
print(vr1.drop(index=0,axis= 0))
print(vr1.drop(columns=["c","d"],axis=1))
print()


print(vr1.fillna(value=99))
#nan degerlere sahıp verılerı doldurdum

print(pd.isna(vr1))
#nan = true
#value = false

#%% Operasyonlar
#İstatistikler
data = {
        "a":[0,1,2,3,4],
        "b":[0,1,2,3,4],
        "c":[0,1,2,3,4],
        "d":[0,1,2,3,4]

        }

xs = pd.DataFrame(data=data)

print(xs.mean())

print()

print(xs.mean(1))
print()


print(xs)

print(xs.apply(np.cumsum))
print()

print(xs.apply(lambda x:x.max()-x.min()))
print()

#Histogram Çıkarma

d = pd.Series(np.random.randint(0,7,size=10))

print(d)

print(d.value_counts())
print()

#%% Dizi Metodları

s = pd.Series(["A","B","C","Aaba","Baca",np.nan,"CABA","dog","cat"])
print(s)
print("-"*30)
print(s.str.lower())
#%% Birleştirmek

#Concat


k = pd.DataFrame(np.random.randn(10,4))
print(k)

print("-"*30)

# break it into pieces
#paramparça etmek


pieces = [k[:3],k[3:7],k[7:]]

print(pd.concat(pieces))

#%% join

left = pd.DataFrame({
    "key":["foo","foo"],
    "lval":[1,2]})


right = pd.DataFrame({
    "key":["foo","foo"],
    "lval":[4,5]})

print(left)

print()

print(right)
print()

print(pd.merge(left, right,on="key"))

print("-"*30)

left = pd.DataFrame({
    "key":["foo","bar"],
    "lval":[1,2]})

right = pd.DataFrame({'key': ['foo', 'bar'],
                      'rval': [4, 5]})
print(left)
print()
print(right)
print("-"*30)
print(pd.merge(left, right,on="key"))
print()

#%% Append


















































