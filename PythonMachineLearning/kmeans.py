# -*- coding: utf-8 -*-
from math import sqrt
from math import pow
from matplotlib import pyplot as plt

#rastgele etiketlenmiş verisetimiz mevcut


def data():
    veriListesi1=[]
    veriListesi1.append((4,2,"c1"))
    veriListesi1.append((6,4,"c2"))
    veriListesi1.append((5,1,"c2"))
    veriListesi1.append((10,6,"c1"))
    veriListesi1.append((11,8,"c2"))
    veriListesi1.append((12,10,"c2"))
    veriListesi1.append((9,6,"c2"))
    veriListesi1.append((12,7,"c1"))
    veriListesi1.append((15,12,"c1"))
    veriListesi1.append((26,7,"c2"))
    veriListesi1.append((3,5,"c2"))
    veriListesi1.append((8,9,"c2"))
    veriListesi1.append((1,1,"c2"))
    veriListesi1.append((7,8,"c1"))
    veriListesi1.append((1,25,"c2"))
    veriListesi1.append((4,22,"c2"))
    return veriListesi1

def plot(liste):
    plt.cla()
    for m in liste:
        renk=''
        if m[2]=="c1":
            renk='bo'
        else:
            renk='ro'
        plt.plot(m[0],m[1],renk)
    
    plt.title("Veri Seti Ilk hali")
    plt.savefig("./resource/kmeans_ilk.png")
    
    

def hesapla(liste):
#    print("iterasyon")
    veriListesi=liste
    
    c1x=0
    c2x=0
    
    c1s=0
    c2s=0
    
    c1y=0
    c2y=0
    

    for m in veriListesi:
        if m[2]=="c1":
            c1s=c1s+1
            c1x=c1x+m[0]
            c1y=c1y+m[1]
        else :
            c2s=c2s+1
            c2x=c2x+m[0]
            c2y=c2y+m[1]
        

    c1merkez=[]
    c2merkez=[]

    c1merkez.append((c1x/c1s, c1y/c1s))
    c2merkez.append((c2x/c2s,c2y/c2s))


    #print ("c1 merkez : ", c1merkez[0], "c2 merkez",c2merkez[0])

    yeniliste=[]

    c1uzaklik=0
    c2uzaklik=0
    
    #hataorani=0
    e1=0;
    e2=0;


    for m in veriListesi:
        c1uzaklik=sqrt(pow((int(m[0])-c1merkez[0][0]),2)+pow((int(m[1])-c1merkez[0][1]),2))
        c2uzaklik=sqrt(pow((int(m[0])-c2merkez[0][0]),2)+pow((int(m[1])-c2merkez[0][1]),2))
        
        e1=e1+pow((int(m[0])-c1merkez[0][0]),2)+pow((int(m[1])-c1merkez[0][1]),2)
        e2=e2+pow((int(m[0])-c2merkez[0][0]),2)+pow((int(m[1])-c2merkez[0][1]),2)
        if c1uzaklik>c2uzaklik:
            yeniliste.append("c2")
        else :
            yeniliste.append("c1")
    
    #print ("e1", e1,"e2",e2)
    #hataorani=e1+e2
    #print("Hata Oranı:",hataorani)
       
     
    degisim=0
    sonListe=[]

    for p in range(0,len(yeniliste)):
        if yeniliste[p]==veriListesi[p][2]:
            sonListe.append(veriListesi[p])
        else:
            sonListe.append((veriListesi[p][0],veriListesi[p][1],yeniliste[p]))
            degisim=degisim+1
    
    #for d in sonListe:
        #print (d[2])
    
    if degisim!=0:
        hesapla(sonListe)
    else:
        plt.cla()
        for d in sonListe:
            renk=''
            if d[2]=="c1":
                renk='bo'
            else:
                renk='ro'
            plt.plot(d[0],d[1],renk)
            
        plt.title("Veri Seti Son Hali")
        plt.savefig("./resource/kmeans_son.png")
        