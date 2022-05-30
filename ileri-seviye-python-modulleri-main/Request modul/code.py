# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:37:31 2021

@author: ali_d
"""

import json
# print(json.__file__)
import requests


result = requests.get("https://jsonplaceholder.typicode.com/todos")

result= json.loads(result.text)
 #print(result)
#

print(result[0]["title"])
print(result[0])
print(type(result))
#print(result)
print()

for i in result:
    if i["userId"]==1:
        print(i["title"])
    #print(i["title"])

print(type(result))

print("-"*20)

#%%

x = requests.get("https://w3schools.com/python/demopage.htm")
print(x.text)

#%% Methods
# delete(url, args)
#Python Requests delete() Method

x = requests.delete('https://w3schools.com/python/demopage.php')
print(x.text)

#%% 
x = requests.delete('https://w3schools.com/python/demopage.php')

#print the response text (the content of the requested file):
print(x.text)

#%% 
url = 'https://w3schools.com/python/demopage.php'

#Sometimes the server redirects a request, could be if the file does not exist etc., set the 'allow_redirects' parameter to False to deny redirects:

x = requests.delete(url, allow_redirects=False)

#print the response text (the content of the requested file):
print(x.text)

#%% Exchange Api



import requests
import json

Api_url = "https://api.exchangeratesapi.io/latest?base="

bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alınan döviz türü: ")

miktar =int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

result = requests.get(Api_url+bozulan_doviz)

result = json.loads(result.text)
#print(result)

print("1 {0}={1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz],alinan_doviz))

print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar*result["rates"][alinan_doviz][alinan_doviz]))














































































