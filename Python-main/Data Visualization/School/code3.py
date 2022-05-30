# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:18:23 2021

@author: ali_d
"""

#code3

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
from plotly import tools


data = pd.read_csv("cwurData.csv")
#data1 = pd.read_csv("education_expenditure_supplementary_data.csv")
data2 = pd.read_csv("educational_attainment_supplementary_data.csv")
data3 = pd.read_csv("school_and_country_table.csv")
data4 = pd.read_csv("shanghaiData.csv")


data5 = pd.read_csv("timesData.csv")

# Bar Charts

df2014 = data5[data5.year == 2014].iloc[:100,:]
df2015 = data5[data5.year == 2015].iloc[:100,:]
df2016 = data5[data5.year == 2016].iloc[:100,:]


#%% Bubble Charts

df2016.info()


df2016 = data5[data5.year == 2016].iloc[:20,:]

num_students_size = [float(each.replace(",",".")) for each in df2016.num_students]
international_color = [float(each) for each in df2016.international]

data = [
    {
        'y': df2016.teaching,
        'x': df2016.world_rank,
        'mode': 'markers',
        'marker': {
            'color': international_color,
            'size': num_students_size,
            'showscale': False
        },
        "text":df2016.university_name
            }
        ]
plot(data)


#%%

df2016.info()


df2016 = data5[data5.year == 2016].iloc[:20,:]

num_students_size = [float(each.replace(",",".")) for each in df2016.num_students]
international_color = [float(each) for each in df2016.international]

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
        "text":df2016.university_name
            }
        ]
plot(data)

#%% Histogram
# prepare data

x2011 = data5.student_staff_ratio[data5.year==2011]
x2012 = data5.student_staff_ratio[data5.year==2012]


trace1 = go.Histogram(
    x=x2011,
    opacity=0.75,
    name = "2011",
    marker=dict(color='rgba(171, 50, 96, 0.6)'))


trace2 = go.Histogram(
    x=x2012,
    opacity=0.75,
    name = "2012",
    marker=dict(color='rgba(20, 29, 196, 0.6)'))

data = [trace1,trace2]
layout = go.Layout(barmode="overlay",
                   title=" students-staff ratio in 2011 and 2012",
                   xaxis=dict(title='students-staff ratio'),
                   yaxis = dict(title="Count"),
                   )
fig= go.Figure(data=data,layout=layout)
plot(fig)
#%%
x2014 = data5.student_staff_ratio[data5.year==2014]
x2015 = data5.student_staff_ratio[data5.year==2015]


trace1 = go.Histogram(
    x=x2014,
    opacity=0.75,
    name = "2014",
    marker=dict(color='rgba(233,77, 106, 0.7)'))


trace2 = go.Histogram(
    x=x2015,
    opacity=0.75,
    name = "2015",
    marker=dict(color='rgba(280, 239, 96, 0.5)'))

data = [trace1,trace2]
layout = go.Layout(barmode="overlay",
                   title=" students-staff ratio in 2014 and 2015",
                   xaxis=dict(title='students-staff ratio'),
                   yaxis = dict(title="Count"),
                   )
fig= go.Figure(data=data,layout=layout)
plot(fig)

#%% Word Cloud

#data prepararion

x2011 = data5.country[data5.year == 2011]

plt.subplots(figsize=(8,8))

wordcloud = WordCloud(
    background_color="black",
    width=512,
    height=384,).generate(" ".join(x2011))


plt.imshow(wordcloud)
plt.axis("off")
plt.show()


#%%

x2011 = data5.country[data5.year == 2016]

plt.subplots(figsize=(10,10))

wordcloud = WordCloud(
    background_color="black",
    width=512,
    height=384,).generate(" ".join(x2011))


plt.imshow(wordcloud)
plt.axis("off")
plt.show()





















































