"""
1. Girilen sayının asal sayı olup olmadığını bulup asal ise True, asal değil ise False değerini döndüren fonksiyon
2. 1 ile 100 arasındaki asal sayıları bir listede tutup bu listeyi geri döndüren fonksiyon 
"""

def asal(sayi):
    durum=True
    if sayi<=1:
        durum=False
    else:
        for i in range(2,sayi):
            if sayi%i==0:
                durum=False
                break
    return durum

def asalsayilar():
    liste=list() #liste=[] #boş liste tanımlanır
    for i in range(1,101):
        if asal(i):
            liste.append(i)
    return liste