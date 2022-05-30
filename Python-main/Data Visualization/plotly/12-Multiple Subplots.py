# -*- coding: utf-8 -*-
"""
Created on Sun May 30 13:55:36 2021

@author: ali_d
"""

#Multiple Subplots

#bırden fazla features gorselestırmek ıstersek ayn frame ıcınde
#subplots kullanıyoruz

import numpy as np 
import pandas as pd 


from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

import matplotlib.pyplot as plt

import plotly.graph_objs as go

timesData = pd.read_csv("timesData.csv")

dataframe = timesData[timesData.year == 2015]


trace1 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.research,
    name = "research"
)
#tracelerım

trace2 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.citations,
    xaxis='x2',
    yaxis='y2',
    name = "citations"
)
trace3 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.income,
    xaxis='x3',
    yaxis='y3',
    name = "income"
)
trace4 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.total_score,
    xaxis='x4',
    yaxis='y4',
    name = "total_score"
)
data = [trace1,trace2,trace3,trace4]
#tracelerımı data listesinde bırlestırıyorum

layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.45]
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
    xaxis2=dict(
        domain=[0.55, 1]
    ),
    xaxis3=dict(
        domain=[0, 0.45],
        anchor='y3'
    ),
    xaxis4=dict(
        domain=[0.55, 1],
        anchor='y4'
    ),
    yaxis2=dict(
        domain=[0, 0.45],
        anchor='x2'
    ),
    yaxis3=dict(
        domain=[0.55, 1]
    ),
    yaxis4=dict(
        domain=[0.55, 1],
        anchor='x4'
    ),
    title = 'Research, citation, income and total score VS World Rank of Universities'
)
#layoutumu olusturuyorum
fig = go.Figure(data=data,layout=layout)
#figurumde birleştiriyorum
iplot(fig)
#plot etırıyorum


