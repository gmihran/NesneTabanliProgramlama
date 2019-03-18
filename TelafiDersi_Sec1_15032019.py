# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:00:02 2019

Section 1 Telafi Dersi

@author: gozdemihranaltinsoy
"""

#Girilen ismin 2. karakterinden 5. karakterine kadar 
#ekrana çıktısını veren kodu yazınız.
isim=input("İsim giriniz:")
print(isim[1:5])
#İlk karakterinden 4. karakterine kadar
print(isim[:4]) #4'ün bir eksiğine kadar gider

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
print("Kontrol:")
kontrol=0
for i in isim:
  if (i=="a" or i=="A"):
    kontrol=1
if (kontrol):
   print("A harfi var")
else:
   print("A harfi yok")
    
#Girilen ismin içinde a harfinin kaçıncı sıralarda olduğunun
#ve a harfinin miktarının çıktısını verecek olan program
sayaç=0
for i in range(len(isim)):
  if (isim[i]=="a" or isim[i]=="A"):
    print(i+1)
    sayaç+=1
print("Miktarı:",sayaç)

#Girilen iki sayının birbirine tam bölünüp bölünemediğinin
#çıktısını veren kodu yazınız
#Mod alma : % işareti ile kontrol edilir
#Eğer mod sonucu 0 ise tam bölünebilir
sayi1=int(input("1.sayı:"))
sayi2=int(input("2.sayı:"))
if (sayi1%sayi2==0 or sayi2%sayi1==0):
  print("Tam bölünebilir")
else:
  print("Tam bölünemez")

#Klavyeden girinin para miktarını banknotlara ayıran programı 
#yazınız. 200,100,50,20,10,5,1
ilkpara=int(input("Para tutarı:"))
para=ilkpara
banknot=0
while(para>=200):
  banknot+=1
  para-=200
print("200 banknot:",banknot)
banknot=0
while(para>=100):
  banknot+=1
  para-=100
print("100 banknot:",banknot)
banknot=0
while(para>=50):
  banknot+=1
  para-=50
print("50 banknot:",banknot)
banknot=0
while(para>=20):
  banknot+=1
  para-=20
print("20 banknot:",banknot)
banknot=0
while(para>=10):
  banknot+=1
  para-=10
print("10 banknot:",banknot)
banknot=0
while(para>=5):
  banknot+=1
  para-=5
print("5 banknot:",banknot)
print("1 banknot",para)

print("Diğer çözüm:")
#Diğer çözüm:
#ilkpara paramızın miktarını tutuyor
para=ilkpara
banknot=0
if (para>=200):
  banknot=int(para/200)
  para%=200
print("200 banknot:",banknot)
banknot=0
if (para>=100):
  banknot=int(para/100)
  para%=100
print("100 banknot:",banknot)
banknot=0
if (para>=50):
  banknot=int(para/50)
  para%=50
print("50 banknot:",banknot)
banknot=0
if (para>=20):
  banknot=int(para/20)
  para%=20
print("20 banknot:",banknot)
banknot=0
if (para>=10):
  banknot=int(para/10)
  para%=10
print("10 banknot:",banknot)
banknot=0
if (para>=5):
  banknot=int(para/5)
  para%=5
print("5 banknot:",banknot)
print("1 banknot:",para)
  
#Girilen günün haftanın kaçıncı günü olduğunu veren program
#Ör/ Kullanıcı Pazartesi girdiğinde 1,
#ÖR/ Kullanıcı Pazar girdiğinde 7 çıktısını verecek
#sözlük yapısını kullanıyoruz:
#farklı çözümlerde kullanılabilir

günler={"Pazartesi":1,"Salı":2,"Çarşamba":3,"Perşembe":4,"Cuma":5,"Cumartesi":6,"Pazar":7}
gün=input("Gün:").title()
#title girilen kelimenin baş harfini büyük harf, diğer harflerini küçük harf yapar
print(günler[gün],".gün")


#Verilen hece sayısı kadar random bir kelime oluşturacak
#Ör/ Kullanıcı 3 girerse; pumaya
#Ör/ Kullanıcı 2 girerse; leke

sesli=["a","e","ı","i","o","ö","u","ü"]
#sesli harf miktarı:8
sessiz=["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","y","z"]
#sessiz harf miktarı:18
randomkelime=[]
rndkelime=""
hece=int(input("Hece:"))
import random
for i in range(hece):
  rndsessiz=random.choice(sessiz)
  randomkelime.append(rndsessiz)
  #diğer yöntem
  #rndsesli=sessiz[random.randint(0,17)]

  rndsesli=random.choice(sesli)
  randomkelime.append(rndsesli)
  #diğer yöntem:
  #rndsesli=sesli[random.randint(0,7)]

  #diğer yöntem:
  rndkelime=rndkelime+rndsessiz+rndsesli
print(randomkelime)
print(rndkelime)
