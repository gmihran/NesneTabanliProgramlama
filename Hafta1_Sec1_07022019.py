# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:30:00 2019
7 Şubat 2019 09:00 - 13:00
@author: gozdemihranaltinsoy
"""

"""
print("Merhaba")
a=10
print("a=",a)

değişken=float(input("değişken="))
kare=değişken*değişken
print("Karesi:",kare,kare,"Karesi:",kare)
print("Karesi:",kare)

değişken2=int(input("değişken2="))
kare2=değişken2*değişken2
print("Karesi:",kare2)

isim=input("İsminiz:")
print("Merhaba ",isim)

ondalıklısayı=eval(input("Sayı:"))
print(ondalıklısayı*2)
isim=eval(input("İsim:"))
print(isim*2)

a=10.2545678
print("%d"%a) #Bu ekrana yazdırırken integer olarak yazdırır
#Yani değişkenin tipini değiştirmez
b=int(a) #Değişkenin tipini(türünü) integer yapar
print(a)
c=255.6545478
d=2125.241548
print("%10.2f"%a)
print("%10.2f"%b)
print("%10.2f"%c)
print("%10.2f"%d)
print("Değerleri yan yana yazdıralım:")
print(a,b,c,d)
print("Değerleri alt alta yazdıralım:")
print(a,"\n",b,"\n",c,"\n",d)
print("%d\n%d\n%d\n%d\n"%(a,b,c,d))

sayı=eval(input("Sayı:"))
if (sayı>0):
    print(sayı)
    print("Sayı pozitif")
elif (sayı<0):
    print(sayı)
    print("Sayı negatif")
else:
    print(sayı)
    print("Sayı sıfır")
if(sayı%2==0):
    print("Sayı çifttir")
else:
    print("Sayı tektir")

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
uzunluk=int(input("Uzunluk(m):"))
print("1-mm 2-cm 3-dm 4-km :?")
seçim=int(input("Seçiminiz:"))
if(seçim==1):
    print(uzunluk*1000,"mm")
elif(seçim==2):
    print(uzunluk*100,"cm")
elif(seçim==3):
    print(uzunluk*10,"dm")
elif(seçim==4):
    print(uzunluk/1000,"km")
else:
    print("Hatalı seçim")
"""

"""
cinsiyet=input("Cinsiyet:")
cinsiyet=cinsiyet.upper() 
#upper --> Metni büyük harfe dönüştürür
#lower --> Metni küçük harfe dönüştürür
if (cinsiyet=="K" or cinsiyet=="KADIN"):
    print("Kadın")
else:
    print("Erkek")
"""
#İdeal kiloyu hesaplayan program
#Beden kütle indeksi: kilo/((boy*boy)/10000)

#Boy(cm) ve cinsiyet klavyeden girilecek
#Kadın: Yöntem1 --> 45.5+2.3*(boy/2.54-60)
#Erkek: Yöntem1 --> 50+2.3*(boy/2.54-60)
#Yaş klavyeden girilecek
#Kadın: Yöntem2 --> (boy-100+yaş/10)*0.8
#Erkek: Yöntem2 --> (boy-100+yaş/10)*0.9
"""
boy=eval(input("Boyunuz:"))
cinsiyet=input("Cinsiyet:")
cinsiyet=cinsiyet.upper(); 
#Girilen cinsiyet değeri büyük harfe dönüştü
yaş=eval(input("Yaşınız:"))
if(cinsiyet=="KADIN" or cinsiyet=="K"):
    idealkilo=45.5+2.3*(boy/2.54-60)
    idealkilo2=(boy-100+yaş/10)*0.8
else:
    idealkilo=50+2.3*(boy/2.54-60)
    idealkilo2=(boy-100+yaş/10)*0.9
print("ideal kilonuz:",idealkilo)
print("İdeal kilo:",idealkilo2)
kilo=eval(input("Kilo:"))
print("Vücut kitle indeksi:",kilo/((boy*boy)/10000))
"""
"""
Ödev-1:
Klavyeden girilen pozitif tamsayıyı tersten
yazdıran program
ipucu : sayının mod 10'u alınabilir
1234
4321
"""
sayı=1234
print(sayı%10)
print(int(sayı/10))
"""
Ödev-2:
Klavyeden girilen sayının tamsayı olup
olmadığını bulan program
ipucu : sayıyı tamsayıya dönüştürüp kendisine
eşit mi diye karşılaştırmak 
"""
