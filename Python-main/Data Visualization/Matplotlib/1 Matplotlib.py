import matplotlib.pyplot as plt
import numpy as np

#-----ornek 1-------

x = [1,2,3,4,5,6]
#x ekseni degerleri
y=[1,4,9,16,25,36]
# y ekseni degerleri
plt.plot(x,y,"o--r")
# x, y plot et cızgılı ve nokta koy
plt.axis([0,10,0,50])
#axis uzunlukları

plt.title("Grafik Başlığı")
#burası baslıgım
plt.xlabel("x label")
#x eksenı baslıgı
plt.ylabel("y label")
#y eksenı baslıgı
plt.show()
#plt goster


#%% ornek 2

x = np.linspace(0,2,100)
#0 ile 2 arasında 100 tane değer olusturduk

plt.plot(x,x,label="linear",color="red")
#aldıgımız x degerıne gore linear bir grafık
plt.plot(x,x**2,label="quadratic",color="yellow")
#xin karesine gore bir grafık
plt.plot(x,x**3,label="cubic",color="green")
#xin küpüne gore bır grafık

plt.xlabel("x label")
#x etiket ısmım
plt.ylabel("y label")
#y etıket ısmım
plt.title("simple plot")
#baslıgım
plt.legend()
#labelerımı gostermesı ıcın 
plt.show()
#plotumu acması ıcın

#%%

yıl = [2011,2012,2013,2014,2015]
#yıl bilgimiz
oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]
#oyuncuların yıllara gore atıgı gol bılgılerı

plt.plot([],[],color = "y",label="oyuncu1")

plt.plot([],[],color = "r",label="oyuncu2")

plt.plot([],[],color = "b",label="oyuncu3")


plt.stackplot(yıl,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])
plt.title("yıllara gore atılan goller")
plt.xlabel("yıl")
plt.ylabel("gol sayısı")
plt.legend()
plt.show()

#%%
urun = "appale mac book pro","msi gamming","asus gamming"

fiyat = [19000,16000,15000]
colors = ["y","r","b"]

plt.pie(fiyat,labels=urun,colors=colors,shadow=(True),explode=(0.05,0.05,0.05))
plt.show()











































