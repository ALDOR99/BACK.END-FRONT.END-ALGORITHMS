# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:37:51 2021

@author: ali_d
"""
#Scatter Plot

"""
2014,2015 ve 2016daki universitelerin alıntılarını karşılaştıracaz
"""


import numpy as np 
import pandas as pd 
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
from wordcloud import WordCloud
# matplotlib
import matplotlib.pyplot as plt


timesData = pd.read_csv("timesData.csv")


timesData.info()

#veri çerçeveleri hazırlamak

df2014 = timesData[timesData.year ==2014].iloc[:100,:]
#timesDatamı al ,timesDatamın yearsını 2014 esıtle ve bunun ılk 100 verısını al yanı
#ilk 100 universitesini

df2015 = timesData[timesData.year==2015].iloc[:100,:]
#2015deki ilk 100 unıversıteyı alıyorum

df2016 = timesData[timesData.year==2016].iloc[:100,:]
#2016tıdaki ilk 100 unıversıteyı alıyorum


import plotly.graph_objs as go
#burda plotly kutuphanemı import ediyorum

trace1 =  go.Scatter(
    
    x = df2014.world_rank,
    #x ekseni universitelerin sıralaması
    y = df2014.citations,
    #y eksenine 2014 yılına ait alıntıları
    mode = "markers",
    # modum markers
    name = "2014",
    #ismi 2014
    marker = dict(color = "rgb(255,128,255,0.8)"),
    text = df2014.university_name)
    #rengımı ayarlıyorum rgb(255,128,255,0.8) red,green,blue ve saydamlıgımı ayarlıyorum
    #yanı bana bu 3 rengın karısımını  verır 
    #text 2014 yılına ait unıversitelerin isimleri
#burda scatterımın ilkini yaratım


trace2 =  go.Scatter(
    
    x = df2015.world_rank,
    y = df2015.citations,
    mode = "markers",
    name = "2015",
    marker = dict(color = "rgb(255,128,2,0.8)"),
    text = df2015.university_name) 
    #burda sadece renkleri farklı

trace3 =  go.Scatter(
    
    x = df2016.world_rank,
    y = df2016.citations,
    mode = "markers",
    name = "2016",
    marker = dict(color = "rgb(0,255,200,0.8)"),
    text = df2016.university_name)
    #

data = [trace1,trace2,trace3]
#yaratıgım 3 tane scetterımı datada bırlestırıyorum

layout = dict(title = "Citiation vs world rank of top 100 universities with 2014,2015,and 2016 years",
              xaxis =dict(title="World Rank",ticklen=5,zeroline=False),
              yaxis = dict(title = "Citation",ticklen=5,zeroline=False)
              )
#daha sonra layoutunu yaratıyorum
#x eksenim World Rank
#y eksenim Citation
#ticklen kalınlığım
fig = dict(data=data,layout=layout)
#daha sonra fıgüre olusturabilmem ıcın data ve layout dic içinde birleştirmem gerek

iplot(fig)
#daha sonrada figürümü plot etiriyorum




























































































