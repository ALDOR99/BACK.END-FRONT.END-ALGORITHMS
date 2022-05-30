# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:36:53 2021

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



#%% Box Plots
# data preparation
x2015 = data5[data5.year == 2015]

trace0 = go.Box(
    y=x2015.total_score,
    name = 'total score of universities in 2015',
    marker = dict(
        color = 'rgb(12, 12, 140)',
    )
)

trace1 = go.Box(
    y=x2015.research,
    name = 'research of universities in 2015',
    marker = dict(
        color = 'rgb(12, 128, 128)',
    )
)
data = [trace0, trace1]
plot(data)
   
   
#%% Scatter Matrix Plots
   

import plotly.figure_factory as ff

dataframe = data5[data5.year == 2015]
datta2015 = dataframe.loc[:,["research","international", "total_score"]]
datta2015["index"] = np.arange(1,len(datta2015)+1)

fig = ff.create_scatterplotmatrix(datta2015, diag='box', index='index',colormap='Portland',
                                  colormap_type='cat',
                                  height=700, width=700)
plot(fig)
#%%

import plotly.figure_factory as ff

dataframe = data5[data5.year == 2015]
datta2015 = dataframe.loc[:,["research","international", "total_score"]]
datta2015["index"] = np.arange(1,len(datta2015)+1)

fig = ff.create_scatterplotmatrix(datta2015, diag='box', index='index',#colormap='Portland',
                                  colormap_type='cat',
                                  height=700, width=700)
plot(fig)
   

#%% Inset Plots

# first line plot
trace1 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.teaching,
    name = "teaching",
    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
)
# second line plot
trace2 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.income,
    xaxis='x2',
    yaxis='y2',
    name = "income",
    marker = dict(color = 'rgba(160, 112, 20, 0.8)'),
)
data = [trace1, trace2]
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

fig = go.Figure(data=data, layout=layout)
plot(fig)
#%%

# first line plot
trace1 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.teaching,
    name = "teaching",
    marker = dict(color = 'rgba(199, 142, 134, 0.8)'),
)
# second line plot
trace2 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.citations,
    xaxis='x2',
    yaxis='y2',
    name = "income",
    marker = dict(color = 'rgba(1, 122, 112, 0.8)'),
)
data = [trace1, trace2]
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

fig = go.Figure(data=data, layout=layout)
plot(fig)

#%% 3D Scatter Plot with Colorscaling

# create trace 1 that is 3d scatter
trace1 = go.Scatter3d(
    x=dataframe.world_rank,
    y=dataframe.research,
    z=dataframe.citations,
    mode='markers',
    marker=dict(
        size=10,
        color='rgb(255,0,0)', # set color to an array/list of desired values      
    )
)

data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0  
    )
    
)
fig = go.Figure(data=data, layout=layout)
plot(fig)

#%%

trace1 = go.Scatter3d(
    x=dataframe.world_rank,
    y=dataframe.total_score,
    z=dataframe.research,
    mode='markers',
    marker=dict(
        size=10,
        color='rgb(255,0,0)', # set color to an array/list of desired values      
    )
)

data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0  
    )
    
)

fig = go.Figure(data=data, layout=layout)
plot(fig)
   
 
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    








































