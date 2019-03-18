# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:20:43 2019

@author: gozdemihranaltinsoy
"""

f=open("11.txt","r+",encoding="utf-8")
a=f.read()
#print(a[0])

"""
a=str(a)
b=a.split()
print(b)
"""

a=list(a)

b=[]

for i in a:
    if i==" " or i=="\n":
        a.remove(i)
"""
for i in range(0,len(a)-1,2):
    s=str(a[i])+str(a[i+1])
    b.append(s)
"""    

for i in range(0,len(a)-1):
    if i%2==0:
        s=str(a[i])+str(a[i+1])
        b.append(s)

#print(b)

e=[ [0 for i in range(20)] for j in range(20) ] #400 eleman
print(e)
sayac=0
for i in range(0,20):
    for j in range(0,20):
        e[i][j]=b[sayac]
        sayac+=1
print(e)


#Matrisin ilk satırının elemanları toplamı
toplam=0
for i in range(0,20):
    toplam+=int(e[0][i])
#string olduğu için int dönüştürdük
print(toplam)

c=[]
for i in range(0,20):
    for j in range (0,17):
        carpim=1
        for k in range(0,4):
            carpim*=int(e[i][j+k])
        c.append(carpim)
#string olduğu için int dönüştürdük
c.sort(reverse=False) 
#Küçükten büyüğe sıralar
print(c)

print(max(c))

