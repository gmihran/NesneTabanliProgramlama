# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:32:59 2019

@author: gozdemihranaltinsoy
"""

#Modüller (Metodlar-Fonksiyonlar)
#Kendisine gönderilen iki sayının toplamını 
#ekrana yazdıran fonksiyon
def toplam(sayi1,sayi2):
    print("Toplam:",sayi1+sayi2)
    
#Kendisine gönderilen iki sayının çarpımını 
#metoda geri döndürecek fonksiyon
def carpim(sayi1,sayi2):
    return sayi1*sayi2

#Girilen değerin karesini ekrana yazdıran metod
def kare():
    sayi=int(input("Sayı:"))
    print(pow(sayi,2))

#Rastgele üretilen 1 ile 20 arasında 10 sayıyı listede tutup,
#bu listenin toplamını geri döndüren metod
def rastgele():
    import random
    liste=[]
    for i in range(10): #0 ile 9 arasında değer alır,10 kez çalışır
       liste.append(random.randint(1,20)) 
    print(liste)
    return sum(liste)

#Kendisine gönderilen n değeri kadar rastgele kendisine 
#gönderilen minimum ve maksimum değerler arasında sayı üretip,
#bu sayıları listede tutarak listeyi geri döndüren metod
def rastgele2(n,kucuk,buyuk):
    import random
    liste=[]
    for i in range(n): #n kere çalışır
       liste.append(random.randint(kucuk,buyuk)) 
    return liste

def main():
#%%
    toplam(5,10)
    s1,s2=int(input("1.sayı:")),int(input("2.sayı:"))
    toplam(s1,s2)
    print("Çarpım=",carpim(s1,s2))
#%%
    kare()
#%%
    print("Toplam:",rastgele())
#%%
    a,b,c=int(input("n:")),int(input("min:")),int(input("mak:"))
    sayilar=rastgele2(a,b,c)   
    print(sayilar)
       
#%%
main()









