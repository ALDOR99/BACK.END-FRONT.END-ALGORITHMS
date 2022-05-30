# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:00:14 2021

@author: ali_d
"""

#Bubble Plot

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

from wordcloud import WordCloud
import matplotlib.pyplot as plt



#2016 ya ait ilk 20 unıversitenin teaching skorunu universite rengine
#gore karsılastıracam ama aynı zamanda number of students benım 
#scatterımın size ı olacak international da rengi olacak

timesData = pd.read_csv("timesData.csv")

df2016 = timesData[timesData.year == 2016].iloc[:20,:]
#burda 2016 yılına ait 20 universiteyi alıyorum

international_color = [float(each) for each in df2016.international]

#benum num_students hem object(str) oldugu ıcın bunu float degere cevırıyorum
#hemde ondalıklı olarak yazılmadıgı ıcın araya vırgul koydugu ıcın bunu "."(nokta)
#ile degistiriyorum
#replace = degistirmek

international_color = df2016.international
#daha sonra international_color içine df2016.international verisini
#ekledim

#simdi plot etmeye hazırız

data = [
    {
        'y': df2016.teaching,
        'x': df2016.world_rank,
        'mode': 'markers',
        'marker': {
            'color': international_color,
            'size': num_students_size,
            'showscale': True
        },
        "text" :  df2016.university_name    
    }
]
iplot(data)














































