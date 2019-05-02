# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:24:00 2019

@author: gozdemihranaltinsoy
"""

#%%
import math
print(dir(math))
print(math.ceil(5.4)) #yukarı yuvarla
print(math.floor(5.7)) #aşağı yuvarla
print(round(5.4)) #yuvarla
print(round(5.7)) #yuvarla
print(math.factorial(5))
print(help(math))

#%%
from math import *
print(ceil(5.4))

#%%
import math as matematik
print(matematik.ceil(3.4))

#%%
from hesaplama import *
print(toplama2(3,4))
print(toplama3(5,8,2))
sayilar.sort()
print(sayilar)
print(buyuksayi(4,6))
print(kucuksayi(5,7))

def toplama2():
    sayi1=int(input("1.sayi:"))
    sayi2=int(input("2.sayi:"))
    return sayi1+sayi2

print(toplama2())
from hesaplama import *
print(toplama2(5,6))


#%%
#Soru 1. Math modülündeki fonksiyonları kullanarak bir hesap makinesi geliştirelim
#1.Yukarı yuvarla (ceil) 
#2.Aşağı yuvarla (floor) 
#3.Faktöriyel(factorial)
#4.Üs alma (pow) 
#5.Karekök alma (sqrt)
#6.Çıkış

import math
while True:
    print("""
    1.Yukarı yuvarla (ceil) 
    2.Aşağı yuvarla (floor) 
    3.Faktöriyel(factorial)
    4.Üs alma (pow) 
    5.Karekök alma (sqrt)
    6.Çıkış""")
    secim=int(input("Seçiniz:"))
    if secim==6:
        break
    sayi=eval(input("Sayi:"))
    if secim==1:
        print(math.ceil(sayi))
    elif secim==2:
        print(math.floor(sayi))
    elif secim==3:
        print(math.factorial(sayi))
    elif secim==4:
        us=int(input("Us:"))
        print(math.pow(sayi,us))
    elif secim==5:
        print(math.sqrt(sayi))
    else:
        print("Geçersiz seçim...")

#%%
#Soru 2. İki parametre alan toplama(s1,s2), çıkarma(s1,s2), çarpma(s1,s2) ve bölme(s1,s2)  fonksiyonlarına sahip (toplama, çıkarma, çarpma, bölme işlemlerini hesaplatan) dortislem isimli modül oluşturalım ve projemize import edip fonksiyonları test edelim
import dortislem
print(help(dortislem))
print(dortislem.bolme(5,2))
try:
    print(dortislem.bolme(5,0))
except:
    print("Hatalı işlem")
finally:
    print("İşlem devam ediyor...")
try:
    print(dortislem.bolme(5,"a"))
except:
    print("Hatalı işlem")
finally:
    print("İşlem devam ediyor...")
    
try:
    print(dortislem.bolme(5,"a"))
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez")
except TypeError:
    print("Değerler geçerli değil")
    
try:
    print(dortislem.bolme(5,0))
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez")
except TypeError:
    print("Değerler geçerli değil")
    
print(dortislem.toplama(4,5))
print(dortislem.carpma(4,5))
print(dortislem.cikarma(4,5))
"""
try:
    sayi1,sayi2=int(input("Sayi:")),int(input("Sayi:"))
    print(dortislem.toplama(sayi1,sayi2))
except ValueError:
    print("Geçersiz değer girdiniz...")
    #Kullanıcı geçersiz bir değer girerse program buraya dallanır
"""
#Kullanıcı geçerli bir değer girine kadar kullanıcıdan değer isteyelim...
while True:
    try:
        sayi1,sayi2=int(input("Sayi1:")),int(input("Sayi2:"))
        print(dortislem.toplama(sayi1,sayi2))
        break #bu kodun çalışabilmesi için kullanıcının geçerli bir sayı girmesi gerekir. Hatalı bir değer girilirse direk except yapısına dallanır
    except ValueError:
        print("Geçersiz değer girdiniz...")    

#%%
#Bir modül oluşturalım. Modül adı: ilkmodulum
#1. Girilen sayının asal sayı olup olmadığını bulup asal ise True, asal değil ise False değerini döndüren fonksiyon
#2. 1 ile 100 arasındaki asal sayıları bir listede tutup bu listeyi geri döndüren fonksiyon 
#import ilkmodulum

#import ilkmodulum as moduller
#moduller.asal(2)
#artık moduller ismiyle çağırırız

#import ilkmodulum
#ilkmodulum.asal(2)
#fonksiyonu çağırırken ilkmodulum diye belirtmek zorundayız 

#from ilkmodulum import asal,asalsayilar
#sadece bu iki fonksiyonu projeye dahil eder
        
from ilkmodulum import *
if asal(5):
    print("Asal")
else:
    print("Asal değil")
    
asalliste=asalsayilar()
print(asalliste)

#%%
import hesaplama
print(help(hesaplama))

#Sayı tahmin oyunu

#5 sayı burada girilecek ve 2.fonk (kontrolet) ile tek tek kontrol edilecek
"""
Modul - sayitahmin
1. fonk (sayiuret)-> 10 tane 1 ile 30 arasında sayı üreten bir fonksiyon tanımlanacak
2. fonk (kontrolet)-> Kullanıcının girdiği 5 değer, bu üretilen 10 sayının içinde var mı kontrol etsin ve olanları bir listede tutsun. time ile 1 sn bekletip "Kontrol ediliyor" çıktısını verelim 
time.sleep(1) -> 1 sn. bekler
3. fonk (yazdir)-> Doğru bilmiş olduğu değerlerin listesini ekrana yazdırsın
"""
import time
import sayitahmin
liste=[]
for i in range(5):
    liste.append(int(input("Sayi:")))
    time.sleep(1)
sayitahmin.yazdir(liste)
