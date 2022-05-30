# -*- coding: utf-8 -*-
"""
Created on Fri May 28 07:07:20 2021

@author: ali_d
"""

#PİE PLOT
# 2016 yılındaki ilk 7 universitenin ogrencilerin oraltıları
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# plotly
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

from wordcloud import WordCloud


import matplotlib.pyplot as plt


timesData = pd.read_csv("timesData.csv")

df2016 = timesData[timesData.year == 2016].iloc[:7,:]
#2016 yılına ait ilk 7 verimi filtreledim

a=df2016.head()
# num_student kısmında ondalıklı sayılar araya virgül konularak yazılmaz
#virgülü noktaya cevirmemiz lazım

print("-"*40)
df2016.info()

#burda num_students object bunu floata çevirmemiz gerek

pie1 = df2016.num_students


pie1_list = [float(each.replace("," , ".")) for each in df2016.num_students]

# df2016.num_students bunun ıcındekı each ıcındekı virgulu noktayla replace et diyorum

#str(2,4) => str(2.4) => float(2.4) =2.4

labels = df2016.university_name

#figure
fig = {
  "data": [
    {
      "values": pie1_list,
      # pie1 listem
      "labels": labels,
      # labelerımde benım universite isimlerim
      "domain": {"x": [0, .5]},
      
      "name": "Number Of Students Rates",
      
      "hoverinfo":"label+percent+name",
      #oranı + yuzdesı + ismi
      
      "hole": .3,
      #delik buyuklugu 
      "type": "pie"
      #plotumun tipi pie
      
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
iplot(fig)

print("-"*40)
#############
print(df2016.head(7))
np.sum(df2016.num_students)

np.sum(pie1_list)
#benım 2016daki num_students larımın toplamı 95 .725

#Harvard Universitesinde 20.152 tane ogrencım var
#bu işlemleri pyplot otomatıkman orantısal olarak verıyor
# 20.152 * 100 / 95.725
#bu işlemi yapmam gerekki orantısal halini buliyim

#################
#[1,2,3,4] = 10
#1in bu listedeki oranı  1*100/10 =10
# 2nin bu listedeki oranı  2*100/10 =20

#df2016.head(7)
#oxford üniversitesinin harvard üniversitesine gore oranı
#
20.152*100/(20.152+19.919)
#
#orantılamayı bu sekılde yapıyoruz






















