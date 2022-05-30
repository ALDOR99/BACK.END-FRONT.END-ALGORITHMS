# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:49:17 2021

@author: ali_d
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.image as mpimg


img = mpimg.imread("79.PNG")
print(img)

#Plotting numpy arrays as images

plt.figure(figsize=(10,6))
imgplot = plt.imshow(img)



#%%

plt.figure(figsize=(10,6))
lum_img = img[:,:,0]
plt.imshow(lum_img)




#%%

plt.figure(figsize = (10,6))
plt.imshow(lum_img,cmap="hot")

#%%

plt.figure(figsize=(10,6))

imgplot = plt.imshow(lum_img)

imgplot.set_cmap('nipy_spectral')

#%%
#Color scale


plt.figure(figsize = (10,6))
imgplot = plt.imshow(lum_img)
plt.colorbar()



#%% 
#Examining a specific data range

plt.figure(figsize=(10,6))
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
#%%
plt.figure(figsize=(10,6))
imgplot = plt.imshow(lum_img, clim=(0.2, 0.7))




#%%
fig = plt.figure(figsize=(10,6))
a = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(lum_img)
a.set_title('Before')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')
a = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0, 0.7)
a.set_title('After')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')
#%%Array Interpolation schemes

from PIL import Image

img = Image.open('h.PNG')
img.thumbnail((900,900), Image.ANTIALIAS)  # resizes image in-place
imgplot = plt.imshow(img)
#%%
imgplot = plt.imshow(img, interpolation="nearest")


#%%

imgplot = plt.imshow(img, interpolation="bicubic")


















