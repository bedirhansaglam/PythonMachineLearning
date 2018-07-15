# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:29:46 2017

@author: Bedirhan
"""

import os
import numpy as np

def saveData(filename,data):
    db=np.array(data)
    f=open(filename,'w')
    for i,a in enumerate(db):
        for p,j in enumerate(db[i]):
            if p!=(len(db[i])-1):
                f.write(j+",")
            else:
                f.write(j+"\n")

def readDataFile(filename):
    f = open(filename)
    data=[]
    for i,row in enumerate(f.readlines()):
        currentline = row.split(",")   
        temp=[]
        for column_value in currentline:
            temp.append(column_value)

        data.append(temp)
    data=np.array(data)
    return data

def allData():
    Data=[]
        #X_train datalari aktariliyor
    work_dir="./data/parkinson/hw_dataset"
    folderList=os.listdir(work_dir)
    for i,folder_name in enumerate(folderList):
        folder=os.listdir(work_dir+"/"+folder_name)
        if folder_name=="control":
            deger=0
        elif folder_name=="parkinson":
            deger=1
        for file_name in folder:
            f = open(work_dir+"/"+folder_name+"/"+file_name)
            for i,row in enumerate(f.readlines()):
                currentline = row.split(";")   
                temp=[]
                for i,column_value in enumerate(currentline):
                    if i!=5 and i!=6:
                        temp.append(column_value)
                    if i==6:
                        temp.append(deger)
                Data.append(temp)
                
    work_dir="./data/parkinson/new_dataset"
    folderList=os.listdir(work_dir)
    for i,folder_name in enumerate(folderList):
        folder=os.listdir(work_dir+"/"+folder_name)
        for file_name in folder:
            f = open(work_dir+"/"+folder_name+"/"+file_name)
            for i,row in enumerate(f.readlines()):
                currentline = row.split(";")   
                temp=[]
                for i,column_value in enumerate(currentline):
                    if i!=5 and i!=6:
                        temp.append(column_value)
                    if i==6:
                        temp.append(1)
                Data.append(temp)
    return Data
    
def SST_Data():
    Data=[]
        #X_train datalari aktariliyor
    work_dir="./data/parkinson/hw_dataset"
    folderList=os.listdir(work_dir)
    for i,folder_name in enumerate(folderList):
        folder=os.listdir(work_dir+"/"+folder_name)
        if folder_name=="control":
            deger=0
        elif folder_name=="parkinson":
            deger=1
        for file_name in folder:
            f = open(work_dir+"/"+folder_name+"/"+file_name)
            for i,row in enumerate(f.readlines()):
                currentline = row.split(";")   
                temp=[]
                if currentline[6]=="0\n":
                    for i,column_value in enumerate(currentline):
                        if i!=5 and i!=6:
                            temp.append(column_value)
                        if i==6:
                            temp.append(deger)
                    Data.append(temp)
    return Data

def DST_Data():
    Data=[]
        #X_train datalari aktariliyor
    work_dir="./data/parkinson/hw_dataset"
    folderList=os.listdir(work_dir)
    for i,folder_name in enumerate(folderList):
        folder=os.listdir(work_dir+"/"+folder_name)
        if folder_name=="control":
            deger=0
        elif folder_name=="parkinson":
            deger=1
        for file_name in folder:
            f = open(work_dir+"/"+folder_name+"/"+file_name)
            for i,row in enumerate(f.readlines()):
                currentline = row.split(";")   
                temp=[]
                if currentline[6]=="1\n":
                    for i,column_value in enumerate(currentline):
                        if i!=5 and i!=6:
                            temp.append(column_value)
                        if i==6:
                            temp.append(deger)
                    Data.append(temp)
    return Data

def STCP_Data():
    Data=[]
        #X_train datalari aktariliyor
    work_dir="./data/parkinson/hw_dataset"
    folderList=os.listdir(work_dir)
    for i,folder_name in enumerate(folderList):
        folder=os.listdir(work_dir+"/"+folder_name)
        if folder_name=="control":
            deger=0
        elif folder_name=="parkinson":
            deger=1
        for file_name in folder:
            f = open(work_dir+"/"+folder_name+"/"+file_name)
            for i,row in enumerate(f.readlines()):
                currentline = row.split(";")   
                temp=[]
                if currentline[6]=="2\n":
                    for i,column_value in enumerate(currentline):
                        if i!=5 and i!=6:
                            temp.append(column_value)
                        if i==6:
                            temp.append(deger)
                    Data.append(temp)
    return Data

def test_sst():
    Data=[]
        #X_train datalari aktariliyor
    work_dir="./data/parkinson/new_dataset"
    folderList=os.listdir(work_dir)
    for i,folder_name in enumerate(folderList):
        folder=os.listdir(work_dir+"/"+folder_name)
        for file_name in folder:
            f = open(work_dir+"/"+folder_name+"/"+file_name)
            for i,row in enumerate(f.readlines()):
                currentline = row.split(";")   
                temp=[]
                if currentline[6]=="0\n":
                    for i,column_value in enumerate(currentline):
                        if i!=5 and i!=6:
                            temp.append(column_value)
                        if i==6:
                            temp.append(1)
                    Data.append(temp)
    return Data

def test_dst():
    Data=[]
        #X_train datalari aktariliyor
    work_dir="./data/parkinson/new_dataset"
    folderList=os.listdir(work_dir)
    for i,folder_name in enumerate(folderList):
        folder=os.listdir(work_dir+"/"+folder_name)
        for file_name in folder:
            f = open(work_dir+"/"+folder_name+"/"+file_name)
            for i,row in enumerate(f.readlines()):
                currentline = row.split(";")   
                temp=[]
                if currentline[6]=="1\n":
                    for i,column_value in enumerate(currentline):
                        if i!=5 and i!=6:
                            temp.append(column_value)
                        if i==6:
                            temp.append(1)
                    Data.append(temp)
    return Data

def test_stcp():
    Data=[]
        #X_train datalari aktariliyor
    work_dir="./data/parkinson/new_dataset"
    folderList=os.listdir(work_dir)
    for i,folder_name in enumerate(folderList):
        folder=os.listdir(work_dir+"/"+folder_name)
        for file_name in folder:
            f = open(work_dir+"/"+folder_name+"/"+file_name)
            for i,row in enumerate(f.readlines()):
                currentline = row.split(";")   
                temp=[]
                if currentline[6]=="2\n":
                    for i,column_value in enumerate(currentline):
                        if i!=5 and i!=6:
                            temp.append(column_value)
                        if i==6:
                            temp.append(1)
                    Data.append(temp)
    return Data