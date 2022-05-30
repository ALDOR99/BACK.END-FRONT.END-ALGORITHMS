# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:33:58 2021

@author: ali_d
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from plotly.offline import init_notebook_mode,plot,iplot
import plotly as py
import plotly.graph_objs as go # plotly graphical object

import warnings            
warnings.filterwarnings("ignore") 


data = pd.read_csv("deprem.csv")

data = data.drop([3378,7512,20650])
data["year"]= [int(each.split("/")[2]) for each in data.iloc[:,0]]
#earthquakes

# 'Date' = Tarih
# 'Time' = Zaman
# 'Latitude' = Enlem
# 'Longitude' = Boylam 
# 'Type' = Tip
# 'Depth' = Derinlik
# 'Depth Error' = Derinlik hatası
# 'Depth Seismic Stations' = Derinlik sismik istasyonları
# 'Magnitude' = Büyüklük
# 'Magnitude Type' =  Büyüklük tipi
# 'Magnitude Error' = Büyüklük hatası
# 'Magnitude Seismic Stations' = Büyüklük sismik istasyonlar
# 'Azimuthal Gap' = Azimut boşluğu
# 'Horizontal Distance' = Yatay mesafe 
# 'Horizontal Error' = Yatay hata
# 'Root Mean Square' = Kök kare ortalama
# 'ID' = İD
# 'Source' = Kaynak
# 'Location Source' = Konum kaynağı
# 'Magnitude Source' = Büyüklük kaynağı
# 'Status' = Durum



print(data.head())

print(data.Type)
print("-"*30)

print(data.Type.unique())
# 'Earthquake' = Deprem
# 'Nuclear Explosion' = Nükleer patlama
# 'Explosion' = Patlama
# 'Rock Burst' = Kaya patlaması

dataset = data.loc[:,["Date","Latitude","Longitude","Type","Depth","Magnitude","year"]]
print(dataset.head())


#%%

years = [str(each) for each in list(data.year.unique())]
#
types = ['Earthquake', 'Nuclear Explosion', 'Explosion', 'Rock Burst']
#
custom_colors = {
    'Earthquake': 'rgb(189, 2, 21)',
    'Nuclear Explosion': 'rgb(52, 7, 250)',
    'Explosion': 'rgb(99, 110, 250)',
    'Rock Burst': 'rgb(0, 0, 0)'
}
#
# make figure

figure = {
    "data":[],
    "layout":{},
    "frames":[]
    }
figure['layout']['geo'] = dict(showframe=False, showland=True, showcoastlines=True, showcountries=True,
               countrywidth=1, 
              landcolor = 'rgb(217, 217, 217)',
              subunitwidth=1,
              showlakes = True,
              lakecolor = 'rgb(255, 255, 255)',
              countrycolor="rgb(5, 5, 5)")
figure['layout']['hovermode'] = 'closest'
figure['layout']['sliders'] = {
    'args': [
        'transition', {
            'duration': 400,
            'easing': 'cubic-in-out'
        }
    ],
    'initialValue': '1965',
    'plotlycommand': 'animate',
    'values': years,
    'visible': True
}
figure['layout']['updatemenus'] = [
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 500, 'redraw': False},
                         'fromcurrent': True, 'transition': {'duration': 300, 'easing': 'quadratic-in-out'}}],
                'label': 'Play',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }
]

sliders_dict = {
    'active': 0,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'Year:',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}
#
# make data

year = 1695
for ty in types:
    dataset_by_year = dataset[dataset['year'] == year]
    dataset_by_year_and_cont = dataset_by_year[dataset_by_year['Type'] == ty]
    
    data_dict = dict(
    type='scattergeo',
    lon = dataset['Longitude'],
    lat = dataset['Latitude'],
    hoverinfo = 'text',
    text = ty,
    mode = 'markers',
    marker=dict(
        sizemode = 'area',
        sizeref = 1,
        size= 10 ,
        line = dict(width=1,color = "white"),
        color = custom_colors[ty],
        opacity = 0.7),
)
    figure['data'].append(data_dict)
    
# make frames

for year in years:
    frame = {'data': [], 'name': str(year)}
    for ty in types:
        dataset_by_year = dataset[dataset['year'] == int(year)]
        dataset_by_year_and_cont = dataset_by_year[dataset_by_year['Type'] == ty]

        data_dict = dict(
                type='scattergeo',
                lon = dataset_by_year_and_cont['Longitude'],
                lat = dataset_by_year_and_cont['Latitude'],
                hoverinfo = 'text',
                text = ty,
                mode = 'markers',
                marker=dict(
                    sizemode = 'area',
                    sizeref = 1,
                    size= 10 ,
                    line = dict(width=1,color = "white"),
                    color = custom_colors[ty],
                    opacity = 0.7),
                name = ty
            )
        frame['data'].append(data_dict)

    figure['frames'].append(frame)
    slider_step = {'args': [
        [year],
        {'frame': {'duration': 300, 'redraw': False},
         'mode': 'immediate',
       'transition': {'duration': 300}}
     ],
     'label': year,
     'method': 'animate'}
    sliders_dict['steps'].append(slider_step)


figure["layout"]["autosize"]= True
figure["layout"]["title"] = "Earthquake"       

figure['layout']['sliders'] = [sliders_dict]

plot(figure)



































