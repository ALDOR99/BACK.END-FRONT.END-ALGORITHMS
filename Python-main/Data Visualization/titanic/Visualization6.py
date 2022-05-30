# -*- coding: utf-8 -*-

"""
Created on Fri Jun 18 16:28:25 2021

@author: ali_d
"""

# Visualization

"""
# PassengerId = yolcuların numarası
# Survived = Hayatta kalan,1= öldü=0,
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



list1 = ["SibSp","Parch","Age","Fare","Survived"]
sns.heatmap(train_df[list1].corr(),annot = True,fmt=".2f")
plot.show()

# Fare feature seems to have correlation with survived feature (0.26).
# Fare özelliği, hayatta kalan özellik ile korelasyon var (0.26).

#%% SibSp -- Survived
#SibSp =  yolcunun kardes yada es sayısı

g = sns.factorplot(x = "SibSp", 
                   y = "Survived", 
                   data = train_df,
                   kind = "bar",
                   size = 6)

g.set_ylabels("Survived Probability")
plt.show()
#SibSp 0,1,2 ise Survived Probability olasılığı daha yuksek
# eğer 3 ,ise Survived Probability olasılığı azalıyor

#%% Parch -- Survived

g = sns.factorplot(x = "Parch",
                   y = "Survived",
                   kind = "bar",
                   data=train_df,
                   size = 6)
g.set_ylabels("Survived Probability")
plt.show()


# Sibsp and parch can be used for new feature extraction with th = 3
# small familes have more chance to survive.
# Küçük aileler hayatta kalmak için daha fazla şansı var.
there is a std in survival of passenger with parch = 3

#%% Pclass -- Survived

g = sns.factorplot(x = "Pclass",
                   y = "Survived",
                   data = train_df,
                   kind = "bar",
                   size=6)
g.set_ylabels("Survived Probability")
plt.show()
# burda Pclass'a gore hayatta kalma olasıgını ınceleyebılırız

#%% Age -- Survived

g = sns.FacetGrid(train_df,col="Survived")
g.map(sns.distplot,"Age",bins=25)

plt.show()

# age <= 10 has a high survival rate,
# oldest passengers (80) survived,
# large number of 20 years old did not survive,
# most passengers are in 15-35 age range,
# use age feature in training
# use age distribution for missing value of age


#%% Pclass -- Survived -- Age

g = sns.FacetGrid(train_df,col = "Survived",row ="Pclass",size=3)
g.map(plt.hist,"Age",bins = 25)
plt.show()

#%% Embarked -- Sex -- Pclass -- Survived

g = sns.FacetGrid(train_df,row = "Embarked",size=3)
g.map(sns.pointplot,"Pclass","Survived","Sex")
g.add_legend()
plt.show()

# Female passengers have much better survival rate than males.
# males have better survşval rate in pclass 3 in C.
# embarked and sex will be used in training.

#%% Embarked -- Sex -- Fare -- Survived

g = sns.FacetGrid(train_df,row="Embarked",col = "Survived",size=3)
g.map(sns.barplot,"Sex","Fare")
g.add_legend()
plt.show()

#%%  Fill Missing: Age Feature

a = (train_df[train_df["Age"].isnull()])


sns.factorplot(x = "Sex",y="Age",
               data=train_df,
               kind="box")
plt.show()
# Sex is not informative for age prediction, age distribution seems to be same.
#%%

sns.factorplot(x = "Sex",
               y="Age",
               hue="Pclass",
               data=train_df,
               kind="box")
plt.show()
# 1st class passengers are older than 2nd, and 2nd is older than 3rd class.
#%%

sns.factorplot(x="Parch",
               y="Age",
               data=train_df,
               kind="box")

sns.factorplot(x="SibSp",
               y="Age",
               data=train_df,
               kind="box")
plt.show()


#%%
train_df["Sex"] = [1 if i == "male" else 0 for i in train_df["Sex"]]

sns.heatmap(train_df[["Age",
                      "Sex",
                      "SibSp",
                      "Parch",
                      "Pclass"]].corr(),
            annot=True)

plt.show()

#%%


index_nan_age = list(train_df["Age"][train_df["Age"].isnull()].index)
for i in index_nan_age:
    age_pred = train_df["Age"][((train_df["SibSp"] == train_df.iloc[i]["SibSp"]) &(train_df["Parch"] == train_df.iloc[i]["Parch"])& (train_df["Pclass"] == train_df.iloc[i]["Pclass"]))].median()
    age_med = train_df["Age"].median()
    if not np.isnan(age_pred):
        train_df["Age"].iloc[i] = age_pred
    else:
        train_df["Age"].iloc[i] = age_med
        
print(train_df[train_df["Age"].isnull()])

#%%

        
        
        
























































