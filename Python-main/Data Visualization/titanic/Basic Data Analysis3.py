# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 23:18:31 2021

@author: ali_d
"""

# Basic Data Analysis

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
print()



# Plcass vs Survived
train_df[["Pclass","Survived"]].groupby(["Pclass"],
                                        as_index = False).mean().sort_values(by="Survived",
             
                                                                             ascending = False)
print()

# Sex vs Survived
print(train_df[["Sex","Survived"]].groupby(["Sex"],
                                     as_index =False).mean().sort_values(by="Survived",
                                                                          ascending = False))
print()

# Sibsp vs Survived
print(train_df[["SibSp","Survived"]].groupby(["SibSp"], as_index = False).mean().sort_values(by="Survived",ascending = False))


print()
# Parch vs Survived
print(train_df[["Parch","Survived"]].groupby(["Parch"], as_index = False).mean().sort_values(by="Survived",ascending = False))









































































