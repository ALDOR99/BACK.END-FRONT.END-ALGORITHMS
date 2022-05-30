name = input("LÜTFEN İSMİNİZİ GİRİNİZ BAYIM: ")
print()
print("MERHABA " + name + " TAHMİNLERİN İÇİN SABIRSIZLANIYORUZ!")

secret_word = "celebrimorg"

guess_string = ""

lives = 10 

while lives > 0:
    character_left = 0 
    for character in secret_word:
        if character in guess_string:
            print(character)
        else:
            print("*")
            character_left += 1
    if character_left == 0:
        print("BU HARİKA KAZANDINIZ!!")
        break
    
    guess = input(f"BAY {name} LÜTFEN HARF VEYA SAYI TAHİMİNDE BULUNUN: ")
    guess_string += guess 

    if guess not in secret_word:
        lives -=1 
        print(f"YANLIŞ TAHMİN ÜZGÜNÜM BAY {name}!")
        print(f" {lives} CANINIZ KADLI ")
    
    if lives == 0:
        print() 

#kodlarınızı yukardaki gibi sublime text editorune yazın ve "adamAsmaca.py"
#olarak kaydedin şimdi daha anlaşılır olması için kodları teker teker 
#inceleyelim.

#name = input("Enter name: ")
#print("Hello " + name + " time to play hangman!")

#secret_word = "Metalica"

#guess_string = ""

#lives = 10

#yukardaki kod satırımızda "name " değişkeniyle kullanıcdan bir isim 
#girmesini istedik ve daha sonra ekrana print fonksiyonu ile üçüncü komut
#satırında olanın aynısını ekrana yazdırdık "secret_word" isimli değişkenimize 
#bullunması gereken kelimeyi yazdık ve en son olarak "guess_string" isimli 
#değişkenimize boş bir string değer ile tanımlayıp lives yanı kullanıcının kalan 
#canını belirten değişkenin 10 olarak belirtik

#while lives > 0:
#    character_left = 0 
#    for character in secret_word:
#        if character in guess_string:
#            print(character)
#        else:
#            print("-")
#            character_left += 1
#    if character_left == 0:
#        print("you won!!")
#        break
    
#    guess = input("guess a word: ")
#    guess_string += guess 

#    if guess not in secret_word:
#        lives -=1 
#        print("wrong!")
#        print(f"You have {lives} left")
    
#    if lives == 0:
#        print() 

#"lives" değişkenini 0 sayısından büyük olduğu sürece devam eden while 
#döngüsü oluşturduk 13.üncü kod bloğunda "character_left" isimli bir değişken 
#tanımlayıp 0a eşitledik "character_left" değişkeni bulunmamış harflerin 
#yerine yazılacak olan "-" karakterinin toplam sayısını beliritr devam edersek 
#15inci kod bloğunda bir for döngüsü oluşturup  başta tanımlamış olduğumuz 
#ve bulunması istenilen kelimenin yani  secret_word değişkeninin üzerinde 
#gezinerek her karakterin character değişkenine aktardık hemen sonrasında 
#gelen if -else  koşulu ile başta boş olarak tanımlamış olduğumuz "gues_string"
#değişkeninin "character" değişkeninde olup olmadığını kontrol ettirdik 

#eğer "guess_string" değişkeninde character değişkeninin elemanı 
#bulunuyorsa ekrana character değişkenini eğer bullunmuyorsa yani else 
#durumunda ise ekrana "-" karakterini yazdırıp character_left değişkenini 1 
#artırdık  character_left değişkenini 1 arttırmamımızın sebi ; character_left
#değişkeninin "-" karakterinin  yani bulunmayan harflerin toplam sayısına eşit 
#olmasını istediğimizdendir bir sonraki yani 24.kod satırına geçersek bir if 
#koşulu daha  oluşturup bu koşulda character_left karakteri 0 a eşit ise 
#yani tüm karakterler bullunmuşsa ekrana "you won " yazdır break komutu 
#ile programı sonlandırılacak eğer if koşula girmez ise daha bulunmamış 
#karakterlerin olduğunu ve bu karakterinde bulunması gerektiği için 
#program devam edecektir .

#şekildeki gibi bir sonuc karşınızıa çıkacaktır bu çıktı henüz harf tahmini 
#yapmadığımız ve guess a word ile tahmin yapacağımız yerdir 
#yapacağımızı harf tahminini "guess" değişkeni (29.kod satırı) ile yapıp başta
#boş olarak belirlediğimiz guess_string değişkenine ekleyeceğiz devamında 
#ise if koşulu ile tahmin ettiğimiz harf eğer secret_word değişkeninde yoksa 
#lives değişkenimizi 1 azaltıp ekrana wrong yazdırıp sonrasında kalan canı 
#ekrana bastıracağız.

#tahmini yanlış ise ekrana olduğu gibi bir sonuç çıkacaktır 
#son olarak yapmış olduğumuz tahmin yanlış ise ve lives değişkenimiz  0 a eşit 
#olursa ekrana you died yazısı çıkacak ve program sonlanacaktır 

#eğer  kod satırlarına dikkat edecek olursanız programın bizden tahmin 
#alırken birden fazla harf girebileceğimizi göreceksiniz bu avantajı kullanark
#tahmin bölümüne büyük küçük tüm harfleri tek seferde yazarsanız program 
#kazandığınızı gösterecktir bu durumu engellemek için girilen tahmin eğer bir 
#karakterden uzun ise girilen tahmin programa dahil etmesini engelleyerek ,
#sorunu çözebilirsiniz.
