# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:09:37 2021

@author: ali_d
"""

#titanic 1

"""
The sinking of the world's largest ship in 1912
"""
#Load and Check Data
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import seaborn as sns
from collections import Counter

import warnings
warnings.filterwarnings("ignore")


train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
test_passengerId = test_df["PassengerId"]

print(train_df.columns)

# PassengerId = yolcuların numarası
# Survived = Hayatta kalan,0= öldü,1=hayatta kalmıs
# Name = isim
# Sex = cinsiyet
# Age = yas
# SibSp = Kardeşlerin / Eşlerin Sayısı
# Parch = Ebeveynlerin / çocuk sayısı
# Ticket = bilet numarası
# Fare = bilete ödediğ para mıktarı
# Cabin = kabin kaldıkları odalar
# Embarked = hangı limandan bındıgı(C = Cherbourg, Q = Queenstown, S = Southampton)
#Pclass = yolcuların sınıfları

print()

a = (train_df.head())

print(a)

print()

b=(train_df.describe())

print(train_df.info())
"""
float64(2): Fare ve Age
int64(5): Pclass, sibsp, parch, passengerId and survived
object(5): Cabin, embarked, ticket, name and sex
"""
















































































