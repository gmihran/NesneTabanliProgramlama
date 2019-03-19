# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:17:51 2019

@author: gozdemihranaltinsoy
"""

"""
Klavyeden girilen bir kelimeyi, her harfinden sonra sırasını 
gösteren sayıyı da yanına koyarak tekrar ekrana yazdıran 
programı Python diliyle kodlayınız.
Ör: Beykoz kelimesi klavyeden girildiğinde; 
B1e2y3k4o5z6 şeklinde çıktı verecektir.
"""

kelime=input("Bir kelime giriniz:")
#print(type(kelime))
liste=[]
for i in range(0,len(kelime)):
    liste.append(kelime[i])
    liste.append(i+1)
print(liste)


"""
Klavyeden girilen kelimenin içinde bulunan sesli harflerden 
kaç tane bulunduğunun çıktısını veren programı Python 
diliyle kodlayınız.
Ör: Beykoz Üniversitesi
e->3
i->3
o->1
ü->1

Ör: Bilgisayar
a-->2
i-->2
"""


kelime=input("Bir kelime giriniz:")
sesliharfler=["a","e","ı","i","o","ö","u","ü"]
miktar=[]
liste=[] 
for i in kelime:
    if (i in sesliharfler):
        liste.append(i)
print(liste)
for i in range(0,len(sesliharfler)):
    sayac=0
    for j in range(0,len(liste)):
        if (sesliharfler[i]==liste[j]):
            sayac+=1
    miktar.append(sayac)
print(miktar)
for i in range(0,len(miktar)):
    if (miktar[i]!=0):
        print(sesliharfler[i],"-->",miktar[i])

"""
Taş - Kağıt - Makas Oyunu
Bilgisayar taş, kağıt ve makas değerlerinden 
birini random olarak seçecek (metin veya sayı 
ile tutabilirsiniz). Oyun aşağıda belirtmiş 
olduğum kurallara göre gerçekleşecek. 

Taş-kâğıt-makas, genellikle iki oyuncuyla ve 
üç durumdan birinin seçilmesiyle oynanan bir 
el oyunudur. Taş makası, makas kağıdı, kâğıt da 
taşı yener. Eğer oyuncular aynı durumu seçerse 
oyun berabere biter. 

Kazanma
Taş, makası kırarak yener.
Kağıt, taşı sararak yener.
Makas, kağıdı keserek yener.

Belirlenen skora ilk ulaşan oyunu kazanır. İstenirse tek seferli oyunlar da oynanabilir.

Hak ve skor planlamasını da dilediğiniz gibi yapabilirsiniz.

Açıklama: Python'da random sayı üretmek için;

import random #random sınıfını projenize 
dahil eder

sayı=random.randint(1,3) #1 ile 3 arasında 
random bir sayı üretip bu sayıyı sayı değişkenine 
atar.
"""
#Yenme durumları
#1-2
#3-1
#2-3

import random
pcskor=0
kullanıcıskor=0

while True:#(kullanıcıskor<3 and pcskor<3):
    kullanıcı=int(input("1-Kağıt 2-Taş 3-Makas Seçiminiz:\n"))
    
    pc=random.randint(1,3)
    print("Bilgisayar Seçimi:",pc)
    if (kullanıcı==pc):
        print("Berabere kaldınız")
    elif ((kullanıcı==1 and pc==2) or (kullanıcı==3 and pc==1) or (kullanıcı==2 and pc==3)):
        print("Tebrikler. Kazandınız.")
        kullanıcıskor+=1
    elif ((kullanıcı==2 and pc==1) or (kullanıcı==1 and pc==3) or (kullanıcı==3 and pc==2)):
        print("Üzgünüm. Yenildiniz.")
        pcskor+=1
    else:
        print("Hatalı seçim")
    print("Skor durumu: \n Pc-->",pcskor," Kullanıcı skor-->",kullanıcıskor)    
    if (kullanıcıskor==3 or pcskor==3):
        break
if (kullanıcıskor>pcskor):
    print("Oyun Bitti! Tebrikler yendiniz...")
else:
    print("Oyun Bitti! Yenildiniz...")



"""
Adam Asmaca Oyunu
Kelimeler arasından rastgele seçim yapılacak
Kullanıcı kelimelerin harflerini bulmaya çalışacak
"""

#6 harfli kelimeler listesi oluşturalım
import random
kelimeler=["KİTAP","KALEM","SİLGİ","LİSTE","ÇOCUK","TAHTA","YASİN","KASAP","GÖZDE","FIRIN","EKMEK"]
print(len(kelimeler))
hak=3
liste=["_","_","_","_","_"]
rastgele=kelimeler[random.randint(0,10)] #11 değer var
#rastgele="KİLİT" #deneme
print(rastgele)

while True:
    tahmin=input("Tahmini harfinizi giriniz:")
    durum=False
    for i in range(0,len(rastgele)):  #i değeri indisi tutar
    #for i in rastgele --> i kelimenin harfleri olurdu
        if (tahmin==rastgele[i]):
            liste[i]=tahmin
            durum=True
    if (durum):
        print(liste)
    else:
        hak-=1;
    sonuc=True
    for i in liste:
        if (i=="_"):
            sonuc=False
            break
    if (hak==0 or sonuc==True):
        break
if (sonuc==True):
    print("Bildiniz... Kelime:",rastgele)
else:
    print("Kaybettiniz... Kelime:",rastgele)













