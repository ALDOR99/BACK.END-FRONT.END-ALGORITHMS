# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 17:28:58 2021

@author: ali_d
"""

#Re Modul
import re 

result = dir(re)
#regular expression

str = "Hello world | location Worl "

result=re.findall("Hello",str)
result = len(result)
print(result)


#%% re.split()
result = re.split(" ",str) #her bır bosluk karakterınden bolunmus olur
result = re.split("R",str)
print(result)#liste sklınde getırılır

#%% re.sub()

result = re.sub(" ","-", str) #butun bosluk karakterlerını cızgı ıle degıstırır
result = re.sub("\s","-", str) #aynı sonucu alırım
print(result)

#%% re.search()

result = re.search("Hello",str)
#result = result.span()
#result = result.start()
#result = result.end()
#result = result.group()
#result = result.sring
print(result)


#%% 
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

#%% Metacharacters
#[]
txt = "The rain in Spain"
x = re.findall("[a-m]",txt)
print(x)

#%% 

txt = "That will be 59 dollars"


x = re.findall("\d", txt)
print(x)

#%% .

txt = "hello world"

x = re.findall("he..o", txt)
print(x)

#%% ^

txt = "hello world"

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
  
print()

txt2 = "hello world"

x = re.findall("^hello",txt2)
if x:
    print("yes")
    
else:
    print("no")

#%% $

txt = "hello world"

x = re.findall("world$",txt)

if x:
    print("Yes, the string ends with 'world'")
else:
    print("no match")

#%%

txt = "hello world hey man"

x = re.findall("world$",txt)

if x:
    print("Yes, the string ends with 'world'")
else:
    print("no match")
#%% *
txt = "the rain in Spain falls mainly in the plain"
x = re.findall("aix*",txt)
print(x)

if x:
    print("yes there is at least one match!")
else:
    print("No match")

#%% +

txt = "the rain in Spain falls mainly in the plain!"

x = re.findall("aix+",txt)
print(x)
if x:
    print("Yes there is at least one match")
else:
    print("no match")
#%% {}	
txt = "The rain in Spain falls mainly in the plain!"

x = re.findall("al{2}", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
#%% | Either or


txt = "The rain in Spain falls mainly in the plain!"

x =re.findall("falls|stays",txt)
print(x)
if x:
    print("yes there is at least one match!")
else:
    print("no match")

#%% Special Sequences
#\A
txt = "The rain in Spain"

x = re.findall("\AThe",txt)
print(x)

if x:
    print("Yes there is a match")
else:
    print("No match")
    

#%% \b
txt = "The rain in Spain"


x = re.findall(r"\ba", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

txt = "The rain in Spain"
x = re.findall(r"\bT",txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#%% 

txt = "The rain in Spain"


x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#%% \B sonunda
txt = "The rain in Spain"


x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#%% 

txt = "The rain in Spain"


x = re.findall(r"ain\B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#%%

txt = "The rain in Spain"
x = re.findall("\d",txt)
print(x)
if x:
    print("yes,there is at least one match")
else:
    print("No match")
    
#%% \D

txt = "The rain in Spain"
x = re.findall("\D",txt)
print(x)
if x:
    print("yes,there is at least one match")
else:
    print("No match")
    
#%% \s 

txt = "The rain in Spain"

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#%% \S

txt = "The rain in Spain"


x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#%% \w

txt = "The World of Game"
x = re.findall("\w",txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#%% \W

txt = "The rain in Spain"


x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#%% \Z


txt = "The rain in Spain"


x = re.findall("Spain\Z", txt)
print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")


    
  


  




  



























































    
    






















