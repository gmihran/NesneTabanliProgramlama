# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:47:35 2019

@author: gozdemihranaltinsoy
"""
"""
#Belirli bir sayı aralılığında(fonksiyon)
sayigir():
    return sayilar -> sayi1,sayi2
"""

def sayigir():
    s1,s2=int(input("Min:")),int(input("Mak:"))
    if (s1>s2):
        s1,s2=s2,s1
    #Kullanıcı ilk değeri daha büyük bir sayı girdiğinde bu değerler yer değiştirir. Bunu yapmazsak asalsayi metodunda for i döngüsü çalışmaz. Ör: Kullanıcı s1:10 ve s2:-100 girerse bu yer değiştirme adımı ile s1:-100 s2:10 değerini alır.
    return s1,s2
"""
#Asal sayıları bulup listede tutup ekrana yazdıracak(fonksiyon)
asalsayi():
    sayilar=sayigir()
    return liste
"""
def asalsayi():
    s1,s2=sayigir()
    liste=[]
    for i in range(s1,s2+1):
        #sayımızın (i) asal olup olmadığını kontrol edelim:
        #asal sayı: 1 ve kendisi dışında böleni olmayan sayıdır
        kontrol=True #asal sayı olduğunu tutar
        #kontrol true ise sayı asaldır. ilk aşamada sayının asal olduğunu kabul edelim 
        for j in range(2,i):
            #j sayının tam bölünüp bölünemediğini kontrol edeceğimiz sayı; i j sayısına bölünüyor mu?
            #Bölünüyorsa asal değildir
            if (i%j==0):
                kontrol=False
                break
        #if i<2:
        #    kontrol=False
        #if kontrol:
        #    liste.append(i)
        if kontrol and i>=2:
            liste.append(i)
    print(liste)
    return liste
    
"""
#Toplamını hesaplayıp(fonksiyon)
toplam():
    liste=asalsayi()
"""
def toplam():
    t=sum(asalsayi())
    return t
"""
#main içersinde toplam değeri yazdıracağız
main():
    print(toplam())
"""
def main():
    print("Toplam değer:",toplam())

main()
