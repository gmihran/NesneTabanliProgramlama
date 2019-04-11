# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:10:10 2019

@author: gozdemihranaltinsoy
"""

def toplam():
    a,b=5,2
    return a+b
#kendisine gelen 2 sayının toplamını geri döndüren fonksiyon
def t(s1,s2):
    return s1+s2
#listedeki değerlerden en büyük değeri geri döndüren fonksiyon
def mak():
    liste=[5,10,2,3,20,15]
    return liste,max(liste)
#Girilen değerin karesini ekrana yazdıran fonksiyon
def kare():
    #s=int(input("Sayı:"))
    s=10
    print("Karesi:",pow(s,2))
#Kendisine gönderilen sayının fonksiyonda girilen değere göre üssünü hesaplayıp ekrana yazdıran fonksiyon
def us(s):
    u=int(input("Us:"))
    print(s,"^",u,":",pow(s,u))
#Bir sayının asal sayı olup olmadığını ekrana yazdıran fonksiyon asayi()
def asayi():
    sayi=2
    kontrol=True #ilk aşamada sayı asal olarak düşünülür
    #asal sayı: 1 ve kendisinden başka böleni olmayan sayılardır.
    #Öyleyse 2 ile kendisine kadar olan (kendisi dahil değil) sayılara bölünüyor mu diye bakarız
    for i in range(2,sayi):
        if sayi%i==0:
            kontrol=False
            break
    if kontrol and sayi>=2:
        print("Sayı asaldır")
    else:
        print("Sayı asal değildir")

#İki sayı girişi alan fonksiyon: sayigir()
def sayigir():
    s1,s2=int(input("Min:")),int(input("Mak:"))
    if (s1>s2):
        s1,s2=s2,s1
    return s1,s2
#sayigir() fonksiyonunda girilen değerler arasındaki değerlerden asal sayıları listeye atayan fonksiyon asalsayi()
def asalsayi():
    mn,mk=sayigir()
    liste=[] #liste=list()
    for sayi in range(mn,mk+1):
        kontrol=True
        for i in range(2,sayi):
            if sayi%i==0:
                kontrol=False
                break
        if kontrol and sayi>=2:
            liste.append(sayi)
    yazdir2(liste)
    return liste
    
#asalsayi() fonksiyonunda üretilen listeyi ekrana yazdıran fonksiyon yazdir()
def yazdir():
    print(asalsayi())
def yazdir2(liste):
    print(liste)
    tliste(liste)
#listenin toplamını yazdıracak fonksiyon toplam()
def tliste(liste):
    print("Toplam:",sum(liste))

def main():
    print(toplam())
    print(t(5,2))
    l,m=mak()
    print("Liste:",l,"\nMak:",m)
    print("Liste & Mak:",mak())
    kare()
    #sayi=int(input("Sayı:"))
    #us(sayi)
    #asayi()
    yazdir()
main()
