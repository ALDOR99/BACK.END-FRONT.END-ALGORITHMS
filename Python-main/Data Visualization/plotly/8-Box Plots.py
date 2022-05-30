# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:51:22 2021

@author: ali_d
"""

#Box Plot

import numpy as np 
import pandas as pd 


from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

import matplotlib.pyplot as plt


timesData = pd.read_csv("timesData.csv")
#dataFramem
x2015 = timesData[timesData.year == 2015].iloc[:100,:]
#2015 yılına ait ilk 100 universitem filtreliyorum


trace0 = go.Box(
    y = x2015.total_score,
    
    
    name  = "total score of universities in 2015",
    marker=dict(
        color = "rgb(12,12,140)",
        
        )
    )
trace1 = go.Box(
    y = x2015.research,
    name  = "research of universities in 2015",
    marker=dict(
        color = "rgb(12,128,148)",
        
        )
    )
data = [trace0,trace1]

iplot(data)




















































































