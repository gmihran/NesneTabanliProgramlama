#https://repl.it/languages/python3 ile oluþturuldu.

#string parçalama
kelime="Merhaba"
#Çýktý: h
print(kelime[3])
#Çýktý: Merh
print(kelime[:4])

#Çýktý: haba
print(kelime[3:])
#Çýktý: ha
print(kelime[3:5])
#Merhaba Çýktý: Mraa 
print(kelime[::2])
#Sadece sesli harfler
sesli="aeýioöuü" #string
sayac=0
print("Sesli Harfler:")
for i in kelime:
  if i in sesli:
    print(i)
    sayac+=1
print("Sesli harf sayýsý:",sayac)
for i in range(0,len(kelime)):
  if kelime[i] in sesli:
    print(i+1,".=",kelime[i])

sozluk={"elma":"apple","muz":"banana","barýþ":"peace","kuzey":"north","güney":"south","bilgisayar":"computer"}
#kelime=input("Kelimeyi girin..:")
#print(sozluk[kelime])
print(sozluk.items())
print(sozluk.keys())
print(sozluk.values())
#items elma,apple
#key elma
#values apple

#Listeyi sýralama:
liste=[10,45,30,23,27,2]
liste.sort()
print(liste)
liste.sort(reverse=True)
print(liste)

#Oyun:
#Listemiz 6 tane rastgele sayýdan oluþsun
#Sayý aralýðý 1-45 arasýnda
#Kullanýcýnýn kaç tane sayýyý doðru tahmin ettiðini yazdýralým
#Not: Üretilen sayýlar benzersiz olmalý (ara sýnavlardan sonra çözülecek), bu sayýlar sýralý olmalý
liste=[]
tahmin=[]
import random
for i in range(1,7):
  liste.append(random.randint(1,15))
  tahmin.append(int(input("Tahmininiz:")))

liste.sort()
tahmin.sort()
#A'dan Z'ye doðru sýralý bir þekilde yazdýrýlýyor...
print("Random sayýlar:")
print(liste)
print("Tahminler:")
print(tahmin)
sayac=0
for i in tahmin:
  if i in liste:
    sayac+=1
print("Doðru Tahmininiz:",sayac)

#Girilen sayýnýn 2 ile 9 arasýndaki rakamlara tam bölünüp bölünmediðinin çýktýsýný veren program
#Ör: 45
#2 bölünenemez
#3 bölünür
#4 bölünemez
#5 bölünür
#6 bölünemez
#7 bölünemez
#8 bölünemez
#9 bölünür
sayi=int(input("Sayý:"))
for i in range(2,10):
#i deðeri 2 ile 9 arasýndaki sayýlarý tutar
  if sayi%i==0:
    print(i," bölünür")
  else:
    print(i," bölünemez")


#1 ile 50 arasýndaki sayýlardan tek olanlarý ekrana yazdýralým
for i in range(1,51):
  if i%2==1:
    print(i)

#random üretilen 10 sayýdan (Random sayý aralýðý:1-100) çift olanlarý ekrana yazdýralým
import random
for i in range(10):
  sayý=random.randint(1,100)
  if sayý%2==0:
    print(sayý)
#random üretilen 10 sayýdan (Random sayý aralýðý:1-100) tek olanlarý teksayý, çift olanlarý çiftsayý, tüm sayýlarý da sayýlar listesinde tutup, ayrý ayrý ekrana yazdýralým
çiftsayý=[]
teksayý=[]
sayýlar=[]
for i in range(10):
  sayý=random.randint(1,100)
  sayýlar.append(sayý)
  if sayý%2==0:
    çiftsayý.append(sayý)
  else:
    teksayý.append(sayý)
sayýlar.sort()
print("Tüm sayýlar:")
print(sayýlar)
teksayý.sort()
print("Tek sayýlar:")
print(teksayý)
çiftsayý.sort()
print("Çift sayýlar:")
print(çiftsayý)