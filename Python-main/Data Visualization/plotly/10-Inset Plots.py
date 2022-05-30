# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:10:45 2021

@author: ali_d
"""

# Inset Plots

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
    x = dataframe.world_rank,
    #x eksenim dunya sıralamam
    
    y = dataframe.teaching,
    #y eksenim teachin skorum
    
    name = "teaching",
    #label ismim
    marker = dict(color = "rgba(16,112,2,0.8)"),
    )
    #rengim ve saydamlığım


trace2 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.income,
    xaxis='x2',
    yaxis='y2',
    name = "income",
    marker = dict(color = 'rgba(160, 112, 20, 0.8)'),
)


data = [trace1,trace2]
#verilerimi data içinde birleştiriyorum

layout = go.Layout(
    xaxis2=dict(
        domain=[0.6, 0.95],
        anchor='y2',        
    ),
    yaxis2=dict(
        domain=[0.6, 0.95],
        anchor='x2',
    ),
    title = 'Income and Teaching vs World Rank of Universities'

)
#bunun dıger plotlardan farkı ıkı tane plot iç içe 
#domain yerımızı belirtiyor
#anchor='y2' bu ıkıncı plotumu cızmek için kulandığımız bir sey
fig = go.Figure(data=data, layout=layout)
#figurumu olusturuyorum
iplot(fig)
#plot etırıyorum







































