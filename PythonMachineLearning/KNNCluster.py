# -*- coding: utf-8 -*-
"""
---- KNN Kümeleme -----
Rastgele dataset oluşturuyoruz , oluşturduğumuz noktaların (0,0) noktasına olan uzaklığını buluyoruz (Minkowski,Manhattan Veya Öklid).
Daha sonra orijine en yakın noktayı ve en uzak noktayı belirliyoruz bu 2 nokta 2 grubun referans noktası oluyor.
Datasetteki bütün noktaların uzaklıkları referans noktalara göre hesaplanıyor ve 2 listede bu değerler tutuluyor.
Örn groupA=(dataset[1],uzaklık),(dataset[2],uzaklık)... groupB=(dataset[1],uzaklık),(dataset[2],uzaklık)...
Bu 2 listedeki uzaklık değerleri karşılaştırılıyor ve datasetteki nokta hangi referans noktasına daha yakınsa o gruba dahil ediliyor.
-----------------------
"""

from math import sqrt
from math import pow
import numpy as np
import matplotlib.pyplot as plt


def datasetOlustur(maxRange,count):
    data = np.random.random_integers(0, maxRange, count*2).reshape((count,2))
    plt.cla()
    for m in data:
        renk='go'
        plt.plot(int(m[0]),int(m[1]),renk)

    plt.show
    plt.savefig("./resource/knn_kume_data.png")
    return data

def minkowski_liste(ref,verilistesi):
    dataset=verilistesi
    veri=[]
    for j in dataset:
        bisey=(pow(abs(ref[0]-j[0]),3)+pow(abs(ref[1]-j[1]),3))
        mnk=pow(bisey,0.33)
        veri.append(mnk)
    return veri 

def minkowski_sifir(verilistesi):
    dataset=verilistesi
    veri=[]
    for j in dataset:
        bisey=(pow(abs(j[0]-0),3)+pow(abs(j[1]-0),3))
        mnk=pow(bisey,0.33)
        veri.append((mnk,j))
    
    veri=sorted(veri, key=lambda veri: veri[0])
    return veri 
    
def manhattan_liste(ref,verilistesi):
    dataset=verilistesi
    veri=[]
    for j in dataset:
        veri.append((abs(ref[0]-j[0])+abs(ref[1]-j[1]))) 
    return veri 

def manhattan_sifir(verilistesi):
    dataset=verilistesi
    veri=[]
    for j in dataset:
        veri.append(((abs(j[0]-0)+abs(j[1]-0)),j)) 
    
    veri=sorted(veri, key=lambda veri: veri[0])
    return veri 
    
def oklid_liste(ref,verilistesi):
    dataset=verilistesi
    veri=[]
    for j in dataset:
        veri.append((sqrt(pow((ref[0]-j[0]),2)+pow(ref[1]-j[1],2))))
    
    return veri            

def oklid_sifir(verilistesi):
    dataset=verilistesi
    veri=[]
    for i in dataset:
        veri.append(((sqrt(pow((i[0]-0),2)+pow(i[1]-0,2))),i))
    veri=sorted(veri, key=lambda veri: veri[0])
    return veri

    
def kumele(dataset,currentIndex):
    if currentIndex==0:
        uzakliksifir=oklid_sifir(dataset)
    elif currentIndex==1:
        uzakliksifir=manhattan_sifir(dataset)
    elif currentIndex==2:
        uzakliksifir=minkowski_sifir(dataset)
    son=len(uzakliksifir)-1
    a1=[]
    b1=[]
    a_ref=uzakliksifir[0][1]
    b_ref=uzakliksifir[son][1]    
    
    if currentIndex==0: # oklid
        for a in dataset:
            a_list=oklid_liste(a_ref,dataset)
            b_list=oklid_liste(b_ref,dataset)
        for i in range (0,len(a_list)):
            if a_list[i] >b_list[i]:
                b1.append((dataset[i]))
            else:
                a1.append((dataset[i]))
                
    elif currentIndex==1: #manhattan
        for a in dataset:
            a_list=manhattan_liste(a_ref,dataset)
            b_list=manhattan_liste(b_ref,dataset)
        for i in range (0,len(a_list)):
            if a_list[i] >b_list[i]:
                b1.append((dataset[i]))
            else:
                a1.append((dataset[i]))
    elif currentIndex==2:#minkowski
        for a in dataset:
            a_list=minkowski_liste(a_ref,dataset)
            b_list=minkowski_liste(b_ref,dataset)
        for i in range (0,len(a_list)):
            if a_list[i] >b_list[i]:
                b1.append((dataset[i]))
            else:
                a1.append((dataset[i]))
    
    plt.cla()
    for m in a1:
        renk='ro'
        plt.plot(int(m[0]),int(m[1]),renk)
    for m in b1:
        renk='bo'
        plt.plot(int(m[0]),int(m[1]),renk)
    
    plt.show
    plt.savefig("./resource/knn_kume.png")


