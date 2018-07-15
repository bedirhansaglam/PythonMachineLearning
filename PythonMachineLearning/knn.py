# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 19:50:49 2017

@author: Bedirhan
"""
import matplotlib.pyplot as plt

def dataload_knn():
    veriListesi=[]
    veriListesi.append((2,4,"kotu"))
    veriListesi.append((3,6,"iyi"))
    veriListesi.append((4,10,"kotu"))
    veriListesi.append((3,4,"iyi"))
    veriListesi.append((5,8,"kotu"))
    veriListesi.append((6,3,"iyi"))
    veriListesi.append((7,9,"iyi"))
    veriListesi.append((9,7,"kotu"))
    veriListesi.append((11,7,"kotu"))
    veriListesi.append((10,2,"kotu"))
        
    for m in veriListesi:
        renk=''
        if m[2]=="kotu":
            renk='b^'
        else:
            renk='ro'
        plt.plot(m[0],m[1],renk,markersize=10)
        
    plt.axis([0,30,0,30])
    plt.title("Veri Seti")
    plt.savefig("./resource/knn_data_set.png")
    
    return veriListesi