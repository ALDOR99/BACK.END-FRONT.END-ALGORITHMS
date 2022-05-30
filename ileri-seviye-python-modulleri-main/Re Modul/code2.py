# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:03:22 2021

@author: ali_d
"""
import re

#Code 2
# Sets

#[arn]

# Dize herhangi bir A, R veya N karakterlerine sahip olup olmadığını kontrol edin:
txt = "The rain in Turkey"

x = re.findall("[arn]",txt)
print(x)

if x:
    print("Yes, there is at least one match")
else:
    print("No match")
#%%
txt2 = "hey man how are you"

x = re.findall("[e]",txt)
print(x)
if x:
    print("yes")
else:
    print("no")
#%% [a-n]

txt = "The rain in Turkey"
x=re.findall("[a-n]",txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#%%  [^arn]
    
txt = "The rain in Spain"

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#%% [0123]

txt = "Hello man how are you"
x=re.findall("[0123]",txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#%% [0-9]

txt = "8 times before 11:45 AM"
x = re.findall("[0-9]",txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#%% [0-5][0-9]

txt = "8 times before 11:45 AM"

x = re.findall("[0-5][0-9]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#%% [a-zA-Z]

txt = "8 times before 11:45 AM"

x = re.findall("[a-zA-Z]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#%% +

txt = "8 times before 11:45 AM"

x = re.findall("[+]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#%% The findall() Function

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)



txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
#%% The search() Function

txt = "The rain ,in Spain"
x=re.search("\s",txt)
print("The first white-space character is located in position:", x.start())
print()
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
print()
txt = "The rain in Portugal"
x = re.search("Portugal", txt)
print(x)
#%% The split() Function

txt = "Hi man how are you"
x = re.split("\s",txt)
print(x)

#%% 
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)

#%% The sub() Function

txt = "The rain in Turkey"
x = re.sub("\s","9",txt)
print(x)
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
#%% Match Object
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

















