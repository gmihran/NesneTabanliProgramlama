# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:17:41 2019

@author: ersinşahin
"""

f=open("11.txt","r+",encoding="utf-8")
a=f.read()
a=list(a)

b=[]

for i in a:
    if i==" " or i=="\n":
        a.remove(i)
        
        
for i in range(0,len(a)-1):
    if i%2==0:
        s=str(a[i])+str(a[i+1])
        b.append(s)


e=[ [0 for i in range(20) ] for j in range(20) ]


o=0
for i in range(0,20):
    for j in range(0,20):
        e[i][j]=b[o]
        o+=1
        
s=0        
for i in range (1):
    for j in range(0,20):
        s+=int(e[i][j])

c=[]      
s1=0
for i in range (0,20):
    for j in range(0,17):
        s1=int(e[i][j])*int(e[i][j+1])*int(e[i][j+2])*int(e[i][j+3])
        c.append(s1)

c.sort(reverse=False)  
      
print(sum(c))