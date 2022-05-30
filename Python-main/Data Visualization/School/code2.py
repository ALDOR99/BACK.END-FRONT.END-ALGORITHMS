# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:00:43 2021

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

df2014 = data5[data5.year == 2014].iloc[:3,:]
print(df2014)

# prepare data frames
trace1 = go.Bar(
                x = df2014.university_name,
                y = df2014.citations,
                name = "citations",
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                             line=dict(color='rgb(0,0,0)',width=1.5)),
                text = df2014.country)
# create trace2 
trace2 = go.Bar(
                x = df2014.university_name,
                y = df2014.teaching,
                name = "teaching",
                marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = df2014.country)
data = [trace1, trace2]
layout = go.Layout(barmode = "group")
fig = go.Figure(data = data, layout = layout)
plot(fig)


#%%
a = go.Bar(
        x = df2014.university_name,
        y = df2014.citations,
        name = "citations",
        marker = dict(color = 'rgba(100, 44, 55, 0.5)',
                      line=dict(color='rgb(0,0,0)',width=1.5)),
        text = df2014.country)

b = go.Bar(
        x = df2014.university_name,
        y = df2014.teaching,
        name = "teaching",
        marker = dict(color = 'rgba(65, 55, 122, 0.5)',
                      line=dict(color='rgb(0,0,0)',width=1.5)),
        text = df2014.country)

data = [a, b]
layout = go.Layout(barmode = "group")
fig = go.Figure(data = data, layout = layout)
plot(fig)


#%% prepare data frames

df2014 = data5[data5.year == 2014].iloc[:3,:]

x = df2014.university_name

trace1 = {
  'x': x,
  'y': df2014.citations,
  'name': 'citation',
  'type': 'bar'
};

trace2 = {
  'x': x,
  'y': df2014.teaching,
  'name': 'teaching',
  'type': 'bar'
};

data = [trace1,trace2]

layout = {
  'xaxis': {'title': 'Top 3 universities'},
  'barmode': 'relative',
  'title': 'citations and teaching of top 3 universities in 2014'
};

fig = go.Figure(data = data,layout =layout)
plot(fig)
#%%

df2014 = data5[data5.year == 2014].iloc[:3,:]

x = df2014.university_name

trace1 = {
  'x': x,
  'y': df2014.international,
  'name': 'international',
  'type': 'bar'
};

trace2 = {
  'x': x,
  'y': df2014.total_score,
  'name': 'total_score',
  'type': 'bar',
};

data = [trace1,trace2]

layout = {
  'xaxis': {'title': 'Top 3 universities'},
  'barmode': 'relative',
  'title': 'total_score and total_score of top 3 universities in 2014'
};

fig = go.Figure(data = data,layout =layout)
plot(fig)

#%%

df2016 = data5[data5.year == 2016].iloc[:7,:]

y_saving = [each for each in df2016.research]
y_net_worth  = [float(each) for each in df2016.income]
x_saving = [each for each in df2016.university_name]
x_net_worth  = [each for each in df2016.university_name]
trace0 = go.Bar(
                x=y_saving,
                y=x_saving,
                marker=dict(color='rgba(171, 50, 96, 0.6)',line=dict(color='rgba(171, 50, 96, 1.0)',width=1)),
                name='research',
                orientation='h',
)
trace1 = go.Scatter(
                x=y_net_worth,
                y=x_net_worth,
                mode='lines+markers',
                line=dict(color='rgb(63, 72, 204)'),
                name='income',
)
layout = dict(
                title='Citations and income',
                yaxis=dict(showticklabels=True,domain=[0, 0.85]),
                yaxis2=dict(showline=True,showticklabels=False,linecolor='rgba(102, 102, 102, 0.8)',linewidth=2,domain=[0, 0.85]),
                xaxis=dict(zeroline=False,showline=False,showticklabels=True,showgrid=True,domain=[0, 0.42]),
                xaxis2=dict(zeroline=False,showline=False,showticklabels=True,showgrid=True,domain=[0.47, 1],side='top',dtick=25),
                legend=dict(x=0.029,y=1.038,font=dict(size=10) ),
                margin=dict(l=200, r=20,t=70,b=70),
                paper_bgcolor='rgb(248, 248, 255)',
                plot_bgcolor='rgb(248, 248, 255)',
)
annotations = []
y_s = np.round(y_saving, decimals=2)
y_nw = np.rint(y_net_worth)
# Adding labels
for ydn, yd, xd in zip(y_nw, y_s, x_saving):
    # labeling the scatter savings
    annotations.append(dict(xref='x2', yref='y2', y=xd, x=ydn - 4,text='{:,}'.format(ydn),font=dict(family='Arial', size=12,color='rgb(63, 72, 204)'),showarrow=False))
    # labeling the bar net worth
    annotations.append(dict(xref='x1', yref='y1', y=xd, x=yd + 3,text=str(yd),font=dict(family='Arial', size=12,color='rgb(171, 50, 96)'),showarrow=False))

layout['annotations'] = annotations

# Creating two subplots
fig = tools.make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                          shared_yaxes=False, vertical_spacing=0.001)

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)

fig['layout'].update(layout)

plot(fig)



#%% Pie Charts

df2016 = data5[data5.year == 2016].iloc[:7,:]
pie1 = df2016.num_students
pie1_list = [float(each.replace(',', '.')) for each in df2016.num_students]  
labels = df2016.university_name

#figure
fig = {
  "data": [
    {
      "values": pie1_list,
      "labels": labels,
      "domain": {"x": [0, .5]},
      "name": "Number Of Students Rates",
      "hoverinfo":"label+percent+name",
      "hole": .3,
      "type": "pie"
    },],
  "layout": {
        "title":"Universities Number of Students rates",
        "annotations": [
            { "font": { "size": 20},
              "showarrow": False,
              "text": "Number of Students",
                "x": 0.20,
                "y": 1
            },
        ]
    }
}
plot(fig)

#%%

df2016 = data5[data5.year == 2016].iloc[:7,:]
pie1 = df2016.num_students
pie1_list = [float(each.replace(',', '.')) for each in df2016.num_students]  
labels = df2016.university_name

#figure
fig = {
  "data": [
    {
      "values": pie1_list,
      "labels": labels,
      "domain": {"x": [0, .5]},
      "name": "Number Of Students Rates",
      "hoverinfo":"label+percent+name",
      "hole": .3,
      "type": "pie"
    },],
  "layout": {
        "title":"Universities Number of Students rates",
        "annotations": [
            { "font": { "size": 30},
              "showarrow": True,
              "text": "Number of Students",
                "x": 0.20,
                "y": 1
            },
        ]
    }
}
plot(fig)
#%%
df2016 = data5[data5.year == 2016].iloc[:7,:]
pie1 = df2016.num_students
pie1_list = [float(each.replace(',', '.')) for each in df2016.num_students]  
labels = df2016.income

#figure
fig = {
  "data": [
    {
      "values": pie1_list,
      "labels": labels,
      "domain": {"x": [0, .5]},
      "name": "Number Of Students Rates",
      "hoverinfo":"label+percent+name",
      "hole": .3,
      "type": "pie"
    },],
  "layout": {
        "title":"Universities Number of Students rates",
        "annotations": [
            { "font": { "size": 20},
              "showarrow": False,
              "text": "Number of Students",
                "x": 0.20,
                "y": 1
            },
        ]
    }
}
plot(fig)






























