# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:05:07 2021

@author: ali_d
"""
# Youtube İstatistik Verilerinin Analizi
import pandas as pd

data = pd.read_csv("DEvideos.csv")

#ilk 10 kaydı getirelim
a1 = data.head(10)
print("----")

#şimdi 2. 5 kaydı getirelim
a2=data[5:10].head(5)
print(a2)
print("----")

a3 = data.columns
print(a3)
# video_id = video kimliği
#trending date = trend tarihi
#title = başlık
#channel title = kanal başlığı
#category_id = kategori kimliği
#publish time = yayınlama tarihi
#tags = etiketler
#views = izlenme,görüntülenme
#likes = beğeni
#dislikes = (hoşnutsuzluk)
#comment count = yorum sayısı
#thumbnail link =*******
#comments disabled = Yorumlar devre dışı
#ratings disabled = engeli puanlar
#video error or removed = video hatası veya kaldırıldı
#description = açıklama

("----")
#toplam columns sayısı
print(len(data.columns))
print("---------------")

#şimdi bir kaç kolon silelim ve kolonları listeliyelim

#data.drop(['thumbnail_link','comments_disabled','comments_disabled','video_error_or_removed','description'],axis=1,inplace=True)
a4 = data.drop(["thumbnail_link","comments_disabled","comments_disabled","video_error_or_removed","description"],axis=1)
#burda kayıt etıgımde none deger donduruyor

#beğenme ve beğenmeme sayılarının ortalamasını bulalım

print(data["likes"].mean())
# bu like ortalaması

print(data["dislikes"].mean())
#buda dislike(beğenmeme) ortalamamız

print("-"*30)
# il 50 videonun like ve dislike kolonlarını getirelim
a5 = data.head(50)[["title","likes","dislikes"]]
print(a5)
print("-"*30)

#en çok görüntülenen video bilgisini alalım
a6 =data[data["views"].max()==data["views"]][["title","views"]]
print(a6)

print("-"*30)

#şimdide en düşük görüntülenmeye sahip videoya bakalım
a7 = data[data["views"].min()==data["views"]][["title","views"]]
print(a7)

print("-"*30)

#en fazla goruntulenen ilk 10 video

a8 = data.sort_values("views",ascending=False).head(10)[["title","views"]]
print(a8)

print("-"*30)
#kategoriye göre beğeni ortalamalarını sıralı şekilde getirelim şimdi

a9 = data.groupby("category_id").mean().sort_values("likes")["likes"]
print(a9)
print("-"*30)

#kategorıye gore yorum sayılarını yukardan asagı sıralıyalım

a10 = data.groupby("category_id").sum().sort_values("comment_count",ascending = False)["comment_count"]
print(a10)
print("-"*30)

#Her kategoride kaç video vardır 

a11 = data["category_id"].value_counts()
print(a11)
print("-"*30)

#her vıdeonun title isimlerının uzunlugunu yenı bır kolomda gosterelım
data["title_len"] = data["title"].apply(len)
print(data)

print("-"*30)

#her vıdeo ıcın kullanılan tag sayısını yenı kolonda gosterelim
# data["tag_count"]=data["tags"].apply(lambda x: len(x.split("|")))
# print(data)

#

def tagCount(tag):
    return len(tag.split("|"))
data["tag_count"] = data["tags"].apply(tagCount)
print(data)

print("-"*30)

#en populer videoları listeleyiniz(like/dislike oranına gore)

def likedislikeoranhesapla(dataset):
    likeList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])
    
    liste=list(zip(likeList,dislikesList))
    
    oranListesi = []
    
    for like,dislike in liste:
        
        if (like + dislike) ==0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))
    return oranListesi

likedislikeoranhesapla(data)

data["beğeni_oranı"] =likedislikeoranhesapla(data)

a13=(data.sort_values("beğeni_oranı",ascending=False)[["title","likes","dislikes","beğeni_oranı"]])
print(a13)


print("-"*40)

print(data.info())







































































