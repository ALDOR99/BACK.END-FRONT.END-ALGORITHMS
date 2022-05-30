# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:57:39 2021

@author: ali_d
"""

#kütüphanaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv("eksikveriler1.csv")
print(veriler)

boy = veriler[["boy"]]

print()

boykilo = veriler[["boy","kilo"]]
print(boykilo)
print()

x = 10

class insan():
    boy=10
    def kosmak(self,b):
        return b + 10
    
ali = insan()
print(ali.boy)
print(ali.kosmak(90))


#
#
print("-"*40)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values= np.nan ,strategy="mean")

Yas = veriler.iloc[:,1:4].values
print(Yas)
print()
imputer = imputer.fit(Yas[:,1:4])
print(imputer)
print("-"*40)

Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)




































