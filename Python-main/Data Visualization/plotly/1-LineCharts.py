# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# plotly
# import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

# word cloud library
from wordcloud import WordCloud

# matplotlib
import matplotlib.pyplot as plt
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory


timesData = pd.read_csv("timesData.csv")


timesData.info()

print("-"*40)
print(timesData.head())

#world rank = Dünya sıralaması
#university_name = Üniversite adı
#country = Ülke
#teaching = Öğretme
#international = Uluslar arası
#research = Araştırma
#citations = Alıntılar
#income = Gelir
#total_score = Toplam puan
#num students = Öğrenci sayısı
#student staff ratio = öğrenci personel oranı
#international students = uluslar arası öğrenciler

#famale male ratio = kadın erkek oranı
#year = yıl



#Line Charts

#burda 2011 yılındaki  citations ve teaching skorlarını 
#görseleştirecez

# prepare data frame
df = timesData.iloc[:100,:]

df.head()
#datamın ilk 5 verisini  alıyorum
#datamda ilk yuz veriyi alıyorum
df.tail()
#datamın son5 verisinş inceliyorum

# import graph objects as "go"
import plotly.graph_objs as go
#kutuphanemı go seklınde kısaltıp ımort edıyorum

# Creating trace1
#bir kalıp olusturalım
#plotly kutuphanesınden scatter kutuphanesını cagrıyorum
trace1 = go.Scatter(
                    x = df.world_rank,
                    #x ekseni,dünya sıralamasını koydum
                    y = df.citations,
                    #y ekseni,
                    mode = "lines",
                    #hangi plot kullanacagımız
                    name = "citations",
                    #plotumuzun ismi
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    #buda plotumuzun rengi rgb= red yesıl ve mavı renklerın bırlesımı
                    text= df.university_name)
                    #buda plotumuzun üzerinde yazan bilgi


# Creating trace2
trace2 = go.Scatter(
                    x = df.world_rank,
                    y = df.teaching,
                    mode = "lines+markers",      
                    name = "teaching",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'),
                    text= df.university_name)
data = [trace1, trace2]
#yaratıgım kalıpları data da birleştiriyorum

layout = dict(title = 'Citation and Teaching vs World Rank of Top 100 Universities',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False)
             )
#daha sonrada layoutumu yaratıyorum plotumun dısında kalan yer

fig = dict(data = data, layout = layout)
#sonrada tum verılerı bırlestirip bir figure olusturuyorum

iplot(fig)
#iplot seklınde cızdırıyorum




































