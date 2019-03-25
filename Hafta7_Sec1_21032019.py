# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:30:21 2019

@author: gozdemihranaltinsoy
"""
print("3'e ve 7'ye tam bölünenler:")
#1 ile 100 arasında sadece 3'e ve 7'ye tam bölünenleri ekrana yazdıralım
#listeye aktararak liste boyutunu ekrana yazdıralım
liste=[] #liste tanımlandı
for i in range(1,101): #1 ile 100 arasındaki sayılar. 
#Son değerin 1 fazlası yazılır
    if(i%3==0 and i%7==0):
        print(i)
        liste.append(i) #i değerini listeye ekler.
print("Sayıların miktarı:",len(liste))
print("Sayıların toplamı:",sum(liste),"\n")

print("5'e veya 8'e tam bölünenler:")
#1 ile 100 arasında 5'e veya 8'e tam bölünenleri ekrana yazdıralım
#sayaç ile bu değerlerin miktarını bulalım
sayac=0
toplam=0
for i in range(1,101):
    if(i%5==0 or i%8==0):
        print(i)  
        sayac+=1
        toplam+=i
print("Sayıların miktarı:",sayac)
print("Sayıların toplamı:",toplam,"\n")
    
#Pop örneği; örnek w3schools platformundan alındı.
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1) #1.indisteki değeri siler
print(fruits,"\n")

#Çarpım tablosu
#aralarda tab boşluğu var
#1*1=1    2*1=2    3*1=3    4*1=4    5*1=5
#1*2=2    2*2=4......................5*2=10
#..........................................
#1*10=10 2*10=20   3*10=30  4*10=40  5*10=50            

ders="Nesne Tabanlı Programlama"
#ders isimli değişkendeki "Tabanlı" metnini 
#ekrana yazdırmak için gerekli olan kod satırını yazınız
print(ders[6:13]) #son karakter:13-1=12.indis

#ders isimli değişkendeki Programlama metninden Pgmm 
#ekrana yazdırmak için gerekli olan kod satırını yazınız
print(ders[14::3])

#ders isimli değişkenin tuttuğu değeri tersten yazdıralım
print(ders[::-1])

#ders isimli değişkendeki "Nesne" metnini 
#ekrana yazdırmak için gerekli olan kod satırını yazınız
print(ders[0:5:])

#ders isimli değişkenin tuttuğu değerin içinde geçen
#a harflerinin indis değerini ekrana yazdıralım ve 
#listede tutup en sonunda listeyi de yazdıralım
#sayac mantığı ile çözüm:
sayac=0
liste=[]
for i in ders:
    if (i=="A" or i=="a"):
        liste.append(sayac)
        print("İndis değeri=",sayac)
    sayac+=1
print(liste)
print(type(i)) #str
print(type(sayac)) #int
print(type(liste)) #list
#range ile çözüm:
liste2=[] #boş bir liste2 isimli list tanımladık
for i in range(0,len(ders)): #a int 
    if ders[i]=="a" or ders[i]=='A':
        print("İndis değeri:",i)
        liste2.append(i)
print(liste2)

sehir="İstanbul"
#sehir[0]="I" #bu kod satırı hatalıdır
#nedeni; str objeleri herhangi bir karakterleri değiştirilemez
sehir="Istanbul"

sayi="104567"
print(sayi[2])

liste=list("Gözde")
print(liste)
liste[1]="o"
print(liste)



    