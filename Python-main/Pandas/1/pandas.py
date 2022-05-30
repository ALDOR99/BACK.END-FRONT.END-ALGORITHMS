# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 17:40:53 2021

@author: ali_d
"""

#Pandas
import pandas as pd
import numpy as np

#data
numbers = [20,30,40,50]
print("----")
leters = ["a","b","c","d",40]

pandas_pd = pd.Series(numbers)

pandas_pd1 = pd.Series(leters)

print(pandas_pd)
print(type(pandas_pd))

print(pandas_pd1)

scalers = 5

print(pd.Series(scalers))
print("---")
pandas_series1 = pd.Series(numbers,["a","b","c","d"])
print(pandas_series1)
print("---")
dict = {"a":15,"b":25,"c":35,"d":45}
pandas_series2 = pd.Series(dict)
print(pandas_series2)
print("---")

a = np.random.randint(10,100,5)

pandas_series3 = pd.Series(a)
print(pandas_series3)
print("---")
pandas_series3 = pd.Series(a,["a","b","c","d","e"])
print(pandas_series3)
print("---")
pandas_series4 = pd.Series([20,30,40,50],["a","b","c","d"])
print(pandas_series4[0])
print(pandas_series4["a"])
print(pandas_series4[:2])
print(pandas_series4[-2])
print(pandas_series4["a"])

print(pandas_series4["d"])
print(pandas_series4["a"])
#
print(pandas_series4.ndim) #1boyutlu  liste oldugunu soyluyor

print(pandas_series4.dtype)#type

print(pandas_series4.shape)

print(pandas_series4.sum())

print(pandas_series4.max())#max

print(pandas_series4.min())#min

print(pandas_series4+pandas_series4)

print(pandas_series4+1000)
print("---")
print(pandas_series4>35)
print("---")
result = pandas_series4 % 2 ==0
print(result)
print("---")
print(pandas_series4[pandas_series4 %2 ==0])
print(pandas_series4[pandas_series4 %2 ==1])
print("---")

opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([20,80,40,20,None],["astra","corsa","mokka","insignia","Grandland"])

total = opel2018+opel2019
print(total)
#%% Pandas dataFrame
import pandas as pd

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples=s1,oranges = s2)
print(data)
print("---")

df=pd.DataFrame(data)
print(df)
print("-------")
# "
# df1= pd.DateFrame()
# print(df1)
# "

df1 = pd.DataFrame([1,2,3,4,5])
print(df1)
print("---")

df2 = pd.DataFrame([["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]],columns = ["Name","Grade"],index=[1,2,3,4])
print(df2)
#columns = sütünlar
print("---")
dict1 = {"Name":["Ahmet","Ali","Yağmur","Çınar"],
         "Grade":[50,60,70,80]
         }
#Grade =sınıf
pd4= pd.DataFrame(dict1)

print(pd4)



liste = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
##
dict1 = {"Name":["Ahmet","Ali","Yağmur","Çınar"],
         "Grade":[50,60,70,80]}
         
a1 = (pd.DataFrame(dict1,index=["212","232","236","456"]))

dict_list=[
           {"Name":"Ahmet","Grade":50},
           {"Name":"Alis","Grade":60},
           {"Name":"Uğurcan","Grade":70},
           {"Name":"Hasan","Grade":80},
           {"Name":"Miray","Grade":90}
           ]

a2 = pd.DataFrame(dict_list)

#%% Pandas  ile DataFrame calısma
import pandas as pd
import numpy as np

a=np.random.randn(3,3)

df = pd.DataFrame(a,index=["A","B","C"],columns=["Column1","Column2","Column3"])
print(df)
result = df
print("---")
print(result["Column1"])
print("---")
print(type(result["Column1"]))
print("---")

result = df[["Column1","Column2"]]
print(result)
print("---")
result1 = df.loc["A"]
print(result1)
print("---")
result2 = type(df.loc["A"])
print(result2)
print("---")
result3 = df.loc[:]
print(result3)
print("---")
result4 = df.loc[:,["Column1","Column2"]]
print(result4)
print("---")
result5 = df.loc[:,["Column1","Column3"]]
print(result5)
print("---")

result6 = df.loc["A":"B","Column2"]
print(result6)
print("---")

a=df.iloc[1]
print(a)

print("---1")

b =df.iloc[2]
print(b)
print("---2")

c=df.iloc[0]
print(c)
print("---3")
#%% fitlreleme

data = np.random.randint(10,100,75).reshape(15,5)


dfx = pd.DataFrame(data,columns=["Columns1","Columns2","Columns3","Columns4","Columns5"])

print(dfx)
print("---")

df = dfx.columns
print(df)
print("---")

df = dfx.head()
print(df)

print("---")

df =dfx.head(10)
print(df)

print("---")

df =dfx.tail()
print(df)

print("---")

df = dfx.tail(10)
print(df)

print("---")

df =dfx["Columns1"].head()
print(df)

print("---")

df=dfx.Columns1.head()
print(df)

print("---")

df = dfx[["Columns1","Columns2"]].head()
print(df)

print("----")

df = dfx[["Columns1","Columns2"]].tail()
print(df)

print("---")

#df = dfx[5:15] 5 -15 arasındakılerı alırım

df = dfx[5:15][["Columns1","Columns2"]].head()
print(df)

print("---")
df = dfx[5:15][["Columns1","Columns2"]].tail()
print(df)
print("---"*10)

df = dfx > 50 
print(df)

print("----")

df = dfx[dfx > 50]
print(df)

print("---")

df = dfx[dfx % 2 == 0]
print(df)
print("---")

df = dfx[df["Columns1"] > 50]
print(df)

print("---")

df = dfx[df["Columns1"] > 50][["Columns1","Columns2"]]
print(df)

print("---")

#df = dfx.query("Columns1 >= 10 & Columns1 % 2 == 1")
#df = dfx.query("Columns1 >= 10 & Columns1 % 2 == 1")[["Columns1","Columns2"]]
#(df)

#Query = Sorgu

#%% DataFrame GroupBy
import pandas as pd
import numpy as np

peronel = {"Çalışan":["Ahmet Yılmaz","Can Ertük","Hasan Korkmaz","Cenk Saymaz","Rıza Ertürk","Mustafa Can","Aslı Demir"],
           "Departman":["İnsan kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","Bilgi İşlem"],
           "Yaş":[30,25,45,50,23,34,42],
           "Semt":["KadıKöy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","KadıKöy"],
           "Maaş":[5000,3000,4000,3500,2750,6500,4500]}

df = pd.DataFrame(peronel)
print(df)

print("---")

result = df["Maaş"].sum()
print(result)

print("---")

result1 = df.groupby("Departman")
print(result1)

print("---")

result2 = df.groupby("Departman").groups
print(result2)

print("---")

result3 = df.groupby(["Departman","Semt"]).groups
print(result3)
print()
print("---")
                      
semtler = df.groupby("Semt")

for name,group in semtler:
    print(name)
    print(group)
    print()

print("---")
print()

for name,group in df.groupby("Departman"):
    print(name)
    print(group)
    print()
print("--------------")
print()

xv = df.groupby("Semt").get_group("KadıKöy")
print(xv)
print("--------------")

xv1 = df.groupby("Departman").get_group("Muhasebe")
print(xv1)
print("---------------")

xv2 = df.groupby("Departman").sum()
print(xv2)

print("---------------")

xv3 = df.groupby("Departman").mean()
print(xv3)
print("--------------")

xv4 = df.groupby("Departman")["Maaş"].mean()
print(xv4)
print("--------------")
xv5 = df.groupby("Semt")["Çalışan"].count()
print(xv5)

print("-------------")

xv6 = df.groupby("Departman")["Yaş"].max()
print(xv6)

print("-------------")


xv7 = df.groupby("Departman")["Maaş"].max()["Muhasebe"]
print(xv7)

print("-------------")

xv8 = df.groupby("Departman").agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]
print(xv8)

#%% Pandas ile Kayıp ve Bozuk Veri Analizi
import pandas as pd
import numpy as np 

data = np.random.randint(20,200,15).reshape(5,3)
print(data)

df = pd.DataFrame(data,index = ["a","c","e","f","h"], columns = ["Column1","Column2","Column3"])
print(df)
print("---")
df = df.reindex(["a","b","c","d","e","f","g","h"])
print(df)
print("---")
newColumn =[np.nan,30,np.nan,51,np.nan,30,np.nan,10]

df["Column4"]=newColumn




result =df
result=df.drop("Column1",axis =1)
print("---")

result=df.drop(["Column1","Column2"],axis =1)
print("---")

result = df.drop("a",axis=0)
print("---")

result = df.drop(["a","b","c"],axis=0)
print("---")

result = df.isnull()
print(result)
print("---")

result = df.notnull()
print(result)
print("---")

result = df.isnull().sum()
print(result)
print("---")

result = df["Column1"].isnull().sum()
print(result)
print()
result =df["Column2"].isnull().sum()
print(result)
print("---")

result = df[df["Column1"].isnull()]
print(result)
print("---")
result = df[df["Column1"].isnull()]["Column1"]
print(result)
print("---")

result = df[df["Column1"].notnull()]["Column1"]
print(result)
print("---")
print()

result = df.dropna()
print(result)

print("---")
print(df)
print("---")

result = df.dropna(axis = 1)
print(result)
print("---")

result = df.dropna(how="any")
print(result)
print("---")

result = df.dropna(how="all")
print(result)
print("---")

result = df.dropna(subset=["Column1","Column2"],how="all")
print(result)

print("----")

result = df.dropna(subset=["Column1","Column2"],how="all")
print(result)
print("---")

result = df.dropna(thresh=2)
print(result)
print("---")

result = df.dropna(thresh=4)
print(result)
print("----")

result = df.fillna(value = "no input")
print(result)
print("---")

result = df.fillna(value = 1)
print(result)
print("---")

result = df.sum().sum()
print(result)
print("---")

result = df.size
print(result)
print("---")

result = df.isnull().sum()
print(result)
print("---")

result = df.isnull().sum().sum()
print(result)
print("----")
##############

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet
result = df.fillna(value = ortalama(df))

print(result)

##############

#%% Pandas ile String Fonksiyonlar
import pandas as pd


customers = {
        "CostomerId":[1,2,3,4],
        "firstName":["Ahmet","Ali","Hasan","Can"],
        "lastName":["Yılmaz","Korkmaz","Çelik","Toprak"],
    }

orders = {
    "OrderId":[10,11,12,13],
    "CustomerId":[1,2,5,7],
    "OrderDate":["2010-07-04","2010-08-04","2010-07-07","2012-07-04"],
    }
df_customers = pd.DataFrame(customers,columns=["CostomerId","firstName","lastName"])
df_orders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])


result = pd.merge(left_on = df_customers,right_on= df_orders, how="inner")

#Merge = Birleştirmek
#%%

customersA = {
        "CostomerId":[1,2,3,4],
        "firstName":["Ahmet","Ali","Hasan","Can"],
        "lastName":["Yılmaz","Korkmaz","Çelik","Toprak"]
    }

ordersB = {
    "OrderId":[10,11,12,13],
    "FirstName":["Yağmur","Çınar","Cengiz","Can"],
    "LastName":["Bilge","Turan","Yılmaz","Turan"]
    }
df_customersA = pd.DataFrame(customersA,columns=["CostomerId","firstName","lastName"])
df_ordersB = pd.DataFrame(ordersB,columns=["OrderId","CustomerId","OrderDate"])

result = pd.concat([df_customersA,df_ordersB])
print(result)
#%%
np.random.seed(0)
left = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': np.random.randn(4)})    
right = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': np.random.randn(4)})


#%% Pandas ile DataFrame  Metotları

import pandas as pd
import numpy as np

data = {
        "Column1":[1,2,3,4,5],
        "Column2":[10,20,13,45,25],
        "Column3":["abc","bca","ade","cba","dea"]
        
        }
df = pd.DataFrame(data)

print(df)
print("--------------------")

result = df["Column2"].unique()
print(result)
print("----")

result = df["Column2"].nunique()
print(result)
print("----")

result = df["Column2"].value_counts()
print(result)
print("---")

result = df["Column1"]*2
print(result)
print("-----")

# def kareal(x):
#     return x*x
kareal = lambda x: x*2

result = df["Column1"].apply(kareal)
print(result)
print("---")

result = df["Column3"].apply(len)
print(result)
print("---")


df["Column4"] = df["Column3"].apply(len)
print(df)
print("---")

print(df)
print(df.columns)
print("---")
print(len(df.columns))
print("---")
print(len(df.index))
print()
print(df.info)
print("----")

result = df.sort_values("Column2")
print(result)
print("---")

result = df.sort_values("Column3")
print(result)
print("---")

result = df.sort_values ("Column3",ascending=False) #yukardan asaga
print(result)
print("----")

data =  {"Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
         "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap"],
         "Gelir":[10,20,22,32,54,66]
         }
df = pd.DataFrame(data)
print(df)
print("---")

df = df.pivot_table(index = "Ay",columns="Kategori",values="Gelir")
print(df)
#%% NBA veri
import pandas as pd
import numpy as np

data =pd.read_csv("Players.csv")

df = data.head(10)
print(df)
print("----")

df = len(data.index)
print(df)
print("---")
#oyuncuların  boy ortalaması
df=data["height"].mean()
print(df)
print("---")

#oyuncuların min boy degerı
df = data["height"].min()
print(df)
print("----")

#oyuncuların max boy değeri
df = data["height"].max()
print(df)
print("----")
print(data.columns)
print("----")
df = data[data["height"]==data["height"].max()]
print(df)

print("----")

df = data[data["height"]==data["height"].min()]
print(df)

print("---")

df1= data[data["weight"]==data["weight"].min()]
print(df1)

df2 =data[data["weight"]==data["weight"].max()]
print(df2)
print("---")

df3 = data[(data["height"]>=160) & (data["height"]<=170)]
print(df3)
print("----")


df4=data[data["Player"]== "Keith Jennings"]['birth_city']
df4=data[data["Player"]== "Keith Jennings"]['birth_state']
print(df4)
print("----")

df5 = data.groupby("birth_city").mean()["height"]
print(df5)
print("----")
df6 = len(data.groupby("born"))
print(df6)
print("----")

df7 = data["birth_state"].nunique()
print(df7)
print("-----")

df9 = data["born"].value_counts()
print("----")

def str_find(name):
    if "Zlin" in name:
        return True
    return False

# df10 = data[data["birth_city"].apply(str_find)]
# print(df10)
# print("----")

















