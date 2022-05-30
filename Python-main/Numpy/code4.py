# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 14:22:33 2021

@author: ali_d
"""

#Numpy’da Koşul İfadeleri ile Çalışmak
import numpy as np

nunmpy_array = np.array([0,1,2,3,4,5,6,7,8,9])

boolean_array = nunmpy_array >= 6

print(boolean_array)


#6 ve 6'dan büyük elemanlar

print(nunmpy_array[boolean_array])
print()

#6'dan küçük elemanlar

#
print(nunmpy_array<6)
print()
#
print(nunmpy_array[nunmpy_array<6])
























































































