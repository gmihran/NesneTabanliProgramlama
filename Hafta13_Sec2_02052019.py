# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:14:48 2019

@author: gozdemihranaltinsoy
"""
#%%
import modulum
print(modulum.toplam2(5,2))
print(modulum.toplam3(3,2,1))
print(help(modulum))
modulum.liste.sort()
print(modulum.liste)
#%%
from modulum import *
print(toplam2(10,2))
print(liste)
#%%
import modulum as islem
islem.liste.sort(reverse=True)
print(islem.liste)
#%%
import math
print(help(math)) #fonksiyonları, dataları açıklamalarıyla listeler
print(dir(math))  #fonksiyonları listeler

print(math.ceil(5.4)) #yukarı yuvarlar
print(math.floor(10.6)) #aşağı yuvarlar
print(math.factorial(5)) #faktöriyeli getirir

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
    secim=int(input("Seçiminiz:"))
    if secim==6:
        break
    sayi=eval(input("Sayı:"))
    if secim==1:
        print(math.ceil(sayi))
    elif secim==2:
        print(math.floor(sayi))
    elif secim==3:
        print(math.factorial(sayi))
    elif secim==4:
        us=eval(input("Us:"))
        print(math.pow(sayi,us))
    elif secim==5:
        print(math.sqrt(sayi))
    else:
        print("Hatalı seçim...")
#%%     
#Soru 2. İki parametre alan toplama(s1,s2), çıkarma(s1,s2), çarpma(s1,s2) ve bölme(s1,s2)  fonksiyonlarına sahip (toplama, çıkarma, çarpma, bölme işlemlerini hesaplatan) dortislem isimli modül oluşturalım ve projemize import edip fonksiyonları test edelim
from dortislem import *
print(toplama(5,2))     
print(cikarma(5,2)) 
print(carpma(5,2)) 
print(bolme(5,2)) 

#print(bolme(5,0)) 
#print(bolme(5,"a")) 

try:
    print(bolme(5,0)) 
except:
    print("Hatalı işlem")

try:
    print(bolme(5,"a")) 
except:
    print("Hatalı işlem")

try:
    print(bolme(5,0)) 
except ZeroDivisionError:
    print("Sıfıra bölünme hatası var")

try:
    print(bolme(5,"a")) 
except TypeError:
    print("Tip uyuşmazlığı hatası var")

try:
    print(bolme(5,"a"))
    print(bolme(5,2)) #hatalı koddan sonraki try adımları çalışmaz
except ZeroDivisionError:
    print("Sıfıra bölünme hatası var")
except TypeError:
    print("Tip uyuşmazlığı hatası var")
finally:
    print("Bu bölüm çalıştı...")


try:
    sayi1,sayi2=int(input("Sayi:")),int(input("Sayi:"))
    print(dortislem.toplama(sayi1,sayi2))
except ValueError:
    print("Geçersiz değer girdiniz...")
    #Kullanıcı geçersiz bir değer girerse program buraya dallanır

#Kullanıcı geçerli bir değer girine kadar kullanıcıdan değer isteyelim...