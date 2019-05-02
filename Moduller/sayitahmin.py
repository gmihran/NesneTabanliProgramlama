"""
Modul - sayitahmin
1. fonk (sayiuret)-> 10 tane 1 ile 30 arasında sayı üreten bir fonksiyon tanımlanacak
2. fonk (kontrolet)-> Kullanıcının girdiği 5 değer, bu üretilen 10 sayının içinde var mı kontrol etsin ve olanları bir listede tutsun. time ile 1 sn bekletip "Kontrol ediliyor" çıktısını verelim 
time.sleep(1) -> 1 sn. bekler
3. fonk (yazdir)-> Doğru bilmiş olduğu değerlerin listesini ekrana yazdırsın
"""
def sayiuret():
    import random
    rastgele=[]
    for i in range(10):
        rastgele.append(random.randint(1,30))
    print(rastgele)
    return rastgele
def kontrolet(kullaniciliste):
    rastgelesayilar=sayiuret()
    kontrollistesi=[]
    for i in kullaniciliste:
        if i in rastgelesayilar:
            kontrollistesi.append(i)
    return kontrollistesi
def yazdir(liste):
    print(kontrolet(liste))