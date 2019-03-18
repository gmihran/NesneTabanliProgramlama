# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:03:18 2019

@author: gozdemihranaltinsoy

"""

#Bu bir açıklama satırıdır
"""
Bu bir açıklama bloğudur
"""
print("Merhaba Dünya")
a=10
isim="Gözde"
ondalıklısayı=10.5
"""
sayı=int(input("Bir sayı girin:"))
o_sayı=float(input("Sayı:"))
sayı=eval(input("Sayı:"))

isim=input("İsminiz:")
print("Merhaba",isim)

sayı=eval(input("Sayı:"))
kare=sayı*sayı
print("Karesi:",kare)
print("Karesi:%d"%kare)
küp=sayı*sayı*sayı
print("Sayı:%d Karesi:%d Küpü:%d"%(sayı,kare,küp))
print("Sayı:%f Karesi:%f Küpü:%f"%(sayı,kare,küp))
print("Sayı:%0.2f Karesi:%0.2f Küpü:%0.2f"%(sayı,kare,küp))
print("Sayı  :%10.1f\nKaresi:%10.1f\nKüpü  :%10.1f"%(sayı,kare,küp))

sayı=eval(input("Sayı:"))
if(sayı>0):
    print(sayı)
    print("Sayı pozitif")
elif(sayı<0):
    print(sayı)
    print("Sayı negatif")
else:
    print(sayı)
    print("Sayı sıfır")

if(sayı%2==0):
    print("Sayı çift")
else:
    print("Sayı tek")

if(sayı==0):
    print("Sayı sıfır ve çift")
elif(sayı>0 and sayı%2==0):
    print("Sayı pozitif ve çift")
elif(sayı>0):
    print("Sayı pozitif ve tek")
elif(sayı%2==0):
    print("Sayı negatif ve çift")
else:
    print("Sayı negatif ve tek")
if(sayı>0 and (sayı%2==0 or sayı%3==0)):
    print(sayı)
"""

#Klavyeden metre cinsinden girilen uzunluğu
#seçilen birime dönüştüren program
#Seçenekler: 1-mm 2-cm 3-dm 4-km ?
#mm=1000*uzunluk
#cm=100*uzunluk
#dm=10*uzunluk
#km=uzunluk/1000
"""
uzunluk=eval(input("Uzunluk:"))
print("1-mm 2-cm 3-dm 4-km")
seçim=eval(input("Seçiminiz:"))
if(seçim==1):
    print(uzunluk*1000,"mm")
elif(seçim==2):
    print(uzunluk*100,"cm")
elif(seçim==3):
    print(uzunluk*10,"dm")
elif(seçim==4):
    sonuç=uzunluk/1000
    print(int(sonuç),"km")
else:
    print("Hatalı seçim")
"""
#İdeal kiloyu hesaplayan program
#Beden kütle indeksi: kilo/((boy*boy)/10000)

#Boy(cm) ve cinsiyet klavyeden girilecek
#Kadın: Yöntem1 --> 45.5+2.3*(boy/2.54-60)
#Erkek: Yöntem1 --> 50+2.3*(boy/2.54-60)
#Yaş klavyeden girilecek
#Kadın: Yöntem2 --> (boy-100+yaş/10)*0.8
#Erkek: Yöntem2 --> (boy-100+yaş/10)*0.9
boy=eval(input("Boy:"))
cinsiyet=input("Cinsiyet:")
cinsiyet=cinsiyet.upper()
#upper --> bütün karakterleri büyük harfe dönüştürür
#lower --> bütün karakterleri küçük harfe dönüştürür
yaş=eval(input("Yaş:"))
if(cinsiyet=="KADIN" or cinsiyet=="K"):
    idealkilo=45.5+2.3*(boy/2.54-60)
    idealkilo2=(boy-100+yaş/10)*0.8
    print(idealkilo,"\n",idealkilo2)
elif(cinsiyet=="ERKEK" or cinsiyet=="E"):
    idealkilo=50+2.3*(boy/2.54-60)
    idealkilo2=(boy-100+yaş/10)*0.9
    print(idealkilo,"\n",idealkilo2)
else:
    print("Hatalı Giriş")





