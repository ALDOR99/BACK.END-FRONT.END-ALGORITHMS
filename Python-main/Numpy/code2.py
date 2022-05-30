# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:03:32 2021

@author: ali_d
"""

#code2

import numpy as np


#Diziyi Ters Çevirme

numpy_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(numpy_array)
print()
#
numpy_array = numpy_array.reshape(5,2)#satır,sutun
print(numpy_array)
print()
#
print(numpy_array[::-1])


#%%0 matrisi oluşturmak:np.zeros()

print(np.zeros((5,4)))


print("-"*30)
#np.ones

print(np.ones(((3,3,3,))))
print("-"*50)

#bir matris olusturmak
#4x4 matris

print(np.eye(4))
#%% Matrisleri birleştirmek
numpy_array = np.array([0,1,2,3,4,5,6,7,8,9])
numpy_array = numpy_array.reshape(5,2)
print(numpy_array)

print()


#satır bazlı birleştirme

print(np.concatenate([numpy_array,numpy_array],axis =0))

print("-"*40)
#

#sütun bazlı birleştirme

print(np.concatenate([numpy_array,numpy_array],axis=1))

#%%  Numpy ile Matematiksel İşlemler
# sum(toplam), max ve min değerlerini hesaplamak

numpy_array = np.array([0,1,2,3,4,5,6,7,8,9])
numpy_array = numpy_array.reshape(5,2)
print(numpy_array)

#
print(numpy_array.max())

#
print(numpy_array.min())

#
print(numpy_array.sum())

#Satırların Toplamı
print(numpy_array.sum(axis=1))

#sütünların toplamı
print(numpy_array.sum(axis=0))

#%% mean, median, varyans ve standart sapma hesaplamak

numpy_array = np.arange(0,11)
print(numpy_array)

#
print(numpy_array.mean())

print(np.median(numpy_array))
print("-")
#
print(numpy_array.var())

#
print(numpy_array.std())

#%%




























