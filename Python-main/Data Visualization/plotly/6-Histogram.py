# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:30:53 2021

@author: ali_d
"""

#Histogram
# 2011 ve 2012deki "students-staff ratio " verilerini incelıyoruz

import numpy as np 
import pandas as pd 


from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

from wordcloud import WordCloud
import matplotlib.pyplot as plt


timesData = pd.read_csv("timesData.csv")

x2011 = timesData.student_staff_ratio[timesData.year == 2011]
x2012  = timesData.student_staff_ratio[timesData.year == 2012]

#burda timesDatamın student_staff_ratio columnslarındakı verılerı
#2011 ve 2012 yıllarına gore filtreledim

trace1 = go.Histogram(
    x=x2011,
    opacity=0.75,
    name = "2011",
    marker=dict(color='rgba(171, 50, 96, 0.6)'))
# x eksenime 2011 yılındaki oranını yazıyorum
# opacity saydamlığım var
#name 2011
#marker benım hıstogramımın rengi
trace2 = go.Histogram(
    x=x2012,
    opacity=0.75,
    name = "2012",
    marker=dict(color='rgba(12, 50, 196, 0.6)'))
#aynı ıslemı 2012 ıcınde yapıyorum

data = [trace1,trace2]
#datamın ıcınde bırlestırıyorum

layout =go.Layout(barmode="overlay",
                  title = "students-staff ratio in 2011 and 2012",
                  xaxis =dict(title="students-staff ratio"),
                  yaxis=dict(title="Count"),)
#layout ile verilerimi birlestiriyorum
#overlay yanı iç içe gecirmek icin kullanıyorum
#ardından title adında bır baslı atıyorum
#x ve y eksenlerındekılerde titlelar

fig = go.Figure(data=data,layout=layout)
#daha sonra fig içinde birleştirip bir figure yaratıyorum
iplot(fig)
#ardından plot etırıyorum




############









































