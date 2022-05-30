# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 17:14:04 2021

@author: ali_d
"""

import pandas as pd
import matplotlib.pyplot as plt



# load iris data
data = pd.read_csv('Iris.csv')
data = data.drop(['Id'],axis=1)


# Make the plot
plt.figure(figsize=(15,10))
parallel_coordinates(data, 'Species', colormap=plt.get_cmap("Set1"))
plt.title("Iris data class visualization according to features (setosa, versicolor, virginica)")
plt.xlabel("Features of data set")
plt.ylabel("cm")
plt.savefig('graph.png')
plt.show()