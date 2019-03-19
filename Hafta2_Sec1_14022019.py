# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 09:08:27 2019

@author: gozdemihranaltinsoy
"""

x=input("sayı:")
print(x[::-1])

# Girilen sayıyı tersten yazdıran program

sayı=eval(input("Sayı:"))
while(sayı>0):
    print(sayı%10,end="")
    #end="" ifadesi değerleri yanyana yazdırdı
    sayı=int(sayı/10)

#Girilen sayının tam sayı olup olmadığını yazdıralım

sayı=eval(input("Sayı:"))
sayı2=int(sayı)
if(sayı==sayı2):
    print("Sayı tamsayıdır.")
else:
    print("Sayı tamsayı değildir.")

#1'den 100'e kadar olan sayılardan 
#tek olanları ekrana yazdıralım

sayı=1
while(sayı<=100):
    if(sayı%2==1):
        print(sayı)
    sayı=sayı+1


print(*range(1,100,2))

#Girilen 2 sayının birbirine bölünüp
#bölünmediğini veren program

s1=eval(input("Sayı:"))
s2=eval(input("Sayı:"))
if (s2>s1):
    x=s1
    s1=s2
    s2=x
    #Yer değiştirme
if(s1%s2==0):
    print("TAM BÖLÜNÜR")
else:
    print("TAM BÖLÜNMEZ")

#Girilen bir sayının tam bölenlerini
#ekrana yazdıran program

sayı=eval(input("Sayı:"))
sayı=int(sayı)
bol=1
while(sayı+1!=bol):
    if(sayı%bol==0):
        print(bol)
    bol=bol+1
    
#2.çözüm yolu
    
sayı=eval(input("Sayı:"))
sayı=int(sayı)
for bol in range(1,sayı+1):
    if(sayı%bol==0):
        print(bol)

#Bir sayının mükemmel sayı olup olmadığını
#bulan program
#Mükemmel sayı: Kendisi dışında
#kendisine tam bölünen sayıların toplamı
#kendisine eşit olan sayılar
#Mükemmel sayı ör: 6, 28, 496, 8128

sayı=eval(input("Sayı:"))
sayı=int(sayı)
toplam=0
for bol in range(1,sayı):
    #sayının kendisi dahil değildir.
    if(sayı%bol==0):
        print(bol)
        toplam=toplam+bol
if(toplam==sayı):
    print("Sayı mükemmel bir sayıdır")
else:
    print("Sayı mükemmel bir sayı değildir")

#Kullanıcıdan alınan 4 kenar bilgisine
#göre şeklin dikdörtgen, kare veya
#diğer dörtgen olduğunu söylesin

a=input("1.kenar:")
b=input("2.kenar:")
c=input("3.kenar:")
d=input("4.kenar:")
if(a==b==c==d):
    print("Şekil karedir.")
#elif((a==b and c==d) or (a==c and b==d) or (a==d and b==c)):
elif(a==b!=c==d or a==c!=b==d or a==d!=b==c):
    print("Şekil dikdörtgendir.")
else:
    print("Şekil yamuktur.")

#Çarpım tablosu
"""
    1*1=1
    1*2=2
    1*3=3
    ...
    1*10=10
    2*1=2
    2*2=4
    ...
    ...
    10*10=100
"""

for i in range(1,11):
    for j in range(1,11):
        #print("{}*{}={}".format(i,j,i*j))
        print(i,"*",j,"=",i*j)


#Girilen ismin harflerini alt alta yazdıran program
isim=input("ismi giriniz:")
for i in isim:
    print(i)
print(isim[0]) #İlk harfi yazdırır
print(isim.upper())
büyükharf=isim.upper()
küçükharf=isim.lower()
ilkharfibüyük=isim.capitalize()
tersinedönüştür=isim.swapcase()
kelimeilkharfbüyüt=isim.title()
print(isim.islower())
#isim değişkeni küçük harflerden mi oluşuyor
print(isim.isupper())
#isim değişkeni büyük harflerden mi oluşuyor
print(isim.istitle())
#isim değişkendeki kelimelerin ilk harfleri
#büyük harflerden mi oluşuyor
print(isim.isspace())
#isim değişkeni boşluklardan mı oluşuyor kontrolü
print(isim)
print(isim.find("a"))
#verilen karakterin kaçıncı karakterde olduğunu verir
#sadece ilk bulduğunun indisini döndürür
#olmadığı takdirde -1 döndürür
print(isim.replace("a","e"))
#isim değişkeninde a değerinin yerine e değerini getirir
print(isim.replace("a",""))
#isim değişkeninde a değerinin yerine boş karakter getirir
#dolaylı yoldan silmiş oluruz

print(len(isim))
#isim değişkenin tuttuğu değerin karakter sayısını verir

#Girilen bir kelimede tüm "a" harflerinin kaçıncı
#karakter olduğunu veren program
for i in range(0,len(isim)):
    #print(isim[i])
    if(isim[i]=="a"):
        print(i+1)
        #i indisi döndürür, i+1 karakterin kaçıncı
        #karakter olduğunu verir

print(isim.rfind("a"))
#aramaya son karakterden başlar
#sağdan sola doğru arama yapar

soyadı=input("Soyadı:")
print(isim,soyadı)

print("*".join(isim))
#her harften sonra boşluk karakteri ekler

#Ödev-1
#Kelimenin Palindrom olup olmadığını bulan program
#kelimenin tersten okunuşu kendisiyle aynı mı?
#ör kayak, ey edip adanada pide ye, kek
