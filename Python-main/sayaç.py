sesli_harfler = 'aeiioöuü'
sayaç = 0
def kelime_sor():
    return input('Bir kelime girin: ')
def seslidir(harf):
    return harf in sesli_harfler
def artir(sayaç, kelime):
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç
def ekrana_bas(kelime):
    mesaj = "{} kelimesinde {} sesli harf var."
    print(mesaj.format(kelime, artir(sayaç, kelime)))
def çalistir():
    kelime = kelime_sor()
    ekrana_bas(kelime)
if __name__ == '__main__':
    çalistir()
