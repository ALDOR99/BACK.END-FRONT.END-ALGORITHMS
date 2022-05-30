# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:51:09 2021

@author: ali_d
"""


from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

#import datetime

result =dir(datetime)
print(result)

#%%
result= datetime.now()
print(result)


#%% 
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.date())
print(now.hour)
print(now.minute)
print(now.second)
#%%

result = datetime.ctime(now)
print(result)

#%%
result = datetime.strftime(now,"%Y")
print(result)
result = datetime.strftime(now,"%X")
print(result)
result = datetime.strftime(now,"%d")
print(result)
result = datetime.strftime(now,"%A")
print(result)
result = datetime.strftime(now,"%B")
print(result)
#
result = datetime.strftime(now,"%Y %B %A")
print(result)

#
#https://docs.python.org/3/library/datetime.html
#

print("-"*30)

t = "21 Nisan 2021"
gun,ay,yıl = t.split()
print(gun)
print(ay)
print(yıl)

#%%

t = "15 April 2019 hour 10:12:30"
print(t)
dt = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")
print(dt)
print()

print(type(t))
print(type(dt))

print()

print(dt.year)
print(dt.month)
print(dt.hour)
print()

#%%

birthday = datetime(1983,5,10,5,30,10)
print(birthday)
print(type(birthday))


result = datetime.timestamp(birthday)
#tarih objesi saniye cinsinden getirilir
print(result)


result = datetime.fromtimestamp(result)
print(result)

print("-"*30)
 
result = datetime.fromtimestamp(0)
print(result)

print("-"*30)

result = now-birthday #timedelta
print(result)

print()


result = result.days
print(result)
print()

result = now + timedelta(days=41)
print(result)


result = now + timedelta(days=790,minutes=10)
print(result)
print()

result = now-timedelta(days=10)
print(result)


#%% 
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
    )
# Only days, seconds, and microseconds remain
print(delta)

print(datetime.timedelta(days=64, seconds=29156, microseconds=10))




























































