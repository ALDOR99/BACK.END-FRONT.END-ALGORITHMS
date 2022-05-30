# -*- coding: utf-8 -*-
"""
Created on Mon May 31 10:39:31 2021

@author: ali_d
"""

#Map Plot

import numpy as np
# linear algebra
#lineer Cebir

import pandas as pd
#data processing
#veri işleme

import seaborn as sns
# visualization library
# Görselleştirme Kütüphanesi

import matplotlib.pyplot as plt
# visualization library
# Görselleştirme Kütüphanesi
import chart_studio.plotly as py# visualization library

from plotly.offline import init_notebook_mode, iplot
# plotly offline mode
# plotly çevrimdışı mod

init_notebook_mode(connected=True) 

import plotly.graph_objs as go 
# plotly graphical object
# plotly grafiksel nesne


#Lodad the Data
#Verileri yükle


#bombing data
#bombalama verileri


aerial = pd.read_csv("operations.csv")
# first weather data that includes locations like country, latitude and longitude.
# Ülke, enlem ve boylam gibi yerleri içeren ilk hava durumu verileri.

weather_station_location = pd.read_csv("Weather Station Locations.csv")

weather = pd.read_csv("Summary of Weather.csv")
# Second weather data that includes measured min, max and mean temperatures
# Ölçülen min, maksimum ve ortalama sıcaklıkları içeren ikinci hava durumu verileri




#Data Cleaning 

#drop countries that are NaN
#nan olan ülkeleri bırak

aerial = aerial[pd.isna(aerial.Country)==False]

# drop if target longitude is NaN
# hedef boylamı nan ıse alma

aerial = aerial[pd.isna(aerial['Target Longitude'])==False]

# Drop if takeoff longitude is NaN
# Kalkış boylamı nan ise alma

aerial = aerial[pd.isna(aerial['Takeoff Longitude'])==False]

# drop unused features
# kullanılmayan özellikleri bırak
drop_list = ['Mission ID','Unit ID','Target ID','Altitude (Hundreds of Feet)','Airborne Aircraft',
             'Attacking Aircraft', 'Bombing Aircraft', 'Aircraft Returned',
             'Aircraft Failed', 'Aircraft Damaged', 'Aircraft Lost',
             'High Explosives', 'High Explosives Type','Mission Type',
             'High Explosives Weight (Pounds)', 'High Explosives Weight (Tons)',
             'Incendiary Devices', 'Incendiary Devices Type',
             'Incendiary Devices Weight (Pounds)',
             'Incendiary Devices Weight (Tons)', 'Fragmentation Devices',
             'Fragmentation Devices Type', 'Fragmentation Devices Weight (Pounds)',
             'Fragmentation Devices Weight (Tons)', 'Total Weight (Pounds)',
             'Total Weight (Tons)', 'Time Over Target', 'Bomb Damage Assessment','Source ID']

aerial.drop(drop_list, axis=1,inplace = True)

aearial = aerial[aerial.iloc[:,8]!="4248"]
# drop this takeoff latitude
# bu kalkış enlemini bırak

aerial = aerial[aerial.iloc[:,9]!=1355]
# drop this takeoff longitude
# bu kalkış boylamını bırak


print(aerial.info())

# what we will use only
weather_station_location = weather_station_location.loc[:,["WBAN","NAME","STATE/COUNTRY ID","Latitude","Longitude"] ]
weather_station_location.info()


# what we will use only
weather = weather.loc[:,["STA","Date","MeanTemp"]]
weather.info()


#Data Visualization(Veri goruntuleme)

# Lets start with basics of visualization that is understanding data.
# How many country which attacks
# Top target countries
# Top 10 aircraft series
# Takeoff base locations (Attacjk countries)
# Bombing paths
# Theater of Operations
# Weather station locations

#

# Verileri anlayan görselleştirme temelleri ile başlayalım.
# Kaç tane ülke saldırdı
# En İyi Hedef Ülkeler
# En İyi 10 Uçak Serisi
# Kalkış taban yerleri (attik ülkeler)
# Bombalama yolları
# Operasyon Tiyatrosu
# Hava Durumu İstasyonu Yerleri

#country(ülke)

print(aerial['Country'].value_counts())
plt.figure(figsize=(22,10))
sns.countplot(aerial['Country'])
plt.show()

print("-"*40)

#Top target countries
#Top Hedef Ülkeler

print(aerial['Target Country'].value_counts()[:10])
plt.figure(figsize=(22,10))
sns.countplot(aerial["Target Country"])
plt.xticks(rotation=90)
plt.show()


# Aircraft Series
# Uçak serisi

data = aerial['Aircraft Series'].value_counts()
print(data[:10])
data = [go.Bar(
            x=data[:10].index,
            y=data[:10].values,
            hoverinfo = 'text',
            marker = dict(color = 'rgba(177, 14, 22, 0.5)',
                             line=dict(color='rgb(0,0,0)',width=1.5)),
    )]

layout = dict(
    title = 'Aircraft Series',
)
fig = go.Figure(data=data, layout=layout)
iplot(fig)



aerial.head()


# ATTACK(Saldırı)

