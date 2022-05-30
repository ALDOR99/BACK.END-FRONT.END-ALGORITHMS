# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:44:16 2021

@author: ali_d
"""

import numpy as np

#Matrislerde aritmetik işlemler


numpy_array = np.array([1,2,3,4,5,6,7,8,9])
numpy_array = numpy_array.reshape(3,3)
print(numpy_array)
print()

#
print(numpy_array+numpy_array)

print()

#
print(numpy_array - numpy_array)
print()

print(numpy_array+5)
print()


#
print(numpy_array*5)
print()

#
print(numpy_array**2)


#%% Özel foksiyonlar ile işlemler

numpy_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_array = numpy_array.reshape(3,3)


print(np.sin(numpy_array))
print()

#
print(np.cos(numpy_array))
print()



print(np.sqrt(numpy_array)) 
print()


#
print(np.exp(numpy_array))
print()


#
print(np.log(numpy_array))
print()


#%% Matrislerin çarpımı



numpy_array = np.array([0,1,2,3,4,5,6,7,8,9])

numpy_array1 = numpy_array.reshape(5,2)
print(numpy_array1)
print()
#
numpy_array2 = numpy_array.reshape(2,5)
print(numpy_array2)
print()

print(np.dot(numpy_array1,numpy_array2))

#%% Matrisin transpozu


numpy_array = np.array([0,1,2,3,4,5,6,7,8,9])
numpy_array = numpy_array.reshape(5,2)

print(numpy_array)
print()

#
print(numpy_array.T)
print()
print(numpy_array.reshape(2,5))



















































































