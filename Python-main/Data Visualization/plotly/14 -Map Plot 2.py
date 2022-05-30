# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:54:15 2021

@author: ali_d
"""

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

import warnings
warnings.filterwarnings("ignore")



#Dünyada olan depremleri görseleştirecez

data = pd.read_csv("database.csv")
#datamı import etim read_csv

print(data.head())

data = data.drop([3378,7512,20650])
#datamın belirli kısımlarını dropladım bozuk oldukları ıcın ( nan)


data["year"]=[int(each.split("/")[2]) for each in data.iloc[:,0]]
#buda datamın ıcınde dolas ve "/" gore splıt et ve 2.indeksini al
#ve bunu int cevır dıyorum
#ardından datamda year adında bır columns olusturdum ve oraya aktardım
#artık int degerlerıne sahıp yıllarım var



data.Type.unique()

dataset = data.loc[:,["Date","Latitude","Longitude","Type","Depth","Magnitude","year"]]
#datamı data sete esıtlıyorum

years = [str(each) for each in list(data.year.unique())]

#yılımı unique yıllarıma esıtlıyorum ve years ıcınde depoluyorum


types = ['Earthquake', 'Nuclear Explosion', 'Explosion', 'Rock Burst']

#daha sonra types larımı depoluyorum toplam 4tane


custom_colors = {
    'Earthquake': 'rgb(189, 2, 21)',
    'Nuclear Explosion': 'rgb(52, 7, 250)',
    'Explosion': 'rgb(99, 110, 250)',
    'Rock Burst': 'rgb(0, 0, 0)'
    }
#herı bır felaketı rgb seklınde renklendıyıryorum

# make figure

figure = {
    
    'data': [],
    #datam geo harıtam olacak
    'layout': {},
    #layout baslıklarımın bulundugu kısım olacak
    'frames': []
    #frames de ekliyecegım butonlar olacak
    }
 #figuremin layoutu geo vs layoutumun ozelıklerı
figure['layout']['geo'] = dict(showframe=False, showland=True, showcoastlines=True, showcountries=True,
                         
              countrywidth=1, 
              landcolor = 'rgb(217, 217, 217)',
              subunitwidth=1,
              showlakes = True,
              lakecolor = 'rgb(255, 255, 255)',
              countrycolor="rgb(5, 5, 5)")

figure['layout']['hovermode'] = 'closest'
figure['layout']['sliders'] = {
    #slider = kaydırıcı
    'args': [
        'transition', {
            'duration': 400,
            #suresını belırlıyorum otomatık gecıs suresı
            'easing': 'cubic-in-out'
        }
    ],
    'initialValue': '1965',
    #baslangıc yıllı
    'plotlycommand': 'animate',
    #animate anımasyon var
    'values': years,
    #degerlerı var
    'visible': True
}
figure['layout']['updatemenus'] = [
  #butonlarımı eklıyorum
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 500, 'redraw': False},
                         'fromcurrent': True, 'transition': {'duration': 300, 'easing': 'quadratic-in-out'}}],
                
                'label': 'Play',
                #butonumun ismi
                
                'method': 'animate'
                #bastıgım zaman etkılesıme gırecek
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
            #burasıda pause buttonu
        ],
        'direction': 'left',
        #plotumun sol kısmında olacak
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

# make data
#datamı hazırlıyorum
year = 1695
for ty in types:
    dataset_by_year = dataset[dataset['year'] == year]
    #datamı yıllara gore fıltrelıycem
    dataset_by_year_and_cont = dataset_by_year[dataset_by_year['Type'] == ty]
    #bu datamıda typlere gore fıltrelıycem
    data_dict = dict(
    type='scattergeo',
    #daha sonra scatter seklınde gorselestirecem ama dunya harıtası uzerıdne gorselestırecem
    lon = dataset['Longitude'],
    #boylam 
    lat = dataset['Latitude'],
    #enlem
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

iplot(figure)




















