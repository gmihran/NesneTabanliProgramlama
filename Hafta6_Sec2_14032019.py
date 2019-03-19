# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:15:22 2019

@author: gozdemihranaltinsoy
"""

isim=input("İsminizi giriniz:")
#Girilen ismin 2. karakterinden 5. karakterine kadar 
#ekrana çıktısını veren kodu yazınız.
print(isim[1:5])

#Girilen ismin içinde a harfi var mı diye 
#kontrolünü gerçekleştiren kodu yazınız
#kelimenin tüm harflerini kontrol edelim:
for i in isim:
    if (i=="a" or i=="A"): 
        print("A harfi var")
    else:
        print("A harfi yok")
#Girilen ismin içinde a harfi var mı diye 
#kontrolünü gerçekleştiren kodu yazınız
#kelimenin tamamını kontrol edelim: (Çıktı 1 kere oluşur)
print("Kelime Kontrol")
kontrol=0
for i in isim:
    if (i=="a" or i=="A"): 
        kontrol=1
if (kontrol==1):
    print("A harfi var")
else:
    print("A harfi yok")
    
#Girilen ismin içinde a harfinin kaçıncı sıralarda olduğunun
#ve a harfinin miktarının çıktısını verecek olan program
sayac=0
for i in range(0,len(isim)) :
#son değer:len(isim) değerinin 1 eksiği
    if (isim[i]=="a" or isim[i]=="A"):
        print(i+1)
        sayac+=1
print("Miktarı:",sayac)    
        
#Girilen iki sayının birbirine tam bölünüp bölünemediğinin
#çıktısını veren kodu yazınız
#Mod alma : % işareti ile kontrol edilir
#Eğer mod sonucu 0 ise tam bölünebilir
sayı1=int(input("1.sayı:"))
sayı2=int(input("2.sayı:"))
if (sayı1%sayı2==0 or sayı2%sayı1==0):
    print("Tam bölünebilir")
else:
    print("Tam bölünemez")

#Klavyeden girinin para miktarını banknotlara ayıran programı 
#yazınız. 200,100,50,20,10,5,1
para=int(input("Para tutarını giriniz:"))
sayac=0
while(para>=200):
    sayac+=1
    para-=200
print("200 banknot:",sayac)
sayac=0
while(para>=100):
    sayac+=1
    para-=100
print("100 banknot:",sayac)
sayac=0
while(para>=50):
    sayac+=1
    para-=50
print("50 banknot:",sayac)
sayac=0
while(para>=20):
    sayac+=1
    para-=20
print("20 banknot:",sayac)
sayac=0
while(para>=10):
    sayac+=1
    para-=10
print("10 banknot:",sayac)
sayac=0
while(para>=5):
    sayac+=1
    para-=5
print("5 banknot:",sayac)
print("1 banknot:",para)



#Girilen günün haftanın kaçıncı günü olduğunu veren program
#Ör/ Kullanıcı Pazartesi girdiğinde 1,
#ÖR/ Kullanıcı Pazar girdiğinde 7 çıktısını verecek
günler={"Pazartesi":1,"Salı":2,"Çarşamba":3,"Perşembe":4,"Cuma":5,"Cumartesi":6,"Pazar":7}
gün=input("Günü giriniz:").title()
print(gün)
print(günler[gün])

#Verilen hece sayısı kadar random bir kelime oluşturacak
#Ör/ Kullanıcı 5 girerse; pumaya
#Ör/ Kullanıcı 3 girerse; leke
sesliharfler=["a","e","ı","i","o","ö","u","ü"] 
#Sesli harf miktarı:8
sessizharfler=["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","y","z"]
#Sessiz harf miktarı:18

miktar=int(input("Hece sayısını giriniz:"))
kelime=[]
for i in range(0,miktar):
    import random
    rndSessiz=sessizharfler[random.randint(0,17)]
    kelime.append(rndSessiz)
    rndSesli=sesliharfler[random.randint(0,7)]
    kelime.append(rndSesli)
print(kelime)
