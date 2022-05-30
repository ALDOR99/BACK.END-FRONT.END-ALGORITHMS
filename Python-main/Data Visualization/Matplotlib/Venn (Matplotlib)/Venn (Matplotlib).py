# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:29:07 2021

@author: ali_d
"""

#Venn (Matplotlib)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib_venn as venn

from matplotlib_venn import venn2


data = pd.read_csv("Iris.csv")

sepal_length = data.iloc[:,0]
#
sepal_width = data.iloc[:,1]
#
petal_length = data.iloc[:,2]
#
petal_width = data.iloc[:,3]


venn2(subsets=(len(sepal_length)-15,len(sepal_width)-15,15),
      set_labels=("sepal_lenght","sepal_width"))
plt.show()


















