# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 11:02:44 2021

@author: ali_d
"""

import numpy as np

liste = [0,1,2,3,4,5,6,7,8,9]

#numpy array
num_array = np.array([0,1,2,3,4,5,6,7,8,9])

print(num_array)
print(type(num_array))
#%%  Dizinin boyutunu bulmak : ndarray.ndim

num_array1 = np.array([0,1,2,3,4,5,6,7,8,9])

print(num_array1.ndim)
#dizi boyutu


num_array2 = np.array([[0,1,2,3,4,5,6,7,8,9]])

print(num_array2)
print(num_array2.ndim)

#%% Dizinin satır ve sütun sayısını bulmak: ndarray.shape

num_array1 = np.array([0,1,2,3,4,5,6,7,8,9])

print(num_array1.shape,num_array1.ndim)
#10 tane elemandan olusan 1 boyutlu dizi(vektör)

#%%

num_array2 = np.array([[0,1,2,3,4,5,6,7,8,9]])

print(num_array2.ndim,num_array2.shape)
#1 satır ve 10 sütündan olusan 2 boyutlu bir dizi(matris)
#%%
#Dizinin satır ve sütun sayısını değiştirmek : ndarray.reshape()

num_array = np.array([0,1,2,3,4,5,6,7,8,9])
print(num_array)

print("-"*10)

print(num_array.reshape(10,1))

print()

print(num_array.reshape(5,2))

print()

print(num_array.reshape(2,5))
print()
# matris ve yeniden şekillendirilen matris aynı sayıda elemana sahip olmalıdır.

#%% np.arange()
#np.arange(başlangıç,bitiş,adım sayısı)

a = np.arange(0,10,2)

print(a)

b = np.arange(0,20)
print(b)

print()

c = np.arange(10)
print(c)


#%%Dizinin elemanlarını seçmek

numpy_array = np.array([0,1,2,3,4,5,6,7,8,9])

numpy_array = numpy_array.reshape(5,2)
print(numpy_array)
print("-")
#%%
#dizinin herhangi bir elemanını seçmek

#1.satır

first_row = numpy_array[0]
print(first_row)

print("-")

second_row = numpy_array[1]
print(second_row)
print()
#%%
#1.ve 2.satırını alalım

first_and_second_rows = numpy_array[0:2]
print(first_and_second_rows)
print("-")
print()
#%%
##Dizinin herhangi bir kolonunu seçmek

first_column = numpy_array[:,0]
print(first_column)
print()
#%%
#1. ve 2. sütun
first_and_second_column = numpy_array[:,0:2]

print(first_and_second_column)
print()
print(first_column)

print()

#%%Dizinin herhangi bir elemanını seçmek

selecting_item = numpy_array[3,1]
print(selecting_item)


selecting_item = numpy_array[0,0]
print(selecting_item)

selecting_item = numpy_array[0,1]
print(selecting_item)

selecting_item = numpy_array[1,1]
print(selecting_item)


selecting_item = numpy_array[2,1]
print(selecting_item)























































