# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 14:50:31 2021

@author: ali_d
"""

#Os Modul

import os
import datetime

result = dir(os)
print(result)

print()

result= os.name
print(result)

#%% dizin değistirme
#os.chdir("C:\\")
#os.chdir("../..)
#%% klasor olusturma
# result= os.getcwd() = etkın dızı ogrenme
#os.makedirs("newdirectory/yeniklasor")
#os.rename("newdirectory", "yeni") #ad degıstırme
#os.mkdir("newdirectory")
#os.rmdir("newdirectory")
#os.removedirs("yeniklasor/yenıklasor")
print(result)

#%% Listeleme
#result = os.listdir()
result = os.listdir("C:\\")
print(result)
# for dosya in os.listdir():
#     if dosya.endswith("py"):
#         print(dosya)

#%%

# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)#olusturulma tarıhı
# result = datetime.datetime.fromtimestamp(result.st_atime)#son erısılme tarıhı
# result = datetime.datetime.fromtimestamp(result.st_mtime)#degıstırılme tarıhı


#os.system("notepad.exe")
print(result)
#%%Path

result = os.path.abspath("_os.py")
result = os.path.dirname("C:\_os.py")
result = os.path.dirname(os.path.abspath("C:\_os.py"))
result = os.path.exists("_os.py") #false doner bu konumda oyle bır dosya yok cunku
print(result)

result = os.path.isdir("C:\_os.py")
result = os.path.isfile("C:\_os.py")
print(result)
#%%








        



























































