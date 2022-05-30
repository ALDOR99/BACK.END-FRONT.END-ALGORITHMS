# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:14:32 2021

@author: ali_d
"""

import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(-10,9,20)
#-9 ile 10 arasında esıt aralıklarda 20 tane deger olusturdum

y = x ** 3
z =  x**2

figure = plt.figure()
#bos bir figur olusturuyorum

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
#konumlarım soldan 0.2 altan 0.2 genıslık ve yukseklık olarakda 0.8

axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("X axis")
axes_cube.set_ylabel("Y axis")
axes_cube.set_title("Cube")


axes_cube = figure.add_axes([0.15,0.6,0.25,0.25])
axes_cube.plot(x,z,"r")
axes_cube.set_xlabel("X axis")
axes_cube.set_ylabel("Y axis")
axes_cube.set_title("Square")
plt.show()



#%%

x = np.linspace(-10,9,20)
#-9 ile 10 arasında esıt aralıklarda 20 tane deger olusturdum

y = x ** 3
z =  x**2



figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=4)

plt.show()


#%%

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8))

axes[0].plot(x,y,"r")
axes[0].set_title("Cube")

axes[1].plot(x,z,"g")
axes[1].set_title("Square")

fig.savefig("matplotlib")
plt.tight_layout()
plt.show()

###
plt.bar([0.25,1.25,2.25,3.25,4.25],[90,80,30,70,90],label="Bmv",width=.5)

plt.bar([0.15,1.35,2.15,3.45,3.25],[40,80,80,60,70],label="Audi",width=.5)

plt.legend()
plt.xlabel("gün")
plt.ylabel("mesafe(km)")
plt.title("Araç Bilgileri")

plt.show()














































