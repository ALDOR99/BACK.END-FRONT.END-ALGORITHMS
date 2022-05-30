import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.image as mpimg

#World population graph
#Dünya nüfüsü grafiği



years = [1,100,1000,1500,1700,1900,2000,2021]

popilation = [100000,250000,60000000,350000000,800000000,2000000000,3000000000,9000000000]

plt.plot(years,popilation)
plt.show()


#%% 
#Adding labels and custom line color
#Etiket ekleme ve özel çizgi rengi

years = [1950,1955,1960,1965,1970,1980,1985,1990,2000,2010,2020]


pop = [2.5,2.7,3.0,3.3,3.6,4.0,4.4,4.8,5.3,5.4,6.7]


plt.plot(years,pop,color=(255/255,100/255,100/255))
plt.ylabel("Population in bilions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")

plt.show()

#%% Legends, Titles, and Labels
#Efsaneler, Başlıklar ve Etiketler


x = [2,5,2]
y = [5,7,4]

x2 = [1,2,3]
y2 = [7,8,9]



plt.plot(x,y,label="first line")
plt.plot(x2,y2,label = "second line")

plt.xlabel("X Plot Number")
plt.ylabel("Y plot Number")

plt.title("graphics control")

plt.legend()

plt.show()

#%% Multiple lines and line styling
# Birden fazla satır ve çizgi stili

years=[1950,1955,1960,1965,1970,1980,1985,1990,1995,2000,2005,2010,2015]

pops=[2.5,2.7,3.0,3.3,3.6,4.0,4.4,4.8,5.3,5.7,6.1,6.5,7.3]

death=[1.2,1.1,1.2,2.1,2.0,2.3,1.8,1.9,2.6,1.6,2.4,2.4,4.0]

plt.plot(years,pops,'--',color=(255/255,100/255,100/255))
plt.plot(years,death,color=(.6,.6,1))
plt.ylabel("Population in Billions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")

plt.show

#%% Configuring the graph
#Grafiği yapılandırma


hero  = ["yone","yasuo","kayn","zed"]

kill = [950,970,940,980]

death = [120,124,130,140]

lines = plt.plot(hero,kill,hero,death)

plt.grid(True)
plt.setp(lines,color=(1,.4,.5),marker="*")

plt.show()


#%%Let's make pie (charts)
#Turta yapalım (grafikler)

labels = ["Zed","Yasuo","Yone","Kayn","Garen","Lux"]

kill = [33,52,12,17,42,48]

separated = (.1,0,0,0,0,0)

plt.pie(kill,labels=labels,autopct="%1.1f%%",explode=separated)

#plt.axis("equal")

plt.show()

#%%Letting Pandas make data simpler


data = {
        "names":["Zed","Yone","Garen","Lux"],
        "power":[130,133,120,125],
        "durability":[70,75,90,40],
        "magic" : [25,23,12,75],
        }

df = pd.DataFrame(data,columns=["names","power","durability","magic"])




#%%


data = {
        "names":["Zed","Yone","Garen","Lux"],
        "power":[130,133,120,125],
        "durability":[70,75,90,40],
        "magic" : [25,23,12,75],
        }

df = pd.DataFrame(data,columns=["names","power","durability","magic"])
df["total_power"] =df["power"] + df["durability"] + df["magic"]

print(df)

#%%
#Using Panda's data for pie charts
#pandamızın verilerini kullanma


color=["red","green","yellow","blue"]

plt.pie(df["total_power"],labels=df["names"],colors=color,autopct='%1.1f%%',shadow=(True),explode=(0.05,0.05,0.05,0.05))

plt.axis("equal")

plt.show()

#%%Bar charts


yone_scores = (234,120,90)
zed_scores = (235,125,99)
lux_scores = (200,80,75)

index = np.arange(3)
bar_width =.2

y1=plt.bar(index,yone_scores,bar_width,alpha=.9,label="yone")
z1=plt.bar(index+bar_width,zed_scores,bar_width,alpha=.9,label="zed")
l1=plt.bar(index+bar_width*2,lux_scores,bar_width,alpha=.9,label="lux")

plt.xticks(index/0.9,("Power","speed","durability"))
plt.ylabel("LoL grade average")
plt.xlabel("LSubjects")
plt.title("League of Legends")
plt.grid(True)
plt.legend()
plt.show()




#%%

hero_ages = [22,22,55,62,45,21,22,34,22,42,42,4,99,102,110,120,121,122,130,111,22,115,112,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(hero_ages,bins,histtype="bar",rwidth=(0.8))

plt.xlabel("Yaşlar")
plt.ylabel("çoğunluk")
plt.title("LoL yaş çoğunluğu")
plt.show()


#%%




























