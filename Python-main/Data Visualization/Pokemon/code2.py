# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 21:48:18 2021

@author: ali_d
"""
#code2


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from subprocess import check_output


data = pd.read_csv("pokemon.csv")


#Line Plot



data.Speed.plot(kind="line",color="blue",label = "Speed",
                linewidth=1,alpha =0.5,grid=True,linestyle = "-")

data.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.9,grid = True,linestyle = ':')
plt.legend()
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Line Plot")
plt.show()


#%%

data1 = (data[data["Attack"]>100].head())
data2 = (data[data["Speed"]>90].head())


data1.Attack.plot(kind="line",color ="blue",label="attack",
                  linewidth=1,alpha=0.5,grid=True,linestyle="-")

data2.Speed.plot(kind="line",color="red",label="speed",
                 linewidth=1,alpha=0.6,grid=True,linestyle=":")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Line Plot")
plt.show()
#%%

data3 = (data[data["HP"]>100].head(20))
data4 = (data[data["Defense"]>100].head(20))


data3.HP.plot(kind = "line" , color="red" , label = "Can" ,linewidth=2,alpha=0.9,grid=True,linestyle="-" )
data4.Defense.plot(kind  ="line" , color ="blue" , label = "Defans",linewidth=2,alpha=0.9,grid=True,linestyle="-")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Line Plot")
plt.show()

#%%Scatter Plot

data.plot(kind="scatter",x="Attack",y="Defense",alpha=0.9,
          color="red")
plt.xlabel("Attack")
plt.ylabel("Defence")
plt.title("Attack Defense Scatter Plot")
plt.show()


#%%

data5 = (data[data["HP"]>100].head(20))
data6 = (data[data["Attack"]>100].head(20))
data7 =pd.concat([data5,data6],axis=0)

data7.plot(kind="scatter",x="HP",y="Defense",alpha=0.9,
           color="red")

plt.xlabel("HP")
plt.ylabel("Attack")
plt.title("HP Attack Scatter Plot")
plt.show()

#%%

data8 = (data[data["HP"]>100].head(20))
data9 = (data[data["Attack"]>100].head(20))
data10 = pd.concat([data8,data9],axis=0)

data10.plot(kind ="scatter",x="HP" , y="Defense",alpha=0.9,
           color="red",grid=True)
plt.legend()
plt.xlabel("HP")
plt.ylabel("Defense")
plt.title("Ortaya karışık Scatter Plot")
plt.show()

#%% Histogram
data.Speed.plot(kind="hist",bins=50,figsize=(12,12))
plt.show

#%%

data.Attack.plot(kind="hist",bins=150,figsize=(9,9),color="red")

plt.show()


#%%

data.Attack.plot(kind="hist" , bins =150 , figsize =(10,5) , color="red")

plt.show()

#%%

data.Defense.plot(kind="hist",bins=90,figsize =(10,5),color="blue",grid=True,
                  alpha=0.9)
plt.show()


#%%
data.boxplot(column = "Attack",by="Legendary")
plt.show()
#%%

data1 = data.loc[:,["Attack","Defense","Speed"]]
data1.plot()


#%%
data2 = data.loc[:,["Attack","HP","Defense"]]
data2.plot(grid=True)

#%% subplots

data1.plot(subplots =True,grid=True)
plt.show

#%%

data2.plot(subplots =True,grid=True)
plt.show



#%%

# importing all the necessary packages
import numpy as np
import matplotlib.pyplot as plt

# importing the style package
from matplotlib import style

# creating an array of data for plot
data = np.random.randn(50)

# using the style for the plot
plt.style.use('Solarize_Light2')

# creating a plot
plt.plot(data)

# show plot
plt.show()
#%%

data2.plot(subplots =True,grid=True)
plt.style.use('Solarize_Light2')
plt.show

#%%

data2.plot(subplots =True,grid=True)
plt.style.use('dark_background')
plt.show
#%%

data2.plot(subplots =True,grid=True)
plt.style.use('fivethirtyeight')
plt.show
#%%
data2.plot(subplots =True,grid=True)
plt.style.use('seaborn-darkgrid')
plt.show
#%%
data2.plot(subplots =True,grid=True)
plt.style.use('fast')
plt.show

#%%

data2.plot(subplots =True,grid=True)
plt.style.use('tableau-colorblind10')
plt.show









