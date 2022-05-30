# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:27:37 2021

@author: ali_d
"""

#school


import numpy as np
import pandas as pd

# plotly
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

from wordcloud import WordCloud

# matplotlib
import matplotlib.pyplot as plt


data = pd.read_csv("cwurData.csv")
#data1 = pd.read_csv("education_expenditure_supplementary_data.csv")
data2 = pd.read_csv("educational_attainment_supplementary_data.csv")
data3 = pd.read_csv("school_and_country_table.csv")
data4 = pd.read_csv("shanghaiData.csv")


data5 = pd.read_csv("timesData.csv")

# world_rank = Dünya sıralaması
# university_name = Üniversite adı
# country = ülke
# teaching = öğretme
# international = Uluslararası
# research = Araştırma
# citations = alıntılar
# income = Gelir
# total_score = toplam puan
# num_students = öğrenci sayısı
# student_staff_ratio = Öğrenci personeli oranı
# international_students =  Uluslararası öğrenciler
# female_male_ratio = kadın erkek oranı
# year = yıl

print(data5.head())
print(data5.info())
print()
#%% Line Charts

df = data5.iloc[:100,:]

trace1 = go.Scatter(
                    x = df.world_rank,
                    y = df.citations,
                    mode = "lines",
                    name = "citations",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text= df.university_name)


trace2 = go.Scatter(
                    x = df.world_rank,
                    y = df.teaching,
                    mode = "lines+markers",
                    name = "teaching",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'),
                    text= df.university_name)


data=[trace1,trace2]
layout = dict(title ="Citation and Teaching vs World Rank of Top 100 Universities",
              xaxis=dict(title="World Rank",ticklen=5,zeroline =False)
              )

fig = dict(data=data,layout=layout)
plot(fig)
#%%

df2 = data5.iloc[:100,:]

a = go.Scatter(
    x = df2.world_rank,
    y = df2.research,
    mode = "lines",
    name = "world_rank",
    marker = dict(color = 'rgba(3, 111, 20, 0.9)'),
    text= df.university_name)


b =go.Scatter(
    x = df2.world_rank,
    y = df2.teaching,
    mode = "lines+markers",
    name = "teaching",
    marker = dict(color = 'rgba(8, 12, 30, 0.8)'),
    text= df.university_name) 



data =[a,b]


layout = dict(title ="Teaching and World rank vs research  of Top 100 Universities",
              xaxis=dict(title="research ",ticklen=5,zeroline =False))

fig = dict(data =data ,layout = layout)

plot(fig)


#%%
df2014 = data5[data5.year == 2014].iloc[:100,:]
df2015 = data5[data5.year == 2015].iloc[:100,:]
df2016 = data5[data5.year == 2016].iloc[:100,:]

trace1 =go.Scatter(
                    x = df2014.world_rank,
                    y = df2014.citations,
                    mode = "markers",
                    name = "2014",
                    marker = dict(color = 'rgba(255, 128, 255, 0.8)'),
                    text= df2014.university_name)
trace2 =go.Scatter(
                    x = df2015.world_rank,
                    y = df2015.citations,
                    mode = "markers",
                    name = "2015",
                    marker = dict(color = 'rgba(255, 128, 2, 0.8)'),
                    text= df2015.university_name)
#  trace3
trace3 =go.Scatter(
                    x = df2016.world_rank,
                    y = df2016.citations,
                    mode = "markers",
                    name = "2016",
                    marker = dict(color = 'rgba(0, 255, 200, 0.8)'),
                    text= df2016.university_name)

data = [trace1,trace2,trace3]

layout = dict(title = 'Citation vs world rank of top 100 universities with 2014, 2015 and 2016 years',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Citation',ticklen= 5,zeroline= False)
             )

fig = dict(data = data, layout = layout)

plot(fig)


#%%

print(data5.columns)


df2014 = data5[data5.year == 2014].iloc[:100,:]
df2015 = data5[data5.year == 2015].iloc[:100,:]
df2016 = data5[data5.year == 2016].iloc[:100,:]

trace1 =go.Scatter(
                    x = df2014.world_rank,
                    y = df2014.num_students,
                    mode = "markers",
                    name = "2014",
                    marker = dict(color = 'rgba(255, 128, 255, 0.8)'),
                    text= df2014.university_name)

trace2 =go.Scatter(
                    x = df2015.world_rank,
                    y = df2015.num_students,
                    mode = "markers",
                    name = "2015",
                    marker = dict(color = 'rgba(255, 128, 2, 0.8)'),
                    text= df2015.university_name)

#  trace3
trace3 =go.Scatter(
                    x = df2016.world_rank,
                    y = df2016.num_students,
                    mode = "markers",
                    name = "2016",
                    marker = dict(color = 'rgba(0, 255, 200, 0.8)'),
                    text= df2016.university_name)


data = [trace1,trace2,trace3]

layout = dict(title = 'num_students vs world rank of top 100 universities with 2014, 2015 and 2016 years',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Citation',ticklen= 5,zeroline= False)
             )

fig = dict(data = data, layout = layout)

plot(fig)








































































