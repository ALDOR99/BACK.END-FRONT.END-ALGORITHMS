import time
import random
import sys
class Oyuncu():
    def __init__(self, isim, can=5, enerji=100):
        self.isim = isim
        self.darbe = 0
        self.can = can
        self.enerji = enerji
    def mevcut_durumu_görüntüle(self):
        print('darbe: ', self.darbe)
        print('can: ', self.can)
        print('enerji: ', self.enerji)
    def saldir(self, rakip):
        print('Bir saldiri gerçeklestirdiniz.')
        print('Saldiri sürüyor. Bekleyiniz.')
        for i in range(10):
            time.sleep(.3)
            print('.', end='', flush=True)
        sonuç = self.saldiri_sonucunu_hesapla()
        if sonuç == 0:
            print('\nSONUÇ: kazanan taraf yok')
        if sonuç == 1:
            print('\nSONUÇ: rakibinizi darbelediniz')
            self.darbele(rakip)
        if sonuç == 2:
            print('\nSONUÇ: rakibinizden darbe aldiniz')
            self.darbele(self)
    def saldiri_sonucunu_hesapla(self):
        return random.randint(0, 2)
    def kaç(self):
        print('Kaçiliyor...')
        for i in range(10):
            time.sleep(.3)
            print('\n', flush=True)
            print('Rakibiniz sizi yakaladi')
    def darbele(self, darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji -= 1
        if (darbelenen.darbe % 5) == 0:
            darbelenen.can -= 1
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print('Oyunu {} kazandi!'.format(self.isim))
            self.oyundan_çik()
    def oyundan_çik(self):
        print('Çikiliyor...')
sys.exit()
##################################
# Oyuncular
siz = Oyuncu('Ahmet')
rakip = Oyuncu('Mehmet')
# Oyun baslangici
while True:
    print('Su anda rakibinizle karsi karsiyasiniz.',
          'Yapmak istediginiz hamle: ',
          'Saldir:s',
          'Kaç:k',
          'Çik:q', sep='\n')
    hamle = input('\n> ')
    if hamle == 's':
        siz.saldir(rakip)
        print('Rakibinizin durumu')
        rakip.mevcut_durumu_görüntüle()
        print('Sizin durumunuz')
        siz.mevcut_durumu_görüntüle()
    if hamle == 'k':
        siz.kaç()
    if hamle == 'q':
        siz.oyundan_çik()