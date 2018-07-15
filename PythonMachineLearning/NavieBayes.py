# -*- coding: utf-8 -*-
"""
Created on Tue Jan 02 00:11:04 2018

@author: Bedirhan
"""

def default_training_data():
    training_data=[]
    training_data.append(("futbol","spor"))
    training_data.append(("basketbol","spor"))
    training_data.append(("tenis","spor"))
    training_data.append(("voleybol","spor"))
    training_data.append(("gol","spor"))
    training_data.append(("puan","spor"))
    training_data.append(("sayı","spor"))
    training_data.append(("kaleci","spor"))
    training_data.append(("hakem","spor"))
    training_data.append(("skor","spor"))
    training_data.append(("galatasaray","spor"))
    training_data.append(("fenerbahçe","spor"))
    training_data.append(("beşiktaş","spor"))
    training_data.append(("bursaspor","spor"))
    training_data.append(("trabzonspor","spor"))
    training_data.append(("futbolcu","spor"))
    training_data.append(("mhk","spor"))
    training_data.append(("tff","spor"))
    training_data.append(("birincilig","spor"))
    training_data.append(("süperlig","spor"))
    training_data.append(("lider","spor"))
    training_data.append(("smaç","spor"))
    training_data.append(("ribaund","spor"))
    training_data.append(("faul","spor"))
    training_data.append(("ofsayt","spor"))
    training_data.append(("para","ekonomi"))
    training_data.append(("euro","ekonomi"))
    training_data.append(("dolar","ekonomi"))
    training_data.append(("tl","ekonomi"))
    training_data.append(("altın","ekonomi"))
    training_data.append(("alış","ekonomi"))
    training_data.append(("satış","ekonomi"))
    training_data.append(("çek","ekonomi"))
    training_data.append(("senet","ekonomi"))
    training_data.append(("çeyrek","ekonomi"))
    training_data.append(("faiz","ekonomi"))
    training_data.append(("hisse","ekonomi"))
    training_data.append(("cari","ekonomi"))
    training_data.append(("oran","ekonomi"))
    training_data.append(("açık","ekonomi"))
    training_data.append(("deflasyon","ekonomi"))
    training_data.append(("enflasyon","ekonomi"))
    training_data.append(("imf","ekonomi"))
    training_data.append(("makro","ekonomi"))
    training_data.append(("piyasa","ekonomi"))
    training_data.append(("sermaye","ekonomi"))
    training_data.append(("endeks","ekonomi"))
    training_data.append(("yatırım","ekonomi"))
    training_data.append(("yatırımcı","ekonomi"))
    training_data.append(("tahvil","ekonomi"))
    return training_data
    
def prior_probability(text,liste):
    a=0
    b=0
    for i in liste:
        if i[1]==text:
            a=a+1
        else:
            b=b+1
    sonuc=float(a)/(a+b)
    return sonuc

def t_hesapla(text,category,liste):
    testliste=[]
    a=1
    for i in liste:
        if i[1]==category:
            testliste=i[0].split( )
            for t in testliste:
                if t==text:
                    a=a+1
    return a

def p_hesapla(text,category,t_values):
    toplam_deger=0
    text_degeri=0
    p_degeri=0
    for t in t_values:
        if t[1]==category:
            toplam_deger+=t[2]
            if t[0]==text:
                text_degeri=t[2]
    
    p_degeri=float(text_degeri)/toplam_deger
    return p_degeri

def fit(liste):
    cat=[] #kategoriler
    pp=[] #Prior Probablity list
    t_value=[]
    p_value=[]
    # listedeki kategoriler ayriliyor
    for item in liste:
        if item[1] not in cat:
            cat.append(item[1])
            
    #kategorilerin prior probability degeri hesaplaniyor
    for c in cat:
        pp.append((c,prior_probability(c,liste)))
    
    for c in cat:
        for item in liste:
            t_value.append((item[0],c,t_hesapla(item[0],c,liste)))
    
    for c in cat:
        for item in liste:
            p_value.append((item[0],c,p_hesapla(item[0],c,t_value)))
    
    return p_value

def predict(cumle,p_val):
    import numpy as np
    p_values=p_val
    cat=[]
    cat_val=[]
    for val in p_values:
        if val[1] not in cat:
            cat.append(val[1])
            
    words=[]
    for i in cumle.split():
        words.append(i.lower())
    
    for c in cat:
        p_c=1
        for word in words:
            for p in p_values:
                if word == p[0] and c==p[1]:
                    p_c*=float(p[2])
              
        cat_val.append((c,p_c))
    
    max_list=sorted(cat_val, key=lambda cat_val: cat_val[1])
    print max_list
    mm=max_list[len(max_list)-1][0]
    return mm

    

  