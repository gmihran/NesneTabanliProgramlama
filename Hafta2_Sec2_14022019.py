# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:05:35 2019

@author: gozdemihranaltinsoy
"""
"""
# Girilen sayıyı tersten yazdıran program
sayı=eval(input("Sayı:"))
sayı=int(sayı)
while(sayı>0):
    print(sayı%10,end="")
    sayı=int(sayı/10)

"""

"""
sayi=input("Sayi giriniz:")
print(sayi[::-1])
"""
"""
def reverse(text):
    a=""
    for i in range(1, len(text)+1):
        a+=text[len(text)-i]
    return a
    
print(reverse(str(input("Bir sayı girin: "))))
"""

#Girilen sayının tam sayı olup olmadığını yazdıralım
"""
sayı=eval(input("Sayı:"))
sayı2=int(sayı)
if(sayı==sayı2):
    print("Sayı tam sayıdır")
else:
    print("Sayı tam sayı değildir")
"""
#1'den 100'e kadar olan sayılardan 
#tek olanları ekrana yazdıralım
"""
for i in range(1,101):
    if(i%2==1):
        print(i)
"""

#Girilen 2 sayının birbirine bölünüp
#bölünmediğini veren program
"""
s1=eval(input("1.Sayı:"))
s2=eval(input("2.Sayı:"))
if(s2>s1):
    x=s1
    s1=s2
    s2=x
if(s1%s2==0):
    print("Tam bölünebilir")
else:
    print("Tam bölünemez")
"""

#Girilen bir sayının tam bölenlerini
#ekrana yazdıran program
"""
sayı=int(eval(input("Sayı:")))
for i in range(1,sayı+1):
    if(sayı%i==0):
         print(i)
"""
#2.çözüm yolu:
"""
sayı=int(eval(input("Sayı:")))
bolen=1
while(bolen<=sayı):
    if(sayı%bolen==0):
        print(bolen)
    bolen+=1
"""
#Bir sayının mükemmel sayı olup olmadığını
#bulan program
#Mükemmel sayı: Kendisi dışında
#kendisine tam bölünen sayıların toplamı
#kendisine eşit olan sayılar
#Mükemmel sayı ör: 6, 28, 496, 8128
"""
sayı=int(eval(input("Sayı:")))
toplam=0
for i in range(1,sayı):
    if(sayı%i==0):
         toplam+=i
if(sayı==toplam):
    print("Mükemmel sayıdır")
else:
    print("Mükemmel sayı değildir")
"""   
#Kullanıcıdan alınan 4 kenar bilgisine
#göre şeklin dikdörtgen, kare veya
#diğer dörtgen(yamuk) olduğunu söylesin
    #a==b==c==d 
    #(a==b and c==d) or (a==c and b==d) or (a==d and b==c)
"""
a=input("1.kenar:")
b=input("2.kenar:")
c=input("3.kenar:")
d=input("4.kenar:")
if(a==b==c==d):
    print("karedir")
elif(a==b and c==d) or (a==c and b==d) or (a==d and b==c):
#elif(a==b!=c==d) or (a==c!=b==d) or (a==d!=b==c)
    print("Dikdörtgendir")
else:
    print("Yamuktur")
"""
#Çarpım tablosu
"""
1*1=1
1*2=2
1*3=3
....
1*10=10
2*1=2
...
...
10*10=100
"""
"""
for i in range(1,11):
    print("%d'ler Çarpım Tablosu"%i)
    for j in range(1,11):
        print("{}*{}={}".format(i,j,i*j))
        #print("%d*%d=%d"%(i,j,i*j))
    print("--------------------")
"""
#Girilen ismin harflerini alt alta yazdıran program
isim="Gözde"
for i in isim:
    print(i)
print("İlk harf=",isim[0])
print(len(isim))
for i in range(0,len(isim)):
    print("isim[",i,"]=",isim[i])

print(len("Gözde"))
#len metnin uzunluğunu döndürür
print(isim.upper())
#metnin tamamını büyük harfe dönüştürür
print(isim.lower())
#metnin tamamını küçük harfe dönüştürür
isim=isim.upper()
#isim içinde tutulan değer büyük harfe dönüştürüldü
print(isim.capitalize())
#metnin sadece ilk harfini büyük harfe dönüştürür
soyadı="Altınsoy"
adsoyad=isim+" "+soyadı
print(adsoyad.title())
#kelimelerin ilk harfini büyük harfe dönüştürür
print(adsoyad)

tersineçevir=adsoyad.swapcase()
#büyük harfi küçük harfe,
#küçük harfi büyük harfe dönüştürür
print(tersineçevir)
print(adsoyad.islower())
print("gözde".islower())
#metnin tamamı küçük harf mi kontrol eder
#evetse true, hayırsa false döndürür
print("GÖZDE".isupper())
#metnin tamamı büyük harf mi kontrol eder
#evetse true, hayırsa false döndürür
print("Gözde".isupper())
print("Gözde AltınsoY".istitle())
#sadece kelimelerin ilk harfi büyük mü
#diye kontrol eder
#evetse true, hayırsa false döndürür
print("    ".isspace())
#metnin tamamı boşluklardan mı oluşuyor
isim=input("İsim:")
print(isim.find("a"))
#ilk bulduğu "a" değerinin indisini döndürür
print(isim.replace("a","e"))
#a harfinin yerine e harfini getir
print(isim.replace("a",""))

print("istanbul".find("e"))
#karakter yoksa -1 değerini verir

#Girilen bir kelimede tüm "a" harflerinin kaçıncı
#karakter olduğunu veren program
#ankara
#1,4,6
print("a değerinin bulunduğu karakterler")
for i in range(0,len(isim)):
    #if(isim[i].find("a")==0)
    if(isim[i]=="a"):
        print(i+1)
        
print(isim.rfind("a"))
#aramaya son karakterden başlar
#sağdan sola doğru arama yapar

print("*".join(isim))
#her harften sonra boşluk karakteri ekler

#Ödev-1
#Kelimenin Palindrom olup olmadığını bulan program
#kelimenin tersten okunuşu kendisiyle aynı mı?
#ör kayak, ey edip adanada pide ye, kek
