# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:16:59 2019

@author: gozdemihranaltinsoy
"""

#lambda_adi=lambda parametre:dönen_deger(ler)
#parametre fonksiyona dışarıdan gönderilen değer(ler)

#kendisine gelen sayının 2 katını döndüren fonksiyon
def ikikati(sayi):
    return sayi*2

print(ikikati(3))

ikikati2=lambda a:a*2

print(ikikati2(5))

#kendisine gelen sayıyı geri döndüren lambda
x=lambda i:i

print("D:",x(10))
#sayının 10 fazlasını ekrana yazdıralım
x2=lambda i:i+10

print("S+10:",x2(5))

#kendisine gelen 2 sayının toplamını hesaplatan lambda
t=lambda s1,s2:s1+s2

print("T:",t(15,10))

#iki sayının birbirine bölümünden kalanı hesaplayan lambda

k=lambda x,y:x%y

print("Kalan:",k(10,3))

#iki sayının birbirine bölümünü hesaplayan lambda

b=lambda x,y:int(x/y)

print("Bölüm:",b(10,3))

#kendisine gönderilen listedeki en büyük değeri döndüren lambda
mak=lambda i:max(i)

liste=[10,5,3,7,8,100]
print("mak:",mak(liste))

#kendisine gönderilen metni tersten yazdıran lambda
ters=lambda a:a[::-1]

print(ters("Beykoz"))

#kendisine gönderilen metnin 5. harfi ile 6. harfini geri döndüren lambda

p=lambda a:a[4:6]

print(p("Beykoz"))

#girilen sayının tek veya çift olduğunu bulan lambda
tç=lambda a:a%2==0

#sayi=int(input("Sayı:"))
sayi=10
if (tç(sayi)):
    print("Çift")
else:
    print("Tek")

#iki sayının çarpımını ekrana yazdıran fonksiyon
def carpim(s1,s2):
    return s1*s2

print("Ç:",carpim(5,2))


