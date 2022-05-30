# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:27:22 2021

@author: ali_d
"""

# 3D Scatter Plot With Colorscaling

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



trace1 = go.Scatter3d(
    
    x=dataframe.world_rank,
    #x eksenim dunya sıralamam
    y=dataframe.research,
    # y eksenim research puanım
    z=dataframe.citations, 
    #z eksenimde citations puanım
    mode ="markers",
    #modum markers nokta nokta seklınde olan yanı
    marker=dict(
        size=10,
        #
        color='rgb(255,0,0)',
        #
        )
    )

data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        )
    )
#margin 
fig=go.Figure(data=data,layout=layout)
iplot(fig)





































































