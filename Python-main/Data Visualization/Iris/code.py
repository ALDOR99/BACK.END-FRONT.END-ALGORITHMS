# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:11:39 2021

@author: ali_d
"""

#Iris

import numpy as np
import pandas as pd



data = pd.read_csv("Iris.csv")

print(data.head())
print(data.info())

print()

print(data["Species"].head())

print()


a = data["Species"] 
print()

b = data["Species"]
print()

c = data["Species"].nunique()
print(c)

print(data.columns)

print(data["PetalLengthCm"].value_counts())

print(data["Species"].value_counts())

print("-"*40)

print(data["SepalWidthCm"].value_counts())
print()
print()
print(data.index)

print()

a1 = (data.sort_values('Species', na_position = 'last'))
a2 = (data.sort_values('Species', na_position = 'first'))
print()

print(data.corr())

print()

print(data.index)

#print(data.loc["Id"])

print(data.iloc[1])
print()
print(data.iloc[5])

print()

print(data.iloc[8])
print("-"*30)

      


b = (data["SepalLengthCm"].head())
n = (data["SepalWidthCm"].head())

br = (pd.concat([b,n],axis=1))
print(br)

print()


print(data["SepalLengthCm"].sum())
print(data["SepalWidthCm"].sum())
print(data["PetalLengthCm"].sum())

print()

SepalLengthCmGroupBy = data.groupby("SepalLengthCm")

ı=(SepalLengthCmGroupBy.sum())
p = (SepalLengthCmGroupBy.min())


i = (data.describe())


print(data.describe())



j = (data["SepalLengthCm"]>5)

ty = (data[data["SepalLengthCm"]>5])




































