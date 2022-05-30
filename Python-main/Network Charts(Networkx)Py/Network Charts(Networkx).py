# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:02:34 2021

@author: ali_d
"""
import numpy as np 
import pandas as pd 


data = pd.read_csv("Iris.csv")


corr = data.iloc[:,0:4].corr()
print(corr)

print()

import networkx as nx

links =corr.stack().reset_index()
links.columns = ["var1","var2","value"]


# correlation
threshold = -1

links_filtered=links.loc[ (links['value'] >= threshold ) & (links['var1'] != links['var2']) ]

G=nx.from_pandas_dataframe(links_filtered, 'var1', 'var2')


nx.draw_circular(G, with_labels=True, node_color='orange',
                 node_size=300, edge_color='red', linewidths=1, font_size=10)
























