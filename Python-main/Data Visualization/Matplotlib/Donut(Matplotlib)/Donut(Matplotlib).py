# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:06:52 2021

@author: ali_d
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



data = pd.read_csv("Iris.csv")


feature_names = "sepal_length","sepal_width","petal_length","petal_width"

feature_size = [len(sepal_length),len(sepal_width),len(petal_length),len(petal_width)]

# create a circle for the center of plot
circle = plt.Circle((0,0),0.5,color = "white")

plt.pie(feature_size, labels = feature_names, colors = ["red","green","blue","cyan"] )

p = plt.gcf()

p.gca().add_artist(circle)
plt.title("Number of Each Features")
plt.show()


















