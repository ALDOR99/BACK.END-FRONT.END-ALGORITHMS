# -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:04:26 2021
@author: ali_d
"""
## -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:04:26 2021
@author: ali_d
"""
import numpy as np 
import pandas as pd

from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Bar Charts

#2014 yılındaki ilk 3 universitenin citations ve teachingini
#karsılastıracaz

timesData = pd.read_csv("timesData.csv")

# prepare data frames
df2014 = timesData[timesData.year == 2014].iloc[:3,:]
# import graph objects as "go"
import plotly.graph_objs as go

# create trace1 
trace1 = go.Bar(
                x = df2014.university_name,
                #x 2014 yılında ilk3 universitenin ismi
                y = df2014.citations,
                #y eksenımızde 2014 yılında ilk 3 unıversıtenın 
                #alıntılarının puanları skorları
                
                name = "citations",
                #isim
                
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                             line=dict(color='rgb(0,0,0)',width=1.5)),
                #bar plotumuzun rengi ile cervesinin kalınlığı
                text = df2014.country)
                #texte grafın uzerıne geldıgımızde uzerınde deki unıversıtenın
                #hangı ulkeye ait oldugunu yazacak

# create trace2 
trace2 = go.Bar(
                x = df2014.university_name,
                y = df2014.teaching,
                name = "teaching",
                marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = df2014.country)

data = [trace1,trace2]
#daha sonra ben bunu data adında bır listenın ıcıne koyuyorum
layout = go.Layout(barmode = "group")
#burda barmode barlarımı yan yana koy yanı grup yap
fig = go.Figure(data=data,layout=layout)
#daha sonra figurumu olusturuyorum
iplot(fig)
#olusturdugum figuru plot etırdım

#%%
# prepare data frames
df2014 = timesData[timesData.year == 2014].iloc[:3,:]
# import graph objects as "go"
import plotly.graph_objs as go

x = df2014.university_name
#x ilk 3 unıversıtemın ısmı 

trace1 = {
  'x': x,
  #x benım x exenim
  
  'y': df2014.citations,
  #y de benım y eksenım
  'name': 'citation',
  #buda ısmım
  'type': 'bar'
  #type tipimde bar 
};
#burda bir trace1 dicti yaratıyorum

trace2 = {
  'x': x,
  'y': df2014.teaching,
  'name': 'teaching',
  'type': 'bar'
};
#trace2 de yukardakıyle aynı

#trace 2 dictimi yaratım
data = [trace1, trace2];
#ardından data listesi icinde trace 1 ve trace 2ımı birleştiriyorum

layout = {
  'xaxis': {'title': 'Top 3 universities'},
  'barmode': 'relative',
  'title': 'citations and teaching of top 3 universities in 2014'
};
#xaxis x eksenime bir label isim vardım
#relative ise barlarımı altlı ustlu  sekilde yap
#title ise baslıgım

fig = go.Figure(data = data, layout = layout)
#ardından figurumuzu olusturdum
iplot(fig)
#ardından figurumu plot etırıyorum





































