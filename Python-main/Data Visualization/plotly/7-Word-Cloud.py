# -*- coding: utf-8 -*-
"""
Created on Fri May 28 18:02:17 2021

@author: ali_d
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go
#
from wordcloud import WordCloud
#
import matplotlib.pyplot as plt


timesData = pd.read_csv("timesData.csv")


#Word Cloud

# 2011 yıılındaki universite sıralamasına bak bu universitelerin
# aid oldugu ulkelere var  bu ulkelerden en cok hangi ulkenin 
#kullanıldıgını bana gorselestir


#datamı filtreliyorum
x2011 = timesData.country[timesData.year == 2011]


plt.subplots(figsize=(8,8))
#matplotlib ile 8e 8lik bir plot olusturuyorum
wordcloud = WordCloud(
                          background_color='white',
                          width=512,
                          height=384
                         ).generate(" ".join(x2011))
#WordCloud kutuphanesini cagrıyorum
#background_color arka plan rengım beyaz olsun dıyorum
#yuksekligimi ve genisligimi ayarlıyorum
#.generate(" ".join(x2011)) bu kullanılan kelimeleri ayır
#ona gore bana en cok yazılı olanları buyuk bir sekılde plot ettir

plt.imshow(wordcloud)

plt.axis('off')
#x ve ye eksenlerını kapat
plt.savefig('graph.png')
#ardından resmı bulundugu dosyaya kayıt et
plt.show()
#plotu goster































