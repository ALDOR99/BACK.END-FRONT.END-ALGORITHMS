# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:44:39 2021

@author: ali_d
"""

import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
#x değerleri
y = [1,4,9,16]
#y değerleri

#plt.plot(x,y,"--g")
#x ve y degerlerını plot etır "--g" cıgzgı olsun ve renk bilgisi

plt.plot(x,y,"o--r")
#"o--r" x ve ynın kesıstıgı noktaya nokta koyuyor

plt.axis([0,6,0,20])
#plotun axis uzunlukları

plt.title("Grafik Başlığı")
#baslıgım

plt.xlabel("x label")
#x eksenı baslıgı
plt.ylabel("y label")
#y eksenı baslıgı
plt.show()
#show
#%%

x1 = np.linspace(0,2,100)
#0 ile 2 arasında 100 esıt parcaya bolsun

plt.plot(x1,x1,label="linear",color="r")
plt.plot(x1,x1**2,label="quadratic",color = "y")
plt.plot(x1,x1**3,label="cubic",color = "g")


plt.xlabel("x label")
plt.ylabel("y label")

plt.title("Baslık")
plt.legend()


#%%

x = np.linspace(0,2,100)

fig,axs =  plt.subplots(3)

axs[0].plot(x,x,color="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2,color="green")
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="yellow")
axs[2].set_title("cubic")

plt.tight_layout()

plt.show()


#%%
x = np.linspace(0,2,100)

fig,axs =  plt.subplots(2,2)

fig.suptitle("grafik başlığı")


axs[0,0].plot(x,x,color="red")

axs[0,1].plot(x,x**2,color="green")

axs[1,0].plot(x,x**3,color="yellow")

axs[1,1].plot(x,x**4,color="blue")


plt.show()






