aerial["color"] = ""
aerial.color[aerial.Country == "USA"] = "rgb(0,116,217)"
aerial.color[aerial.Country == "GREAT BRITAIN"] = "rgb(255,65,54)"
aerial.color[aerial.Country == "NEW ZEALAND"] = "rgb(133,20,75)"
aerial.color[aerial.Country == "SOUTH AFRICA"] = "rgb(255,133,27)"
#burda her bır ulkemın renk degerı var
data = [dict(
    type='scattergeo',
    lon = aerial['Takeoff Longitude'],
    #saldırı yapan uçağımızın kalkıtığı boylanm
    lat = aerial['Takeoff Latitude'],
    #buda saldırı yapan ucagımızın kaltıgı enlem
    #bu ıkısı bana saldırı yapan ucagımın kaltıgı yerı verıyor
    hoverinfo = 'text',
    #mapımıızın ustundekı noktalara geldıgımızde cıkan yazılar
    text = "Country: " + aerial.Country + " Takeoff Location: "+aerial["Takeoff Location"]+" Takeoff Base: " + aerial['Takeoff Base'],
    #textımın ıcınde de bunlar yazsın dıyorum
    #saldırı yapan ulke, saldırı yapan ulekenın ucagının kaltıgı Location daha sonrada saldı yapan ucagın kalktıgı hava alanı
    mode = 'markers',
    #yani point koyuyorum
    
    marker=dict(
        sizemode = 'area',
        #bu nokta yerıne topcuk olsun
        sizeref = 1,
        size= 10 ,
        #topcuklarımın buyuklugu
        line = dict(width=1,color = "white"),
        #bu size etrafındakı lıne onun rengıde beyaz olsun dıyorum
        color = aerial["color"],
        
        opacity = 0.7),
        #saydamlığım
)]

layout = dict(
    title = 'Countries Take Off Bases ',
    #baslıgımı yazıyorum
    hovermode='closest',
    geo = dict(showframe=False, showland=True, showcoastlines=True, showcountries=True,
              countrywidth=1, projection=dict(type='miller'),
              landcolor = 'rgb(217, 217, 217)',
              subunitwidth=1,
              showlakes = True,
              lakecolor = 'rgb(255, 255, 255)',
              countrycolor="rgb(5, 5, 5)")
    #geo ozelıklerım
)
fig = go.Figure(data=data, layout=layout)
#figurumu olusturuyorum
iplot(fig)
#iplot etırıyorum








# Bombing paths(# Bombalama yolları)
#trace1 
#hangı ucak nerden nereye saldırmıs

airports = [ dict(
        type = 'scattergeo',
        lon = aerial['Takeoff Longitude'],
        lat = aerial['Takeoff Latitude'],
        hoverinfo = 'text',
        text = "Country: " + aerial.Country + " Takeoff Location: "+aerial["Takeoff Location"]+" Takeoff Base: " + aerial['Takeoff Base'],
        mode = 'markers',
        marker = dict( 
            size=5, 
            color = aerial["color"],
            line = dict(
                width=1,
                color = "white"
            )
        ))]
#2.dünya savasında ucakların bomba atmak ıcın kalktığı hava alanları

# trace2
#burda ıse bu ucaklar nereye ucmus
targets = [ dict(
        type = 'scattergeo',
        lon = aerial['Target Longitude'],
        #hedef boylamı
        lat = aerial['Target Latitude'],
        #hedef enlemi
        #yani bombamın atığı,vurdugu boylam ve enlemim
        hoverinfo = 'text',
        text = "Target Country: "+aerial["Target Country"]+" Target City: "+aerial["Target City"],
        #atak yaptıgım ulke, o ulkenın hangı sehrını vurmusum
        mode = 'markers',
       #point
        marker = dict( 
            size=1, 
            color = "red",
            #saldırı yapılan ulkeler kırmızı
            line = dict(
                width=0.5,
                color = "red"
            )
        ))]
        #markerımın ozelıkleri
        
# trace3
flight_paths = []
#bos bır lıste atıyorum
for i in range( len( aerial['Target Longitude'] ) ):
    #Target Longitude kadar uzunluk alıyorum ve buna range dıyorum
    #ne kadarsa uzunlugum o uzunlukta bır dongu dondurecem
    flight_paths.append(
        dict(
            type = 'scattergeo',
            lon = [ aerial.iloc[i,9], aerial.iloc[i,16] ],
            #burda kalkıs yaptıgım ve saldıgı yaptıgım boylam degerlerı
            lat = [ aerial.iloc[i,8], aerial.iloc[i,15] ],
            #ucagımı kaldırdıgım enlem ve atak yaptıgım enlem
            mode = 'lines',
            #line
            line = dict(
                width = 0.7,
                color = 'black',
            ),
            opacity = 0.6,
        )
    )
    
    
layout = dict(
    title = 'Bombing Paths from Attacker Country to Target ',
    #baslıgım
    hovermode='closest',
    geo = dict(showframe=False, showland=True, showcoastlines=True, showcountries=True,
               countrywidth=1, projection=dict(type='hammer'),
              landcolor = 'rgb(217, 217, 217)',
              subunitwidth=1,
              showlakes = True,
              lakecolor = 'rgb(255, 255, 255)',
              countrycolor="rgb(5, 5, 5)")
)
    
fig = dict( data=flight_paths + airports+targets, layout=layout )
#figirumu olusturuyorum
iplot( fig )
#iplot etırıyorum























































