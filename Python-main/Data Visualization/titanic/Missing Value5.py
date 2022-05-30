# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 14:34:17 2021

@author: ali_d
"""
#Missing Value


# -Find Missing Value
# -Fill Missing Value


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



train_df_len = len(train_df)
print(train_df_len)


train_df = pd.concat([train_df,test_df],axis = 0).reset_index(drop = True)

print(train_df.head())


# Find Missing Value
print(train_df.columns[train_df.isnull().any()])
print("-"*30)

print(train_df.isnull().sum())
print("-"*30)



# Fill Missing Value
b = (train_df[train_df["Embarked"].isnull()])

print()

train_df.boxplot(column="Fare",by = "Embarked")
plt.show()

print()

train_df["Embarked"] = train_df["Embarked"].fillna("C")
print("-"*30)

train_df[train_df["Fare"].isnull()]

d = train_df[train_df["Pclass"] == 3]["Fare"]
print(np.mean(d))

train_df["Fare"]=train_df["Fare"].fillna(np.mean(d))

print(train_df[train_df["Fare"].isnull()])




































































































