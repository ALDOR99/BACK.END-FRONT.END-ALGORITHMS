# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:23:02 2021

@author: ali_d
"""


#Univariate Variable Analysis

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
print("-"*30)

#--Categorical Variable


def bar_plot(variable):
    
    """     
     input: variable ex: "Sex"
     output: bar plot & value count
    """
    # özelliği almak
    var = train_df[variable]
    
    # Kategorik Değişken Sayısı (Değer / Örnek)
    varValue = var.value_counts()
    #cinsiyetimizden kaç tane olması gerektiğini sağlıyor
    
    # görselleştirmek
    plt.figure(figsize=(9,3))
    plt.bar(varValue.index, varValue)
    plt.xticks(varValue.index, varValue.index.values)
    plt.ylabel("Frequency")
    plt.title(variable)
    plt.show()
    print("{}: \n {}".format(variable,varValue))
    
    
category1 = ["Survived","Sex","Pclass","Embarked","SibSp", "Parch"]
for c in category1:
    bar_plot(c)
    
    
    
#%%
def bar_plot(variable):
    var = train_df[variable]
    
    # Kategorik Değişken Sayısı (Değer / Örnek)
    varValue = var.value_counts()
    print("{}: \n {}".format(variable,varValue))

category1 = ["Survived","Sex","Pclass","Embarked","SibSp", "Parch"]
for c in category1:
    bar_plot(c)
    
    
    
    
    
#%%

def bar_plot(variable):
    
    """     
     input: variable ex: "Sex"
     output: bar plot & value count
    """
    # özelliği almak
    var = train_df[variable]
    
    # Kategorik Değişken Sayısı (Değer / Örnek)
    varValue = var.value_counts()
    #cinsiyetimizden kaç tane olması gerektiğini sağlıyor
    
    # görselleştirmek
    plt.figure(figsize=(9,3))
    plt.bar(varValue.index, varValue)
    plt.xticks(varValue.index, varValue.index.values)
    plt.ylabel("Frequency")
    plt.title(variable)
    plt.show()
    print("{}: \n {}".format(variable,varValue))
    
category2 = ["Cabin", "Name", "Ticket"]
for c in category2:
    print("{} \n".format(train_df[c].value_counts()))
    
    
    
#%% Numerical Variable


def plot_hist(variable):
    plt.figure(figsize = (9,3))
    plt.hist(train_df[variable], bins = 50)
    plt.xlabel(variable)
    plt.ylabel("Frequency")
    plt.title("{} distribution with hist".format(variable))
    plt.show()
numericVar = ["Fare", "Age","PassengerId"]

for n in numericVar:
    plot_hist(n)
    

































