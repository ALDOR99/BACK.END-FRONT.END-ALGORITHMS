# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 15:58:08 2021

@author: ali_d
"""

"pip install missingno"


import numpy as np
import pandas as pd

dictionary = {"column1":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
              
              "column2":[1,2,3,4,np.nan,6,7,8,np.nan,10,np.nan,12,13,14,15,16,np.nan,18,np.nan,20],
              
              "column3":[1,2,3,4,np.nan,6,7,8,9,10,11,12,13,np.nan,15,16,17,18,np.nan,20]}

data_missingo = pd.DataFrame(dictionary)
print(data_missingo.head())



import missingno as msno

msno.matrix(data_missingo)
plt.show()


#%% missingno bar plot

msno.bar(data_missingo)
plt.show()

#%%















