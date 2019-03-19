# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:05:37 2019

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
kelime2=[]
for i in range(0,len(kelime)):
    kelime2.append(kelime[i])
    kelime2.append(i+1)
print(kelime2)


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
bulunansesliharfler=[]
miktar=[]
for i in range(0,len(kelime)):
    if (kelime[i] in sesliharfler):
        bulunansesliharfler.append(kelime[i])
print(bulunansesliharfler)
#kelime
#eie
for i in sesliharfler:
    sayac=0
    for j in bulunansesliharfler:
        if (i==j):
            sayac+=1
    miktar.append(sayac)
print(miktar)
print(len(miktar))

print("Sadece bulunanlar:\n")
for i in range(0,len(miktar)):
    if (miktar[i]!=0):
        print(sesliharfler[i],"-->",miktar[i])
print("Tüm Değerler:\n")
for i in range(0,len(miktar)):
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
#Yenme Durumları
#2-1
#1-3
#3-2

import random
kullanıcıskor=0
pcskor=0
while True:
    seçim=int(input("Seçiminiz: 1-Taş, 2-Kağıt, 3-Makas :\n"))
    pc=random.randint(1,3)
    if (seçim==pc):
        print("Berabere kaldınız.")
    elif ((seçim==2 and pc==1) or (seçim==1 and pc==3) or (seçim==3 and pc==2)):
        print("Bilgisayarın kararı:",pc)
        print("Tebrikler yendiniz")
        kullanıcıskor+=1
    elif ((seçim==1 and pc==2) or (seçim==3 and pc==1) or (seçim==2 and pc==3)):
        print("Bilgisayarın kararı:",pc)
        print("Üzgünüm yenildiniz")
        pcskor+=1
    else:
        print("Hatalı seçim")
    print("Skorlar: \nKullanıcı->",kullanıcıskor," PC->",pcskor)
    if (kullanıcıskor==3 or pcskor==3):
        break
    
if (kullanıcıskor>pcskor):
    print("Oyun Sona Erdi...TEBRİKLER Yendiniz!")
else:
    print("Oyun Sona Erdi...YENİLDİNİZ!")


"""
Adam Asmaca Oyunu
Kelimeler arasından rastgele seçim yapılacak
Kullanıcı kelimelerin harflerini bulmaya çalışacak
"""


#6 harfli kelimeler listesi oluşturalım
import random
kelimeler=["BEYKOZ","KLAVYE","KELİME","PEYNİR","MATKAP","KOLTUK","GÖZLÜK","PYTHON","ANKARA","YALOVA"]
print("Kelime sayısı:",len(kelimeler))
rastgele=kelimeler[random.randint(0,9)]
print(rastgele)
kelime=list(rastgele)
print(type(kelime))
hak=3
#Kullanıcının 8 yanlış yapma hakkı var
while True:
    kontrol=False
    harf=input("Tahmini Harfiniz:")
    for i in range(0,len(rastgele)):
        if(rastgele[i]==harf):
            kontrol=True
            print(i,".değer=",harf)
            kelime[i]="-"
    if (kontrol==False):
        hak-=1


"""        
    KOLTUK
    K
    -OLTU-
    --LTU-
    ---TU-
    ----U-
    ------
"""


    durum=True
    for i in kelime:
        if (i!="-"):
            durum=False
            break
    if(hak==0 or durum==True):
        break
if (durum==True):
    print("Tebrikler. Bildiniz.Kelime=",rastgele)
else:
    print("Bilemediniz.Kelime=",rastgele)


#Versiyon 2
#6 harfli kelimeler listesi oluşturalım
import random
kelimeler=["BEYKOZ","KLAVYE","KELİME","PEYNİR","MATKAP","KOLTUK","GÖZLÜK","PYTHON","ANKARA","YALOVA"]
print("Kelime sayısı:",len(kelimeler))
rastgele=kelimeler[random.randint(0,9)]
print(rastgele)
kelime=["_","_","_","_","_","_"]
print(type(kelime))
hak=3
#Kullanıcının 8 yanlış yapma hakkı var
while True:
    kontrol=False
    harf=input("Tahmini Harfiniz:")
    for i in range(0,len(rastgele)):
        if(rastgele[i]==harf):
            kontrol=True
            print(i,".değer=",harf)
            kelime[i]=rastgele[i]
    print(kelime)
    if (kontrol==False):
        hak-=1
        """
    KOLTUK
    K
    -OLTU-
    --LTU-
    ---TU-
    ----U-
    ------
    """
    durum=True
    for i in range(0,len(kelime)):
        if (kelime[i]!=rastgele[i]):
            durum=False
            break
    if(hak==0 or durum==True):
        break
if (durum):
    print("Tebrikler. Bildiniz.Kelime=",rastgele)
else:
    print("Bilemediniz.Kelime=",rastgele)
            






