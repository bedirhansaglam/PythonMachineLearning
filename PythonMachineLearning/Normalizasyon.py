# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:59:11 2017

@author: Bedirhan
"""
import statistics
import numpy as np

def zscore(data):
    zscoredata=[]
    standart_sapma=statistics.stdev(data)
    ortalama=statistics.mean(data)
    for d in data:
        z=(d-ortalama)/standart_sapma
        zscoredata.append(z)
    return zscoredata
    
def minmax(data):
    minmaxscoredata=[]
    maxData=max(data)
    minData=min(data)
    for d in data:
        m=(d-minData)/(maxData-minData)
        minmaxscoredata.append(m)
    return minmaxscoredata

def median(data):
    medianscore=[]
    med=statistics.median(data)
    for d in data:
        m=d/med
        medianscore.append(m)
    return medianscore

def normalizasyon(filename,currentIndex):
    f = open(filename)
    X=[]
    for i,row in enumerate(f.readlines()):
        
        currentline = row.split(",")   
        temp=[]
        for column_value in currentline:
            temp.append(column_value)

        X.append(temp)

    X=np.array(X)


    norm_veri=[]

    if len(X[0])!=len(X[len(X)-1]): #eger son satir ile ilk satirin degeri esit degilse son satiri siliyoruz
        X=np.delete(X,[len(X)-1]) 
    
    for a in range(0,len(X[0])-1):
        datalist=[]
        for b in range(0,len(X)):
            p=float(X[b][a])
            datalist.append(p)
        if currentIndex==0:
            norm_veri.append(minmax(datalist))
        elif currentIndex==1:
            norm_veri.append(zscore(datalist))
        elif currentIndex==2:
            norm_veri.append(median(datalist))


    y_list=[]
    for y in X:
        y_list.append(y[len(y)-1])
        
    norm_veri.append(y_list)
    norm_veri=np.array(norm_veri)
    norm_veri=np.transpose(norm_veri)
    return norm_veri
