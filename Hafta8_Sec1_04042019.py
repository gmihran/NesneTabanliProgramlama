# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:42:45 2019

@author: gozdemihranaltinsoy
"""
#Modüller (Metodlar - Fonksiyonlar)
#Kendisine gönderilen iki sayının toplamını hesaplayan metod:

def toplam(sayi1,sayi2):
    return sayi1+sayi2

#Kendisine gönderilen sayının faktöriyelini hesaplayan metod:
def faktoriyel(sayi):
    f=1
    for i in range(1,sayi+1): #1'den sayi değerine kadar 
        f*=i
    return f

#Sayının karesini ekrana yazdıran metod:
def kare():
    sayi=int(input("Sayı giriniz..:"))
    print(pow(sayi,2))

#Kendisine gönderilen sayı ve üs değerlerine göre üssünü hesaplayıp
#ekrana yazdıran metod:
def us(sayi,us):
    print(pow(sayi,us))

#Rastgele 1 ile 100 arasında üretilen 10 sayının toplamını döndüren (return) metod:
def rast():
    import random
    liste=[]
    for i in range(1,11):
        liste.append(random.randint(1,100))
    print(liste)
    print("Mak:",max(liste))
    print("Min:",min(liste))
    return sum(liste)

#10 sayısının 3 sayısına bölümünden kalanı ekrana yazdıran metod:
def kalan():
    print(s1%s2)
    
#Kendisine gönderilen değer kadar kendisine gönderilen
#min ve mak değerler arasında random değer üretip
#bu değerleri ana metoda döndüren metod:
#Parametre 3 değer, döndürülen random değerler (liste)
def rastgele(n,mn,mk):
    import random
    sayilar=[]
    for i in range(n):
        sayilar.append(random.randint(mn,mk))
    return sayilar



def taskagitmakas():
    print("1.Taş 2.Kağıt 3.Makas")

#Kullanıcıya 3 seçenek gösterelim
#1. seçeneği tercih ederse; 
    #Taş kağıt makas oyununu yazdığımız metodu çağırsın
#2. seçeneği tercih ederse
    #1.Listeyi görüntüleme
    #2.Global bir listeye değer ekleme (liste metoddan önce ve dışında tanımlanacak)
    #3.Listeden seçilen değeri silme
    #4.Listeyi A'dan Z'ye sıralama
#3. seçeneği tercih ederse   
    #Çıkış
liste=["Beykoz","Sarıyer","Usküdar","Kadıköy","Mecidiyeköy","Istinye"]

def menu():
    while(True):
        print("1-Taş Kağıt Makas Oyunu\n2-Liste\n3-Çıkış")
        secim=int(input("Seçiminiz:"))
        if (secim==1):
            taskagitmakas()
        elif (secim==2):
            print("1-Liste Görüntüleme\n2-Ekleme\n3-Silme\n4-Sıralama")
            secim2=int(input("Seçiminiz:"))
            if (secim2==1):
                print(liste)
            elif (secim2==2):
                liste.append(input("Şehir giriniz:"))
            elif (secim2==3):
                print(liste,"\n kaçıncı değeri silmek istersiniz?:")
                a=int(input("Değer no:"))
                liste.pop(a-1)
                print(liste)
            elif (secim2==4):
                liste.sort()
                print(liste)
            else:
                print("Hatalı seçim")
        elif (secim==3):
            break
        else:
            print("Hatalı seçim")
    
s1=10
s2=3
def main():
    # %%
    print(toplam(5,10))
    
    # %%
    sayi=int(input("Faktöriyeli alınacak sayıyı giriniz..:"))
    print(faktoriyel(sayi))
    
    # %%
    kare()
    
    # %%
    us(5,4)
    
    # %%
    toplam=rast()
    print("Toplam:",toplam)
    
    # %%
    print(s1+s2)
    
    # %%
    kalan()
    
    # %%
    liste=rastgele(5,10,15) 
    #5 tane değer üret, değerler 10 ile 15 arasında olsun
    print(liste)
    
    # %%
    a,b,c=int(input("n:")),int(input("mn:")),int(input("mk:"))
    liste=rastgele(a,b,c)
    #a tane değer üret, değerler b ve c aralığında olsun
    print(liste)
    
    # %%
    menu()
    
    # %%
main()

