# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:57:01 2021

@author: ali_d
"""
## Numpy

import numpy as np

#python listy

# lst = [1,2,3,4,5,6,7,8,9]
# #numy array
# a = np.array(lst)
# print(a)
# print(type(a))
# print()

# py_multi = [[1,2,3],[4,5,6],[7,8,9]]

# np_multi = np_array.reshape(3,3)

np_array = np.array([1,2,3,4,5,6,7,8,9])

mp_multi = np_array.reshape(3,3)

#reshape = yenıden sekılendırmek

print(mp_multi)
print(mp_multi.ndim)
#burda 2 boyutlu bır matrıs oldugunu soyluyor
print()
print(mp_multi.shape)

#%% numpy dızılerı ıle calısma
import numpy as np 

result = np.array([1,3,5,7,9])

print(result)
print(type(result))

print()

result1 = np.arange(1,11) #10degerı ıcın 11# 

print(result1)
print(type(result1))
print()

result2 = np.arange(10,100,5)
print(result2)
print()

result3 = np.zeros(10)
print(result3)

result4 = np.ones(10)
print()

result5 = np.linspace(0,100,5)
result6 = np.linspace(0,5,5)

print(result5)
print(result6)
print()
resultx = np.random.randint(0,10)
print(resultx)
print()
resultx1 = np.random.randint(20)
print(resultx1)

resultx2 = np.random.rand(5) # 0 ile 1  arasında 5 tane sayı uretır
print(resultx2)
print()

resultx3 = np.random.randn(5) # eksi degerlerde ısın ısıne gırer
print(resultx3)
print()
#-------------

np_array = np.arange(50)
a1 = np_array.reshape(5,10)
print()
print(a1.sum(axis=1)) #satırların toplamı
print()
print(a1.sum(axis=0)) #sutunların degelerını aldık
print()
print(a1)
print()
#-------------

result11 = np.random.randint(1,100,10)
print(result11)

print()

print("-----")
print()

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)

resultaa1 = rnd_numbers.max()
resultaa2 = rnd_numbers.min()
resultaa3 = rnd_numbers.mean() #ortalama
print("----")

resultaa4 = rnd_numbers.argmax() #

resultaa5 = rnd_numbers.argmin()

print(resultaa1)
print(resultaa2)
print(resultaa3)
print()
print(resultaa4) #en yuksek sayının ındex numarasını verıyor
print("-----")
print(resultaa5)


#%% Numpy Dizilerini İndeksleme
import numpy as np

number = np.array([0,5,10,15,20,25,50,75])
print(number[5])
print(number[7])
print(number[0:3])
print(number[:3])
print(number[:])
print(number[::-1])
print()

number2= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(number2)
print()

result1 = number2[2]
result2 = number2[0,1]
result3 = number2[1,1]
result4 = number2[2,1]

print(result1)
print()
print(result2)
print(result3)
print(result4)
print()
print(number2[:,2])
print(number2[0,2])
#
print(number2[:,0:2]) #
#
print()
print(number2[-1:,0:2]) #
print()
print(number2[-1,:]) #
print()
print(number2[:3,:3]) #dızı oldugu gıbı gelır
print()
print(number2[:2,:2])
print()

arr1 = np.arange(10)
#print(arr1)
#arr2 = arr1 #referans


arr1[1] =10
print(arr1)

# aynı ıd adresını paylastıgı ıcın degısıklık ıkısınıde etkıler

arr2 = arr1.copy()
print(arr2)

arr2[0]=73
print(arr2)

#---------------------------------------------------------------
#%% Numpy Dizi Operasyonları
import numpy as np

numbers1 = np.random.randint(10,100,6)

numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1+numbers2
print(result)
print()

result1 = numbers1 +10
print(result1)
print()

result3 = numbers2-numbers1
print(result3)
print()
result4 = numbers1*numbers2
print(result4)
print("---")
result5 = numbers1/numbers2
print(result5)
print("---")

result7 = np.sin(numbers1)
print(result7)
print("---")
result8 = np.sqrt(numbers1)
print(result8)
print("---")
result9 = np.log(numbers1)
print(result9)
print("---")
mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)
print(mnumbers1)
print("---")
print(mnumbers2)
print("---")

result10 = np.vstack((mnumbers1,mnumbers2))

print(result10)
print("---")

result11 = np.hstack((mnumbers1,mnumbers2))
print(result11)
print("---")

result12 = numbers1 >5
print(result12)
print("-"*40)

result13 = numbers1%2==0
print(numbers1[result13])

print("---")
print(result13)
print("---")
#%%
import numpy as np


result = np.array([10,15,30,45,60])

result =np.arange(1,15)

result = np.arange(50,100,5)

result = np.zeros(10)

result = np.ones(10)

result = np.linspace(10,100,5)

result = np.random.randint(10,30,5)

result = np.random.randn(5)
#
matris = np.random.randint(10,50,15).reshape(3,5)
#
rewTotal = matris.sum(axis=1)#sutun
colTotal = matris.sum(axis=0)#satır
print("---")
print(rewTotal)
print(colTotal)
print("---")

print(matris)

result=matris.max()
result =matris.min()
result = matris.mean()
result = matris.argmax()
result = matris.argmin()

print("---")
arr =np.arange(10,20)

result = arr[0:3]
result =arr[::-1]

result = matris[0]
result = matris[1,2]

print("---")
print(matris)
print("---")

result = matris[:,0]#0.sutun tamamı
result = matris**2

ciftler = matris[matris%2==0]
result = ciftler[ciftler>0]
print(arr)
print()
print(result)
























     
 
      
 