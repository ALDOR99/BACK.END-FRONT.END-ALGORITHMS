# -*- coding: utf-8 -*-

"""
Created on Sat May 29 14:18:17 2021

@author: ali_d
"""




#Sacatter Plot Matrix

#iki tane features arasındakı covariance ilişkiyi gormek ıcın
#kullanıyoruz



import numpy as np 
import pandas as pd 


from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

import matplotlib.pyplot as plt

#
import plotly.figure_factory as ff
#burda figure_factory kullanmak ıstıyruz ve ff olarak kısaltıyruz




timesData = pd.read_csv("timesData.csv")


# import figure factory
import plotly.figure_factory as ff
# prepare data
dataframe = timesData[timesData.year == 2015]
#datada sadece 2015 yılına aıt verılerı kullanmak ıstıyorum

data2015 = dataframe.loc[:,["research","international", "total_score"]]
#burda datamda karsılastırmak ıstedıgım featureslar bunları data2015 ıcıne atıyorum


data2015["index"] = np.arange(1,len(data2015)+1)
#daha sonra dataframemın uzunlugunda arange bır liste hazırlayıp bunu
#dataframemın indexıne features acıp esitliyoruz


# scatter matrix
fig = ff.create_scatterplotmatrix(data2015, diag='box', index='index',colormap='Portland',
                                  colormap_type='cat',
                                  height=700, width=700)
#ff kutuphanemden create_scatterplotmatrix methodumu cagrıyorum

iplot(fig)














































































































































