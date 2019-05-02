"""
Burada sayı toplama, büyük sayı hesaplama gibi işlemler yer almaktadır.
"""

sayilar=[3,6,2,8,4,5,10]

def toplama2(s1,s2):
    """
    İki sayının toplamını geri döndürür
    """
    return s1+s2

def toplama3(s1,s2,s3):
    """
    Üç sayının toplamını geri döndürür
    """
    return s1+s2+s3

def buyuksayi(s1,s2):
    """
    İki sayı içerisindeki büyük sayıyı geri döndürür
    """
    if s1>s2:
        return s1
    elif s1<s2:
        return s2
    else:
        return 0

def kucuksayi(s1,s2):
    """
    İki sayı içerisindeki küçük sayıyı geri döndürür
    """
    if s1<s2:
        return s1
    elif s1>s2:
        return s2
    else:
        return 0
