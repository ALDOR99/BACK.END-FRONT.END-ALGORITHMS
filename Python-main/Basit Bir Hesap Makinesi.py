isim=input("Lütfen isminizi giriniz efendim: ")
giriş="""
    Hesap makinasına hoş geldiniz bay {}
(1) topla
(2) çıkar
(3) çarp
(4) böl
""".format(isim)
print(giriş)
soru = input("Yapmak istediğiniz işlemin numarasını girin: ")
if soru =="1":
    sayı1=int(input("Toplama işlemi için ilk sayı değerini girin: "))
    sayı2=int(input("Toplama işlemi için ikinci sayı değerini girin: "))
    print(sayı1 ,"+",sayı2,"=",sayı1+sayı2)
elif soru =="2":
    sayı3=int(input("Çıkarma işlemi için ilk sayıyı girin: "))
    sayı4=int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
    print(sayı3,"-",sayı4,"=",sayı3-sayı4)
elif soru =="3":
    sayı5=int(input("Çarpma işlemi için ilk sayıyı giriniz: "))
    sayı6=int(input("Çarpma işlemi için ikinci sayıyı giriniz: "))
    print(sayı5,"x",sayı6,"=",sayı5*sayı6)
elif soru=="4":
    sayı7=int(input("Bölme işlemi için ilk sayıyı giriniz: "))
    sayı8=int(input("Bölme işlemi için ikinci sayıyı giriniz: "))
    print(sayı7,"/",sayı8,"=",sayı7/sayı8)
elif soru=="5":
    sayı9=int(input("hangi sayının karesini almak istersiniz: "))
    print(sayı9,"sayısının karesi = ",sayı9**2) # sayının karesını aldık
elif soru=="6":
    sayı10=int(input("Karekökünü hesaplamak istediğiniz sayıyı giriniz: "))
    print(sayı10,"sayısının karekökü= ",sayı10**0.5)
    
else:
    print("yanlış hesaplama fonksiyonu gırdınız")
    print("Aşağıdaki seçeneklerden birini giriniz:",giriş)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    