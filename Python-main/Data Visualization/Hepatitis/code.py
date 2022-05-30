# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 13:51:07 2021

@author: ali_d
"""

#
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objs as go
import klib



data = pd.read_csv("hepatitis_csv.csv")

print(data.info())

print("-"*30)

print(data.shape)
#toplam sütun ve satır sayısı

a =(data.head(5))
print("-"*30)

print(data.describe())
print()
b =(data.describe().T)
print(b)


print("-"*40)

klib.missingval_plot(data)
#%%

data1=data.dropna()
data1.info()
print("-"*30)

print(data1.columns)
print()
print(data.columns)

#%%
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot, plot
import plotly.graph_objects as go
pyo.init_notebook_mode()
import plotly.figure_factory as ff


px.scatter(data1, y='bilirubin',x='age', color='sex')

#%%Preprocessing

def preprocess_inputs(df, drop_protime=False):
    df = data1.copy()
    
    # Identify the continuous numeric features
    continuous_features = ['age', 'bilirubin', 'alk_phosphate', 'sgot', 'albumin', 'protime']
    
    # Fill missing values
    for column in continuous_features:
        df[column] = df[column].fillna(df[column].mean())
    
    for column in df.columns.drop(continuous_features):
        df[column] = df[column].fillna(df[column].mode().sample(1, random_state=1).values[0])
    
    # Convert the booleans columns into integer columns
        for column in df.select_dtypes('bool'):
            df[column] = df[column].astype(np.int)
    
    # Encode the sex column as a binary feature
    df['sex'] = df['sex'].replace({
        'female': 0,
        'male': 1
    })
    
    # Shuffle the data
    df = df.sample(frac=1.0, random_state=1).reset_index(drop=True)
    
    # Change label name
    df = df.rename(columns={'class': 'label'})
    
    # Drop protime
    if drop_protime == True:
        df = df.drop('protime', axis=1)
    
    # Split df into X and y
    y = df['label']
    X = df.drop('label', axis=1)
    
    return X, y

X, y = preprocess_inputs(data, drop_protime=True)

print(X)
#%%
print(X.info())
#%%
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style = "ticks", context = "talk")
plt.figure(figsize=(20, 12))
sns.heatmap(data1.corr(), annot=True, cmap='viridis')
#%%
plt.figure(figsize=(20, 10))
sns.displot(data1.age, bins=40)
#%%

sns.kdeplot(data1.age)

#%%
px.histogram(data1.age)
#%%
plt.figure(figsize=(20, 10))
sns.displot(data1.bilirubin, bins=40)

#%%
sns.kdeplot(data1.bilirubin)


#%%
plt.figure(figsize=(20, 10))
data1['sex'].value_counts().plot(kind="bar",
                                 color='blue', 
                                 title='Gender Distribution')

#%%
px.pie(data1['sex'], labels = data1['sex'].value_counts().index,
       values = data1['sex'].value_counts().values,
       names = data1['sex'].value_counts().index,
       title = 'Gender Distribution in the Data'
      )


#%%

from plotly.subplots import make_subplots
# features = ['age', 'sex', 'steroid', 'antivirals', 'fatigue', 'malaise', 'anorexia',
#        'liver_big', 'liver_firm', 'spleen_palpable', 'spiders', 'ascites',
#        'varices', 'bilirubin', 'alk_phosphate', 'sgot', 'albumin',
#        'histology', 'class']
# rows = 3
# cols = 5
# fig = make_subplots(rows=rows, cols=cols, subplot_titles=features)
# x, y = np.meshgrid(np.arange(rows)+1, np.arange(cols)+1)
# count  = 0
# for row, col in zip(x.T.reshape(-1), y.T.reshape(-1)):
#     fig.add_trace(
#         go.Histogram(x = data1[features[count]].values),
#         row = row,
#         col = col
#     )
#     count+=1
    
# fig.update_layout(height=900, width=900, title_text='Feature Distribution', showlegend=False)
# fig.show()

#%%
box_cols = ['age', 'sex', 'steroid', 'antivirals', 'fatigue', 'malaise', 'anorexia',
       'liver_big', 'liver_firm', 'spleen_palpable', 'spiders', 'ascites',
       'varices', 'bilirubin', 'alk_phosphate', 'sgot', 'albumin',
       'histology', 'class']
rows = 3
cols = 5
fig = make_subplots(rows=rows, cols=cols, subplot_titles=box_cols)
x, y = np.meshgrid(np.arange(rows)+1, np.arange(cols)+1)
count = 0
for row, col in zip(x.T.reshape(-1), y.T.reshape(-1)):
    try:
        fig.add_trace(
            go.Box(x = data1[box_cols[count]].values, name=''),
            row = row,
            col = col
        )
        count+=1
    except:
        break
    
fig.update_layout(height=900, width=900, title_text='Boxplot Distribution', showlegend=False)
fig.show()
































































