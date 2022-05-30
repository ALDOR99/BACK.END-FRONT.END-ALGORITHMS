# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:13:53 2021

@author: ali_d
"""
#Hızlı Başlangıc 3

import numpy as np
import pandas as pd





#Append
#Bir dataframe’e satır ekleme


df = pd.DataFrame(np.random.randn(8,4),
                  columns=["A","B","C","D"])
print(df)

s = df.iloc[3]

a = (df.append(s,ignore_index=True))

b = (df.append(s,ignore_index=False))


#%% Gruplama


df = pd.DataFrame({
    "A":["foo","bar","foo","bar",
         "two","two","one","three"],
    
    "B":["one","one","two","three",
         "two","two","one","three"],
    
    "C":np.random.randn(8),
    
    "D":np.random.randn(8)
    })

print(df)
print("-"*30)
print(df.groupby("A").sum())
print()
print(df.groupby("B").sum())
print()

print(df.groupby(["A","B"]).sum())
print()
#%% Yeniden Şekillendirme
#Stack

tuples = list(zip(*[["bar","bar","baz","baz",
                     "foo","foo","qux","gux"],
                    ["one","two","one","two",
                     "one","two","one","two"]]))


index = pd.MultiIndex.from_tuples(tuples,names = ["first",
                                                 "second"])
df1 =pd.DataFrame(np.random.randn(8,2),index=index,
                  columns=["A","B"])


print(df1)
print()
df2 = df1[:4]
print(df2)
print("-"*30)

Stack =df2.stack()
print(Stack)
print()

print(Stack.unstack())
#good
print()

print(Stack.unstack(1))
print()


print(Stack.unstack(0))


#%% Pivot Tabloları


ex = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})
 

print(ex)

print()

ex1 = pd.pivot_table(ex, values='D', index=['A', 'B'], columns=['C'])

print(ex1)


#%% Zaman serisi

rng = pd.date_range("1/1/2012",
                    periods=100,freq="S")

ts = pd.Series(np.random.randint(0, 500, len(rng)),
               index=rng)

print(ts.resample("5Min").sum())

#%%


rng1= pd.date_range("1/1/2021",
                    periods=50,freq="S")

print()

rng2 = pd.date_range("1/1/2021",
                     periods=50,freq="A")
#years

rng3 = pd.date_range("1/1/2021",periods=50,freq="C")


rng4 = pd.date_range("3/6/2021 00:00",
                     periods=5,freq="D")


print(rng4)

ts1 = pd.Series(np.random.randn(len(rng)), rng)

#%%

df = pd.DataFrame(
    {"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']
     })





df["grade"] = df["raw_grade"].astype("category")

print(df)


print(df["grade"])



df["grade"].cat.categories = ["very good", "good", "very bad"]

print(df)



print()

df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])

print(df)

#Plotting

ts = pd.Series(np.random.randn(1000), 
               index=pd.date_range('1/1/2000',
                                   periods=1000))

ts = ts.cumsum()

print(ts.plot())

#%%























