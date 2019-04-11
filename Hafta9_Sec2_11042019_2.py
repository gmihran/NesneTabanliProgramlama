# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:09:39 2019

@author: gozdemihranaltinsoy
"""

#iki sayının bölümünün sonucunu döndüren fonksiyon
def bolum():
    return 10/2

#kendisine gelen değeri geri döndüren lambda
a=lambda s:s

#kendisine gelen değerlerin bölümünü döndüren lambda
b=lambda a,b:int(a/b)

#kendisine gelen 2 tane sayının birbirine bölümünden kalanını veren lambda
kalan=lambda x,y:x%y

#kendisini gelen sayının 2 katını geri döndüren lambda
ikikati=lambda x:2*x

#kendisini gelen sayının karesini geri döndüren lambda
kare=lambda a:pow(a,2)

#kendisini gelen sayının, kendisine gelen üssünü geri döndüren lambda
us=lambda a,b:pow(a,b)

#kendisine gönderilen listeden en büyük sayıyı döndüren lambda
mak=lambda liste:max(liste)

#kendisine gönderilen listeden sayıların toplamlarını döndüren lambda
toplam=lambda liste:sum(liste)

#kendisine gönderilen metni tersten yazdıran lambda
ters=lambda isim:isim[::-1]

#kendisine gönderilen metnin 5. ve 6. harflerini ekrana yazdıran lambda
p=lambda isim:isim[4:6]

#Kendisine gelen sayının tek veya çift olduğunu döndüren lambda
tekçift=lambda sayi:sayi%2==0

#Kendisine gelen değer 2'den küçükse 1 değerini, değilse 5 değerini döndüren lambda
x = lambda y: 1 if y < 2 else 5

#Kendisine gelen sayının tek veya çift olduğunun sonucunu yazdıran lambda
tç=lambda a: print("çift") if a%2==0 else print("tek")

#Kendisine gönderilen sayıların tek veya çift olduğunu ekrana yazdıran lambda
tç2=lambda i: print(i,":çift") if i%2==0 else print(i,":tek")

#Kendisine gönderilen 5 adet sayının toplamını döndüren lambda
t=lambda a,b,c,d,e:a+b+c+d+e

#Kendisine gönderilen isimleri Z'den A'ya sıralayan lambda
sirala=lambda isimler:sorted(isimler,reverse=True)

#Kendisine gönderilen isimleri A'dan Z'ye sıralayan lambda
sirala2=lambda isimler:sorted(isimler)

#kendisine gönderilen listedeki isimlerin karakter sayısına bakarak kısa kelimeden uzun kelimeye doğru sıralayan fonksiyon
def ksirala():
    #Soru mimarı: Doğukan Dombaycı
    yeniliste=list()
    isimler=["Aslı","Doğukan","Akın","Zeynep","Süleyman","Kaan","Sezer","Beyza","Ada"]
    uzunluk=[]
    for i in isimler:
        uzunluk.append(len(i))
    print(uzunluk)
    #Çözüm mimarı: Okan Kukul
    for i in range(1,max(uzunluk)+1):
        for j in range(0,len(isimler)):
            if (len(isimler[j])==i):
                yeniliste.append(isimler[j])
    print(yeniliste)

    """
    #Değerleri ekrana yazdıralım
    for i in range(0,len(isimler)):
        print(isimler[i])
    #Değerleri ekrana yazdıralım
    for i in isimler:
        print(i)
    """
def main():
    print("Bolum:",bolum())
    print(b(10,3))
    print(a(2))
    k=kalan(10,3)
    print(k)
    print(ikikati(5))
    print(kare(6))
    print(us(5,3))
    liste=[5,10,20,15,30,78,40]
    print("Mak:",mak(liste))
    print("Toplam:",toplam(liste))
    print(ters("Beykoz"))
    print(p("Beykoz"))
    #sayi=int(input("sayı:"))
    sayi=10
    if tekçift(sayi):
        print("Sayı çifttir")
    else:
        print("Sayı tektir")
    print(x(2))
    tç(5)
    for i in range(1,10):
        tç2(i)
    print("T:",t(1,2,3,4,5))
    isimler=["Aslı","Akın","Zeynep","Kaan","Sezer","Beyza"]
    print(sirala(isimler))
    print(sirala2(isimler))
    ksirala()
main()
