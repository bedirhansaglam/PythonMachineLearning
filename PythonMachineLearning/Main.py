# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:13:38 2017

@author: Bedirhan
"""

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplotlib.pyplot as plt
import numpy
from PIL.ImageQt import ImageQt
from math import sqrt
from tasarim import Ui_Dialog
from sklearn.externals import joblib
import pickle
import kmeans
from knn import dataload_knn
from ParkinsonDataSet import SST_Data
from ParkinsonDataSet import DST_Data
from ParkinsonDataSet import STCP_Data
from ParkinsonDataSet import test_sst
from ParkinsonDataSet import test_dst
from ParkinsonDataSet import test_stcp
from ParkinsonDataSet import allData
import ParkinsonDataSet
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import KNNCluster
import Normalizasyon
import NavieBayes

class MainWindow(QtGui.QMainWindow,Ui_Dialog):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)  
        self.veriListesi=dataload_knn()
        self.gb_main_menu.setGeometry(QtCore.QRect(0, 50, 0, 670))
        self.pb_hamburger_menu.clicked.connect(self.main_menu_clicked)
        self.sifirla()
        self.gb_knn_sinif.setGeometry(QtCore.QRect(200,50,1080,670))
        self.pb_main_menu_1.clicked.connect(self.mm_pb_knn)
        self.pb_main_menu_2.clicked.connect(self.mm_pb_rus)
        self.pb_main_menu_3.clicked.connect(self.mm_pb_kmeans)
        self.pb_main_menu_4.clicked.connect(self.mm_pb_knn_kume)
        self.pb_main_menu_5.clicked.connect(self.mm_pb_navie)
        self.pb_main_menu_6.clicked.connect(self.mm_pb_normalizasyon)
        self.pb_main_menu_7.clicked.connect(self.mm_pb_random_forest)
        self.pb_main_menu_8.clicked.connect(self.mm_pb_train_test)
        self.pb_main_menu_9.clicked.connect(self.mm_pb_parkinson)
        #knn-kümeleme---b--
        self.knn_cluster_pb_create_dataset.clicked.connect(self.knn_cluster_create_dataset)
        self.knn_pb_cluster.clicked.connect(self.knn_cluster)
        #knn kümelme --s--
        #navie-text-class -b-
        self.pb_navie_veriekle.clicked.connect(self.navie_item_add)
        self.pb_navie_siniflandir.clicked.connect(self.navie_bayes_siniflandir)
        #rus-ros butons----b--
        self.rus_ros_pb_create_dataset.clicked.connect(self.rus_ros_dataSet_olustur)
        self.rus_ros_pb.clicked.connect(self.rus_ros_uygula)
        self.rus_ros_slider.valueChanged.connect(self.rus_ros_slider_changedValue)
        #rus-ros butons----s--
        #normalizasyon -b-
        self.pb_normalizasyon_dataload.clicked.connect(self.norm_data_load)
        self.pb_normalize.clicked.connect(self.normalize_uygula)
        self.pb_normalizasyon_datasave.clicked.connect(self.normalize_data_save)
        #normalizasyon -s-
        #Random Forest -b-
        self.pb_random_forest_data_load.clicked.connect(self.random_forest_data_load)
        self.pb_random_forest_tandt.clicked.connect(self.random_forest_train_test)
        self.random_forest_slider.valueChanged.connect(self.random_forest_slider_changedValue)
        self.pb_random_forest.clicked.connect(self.random_forest_uygula)
        self.pb_random_forest_modelsave.clicked.connect(self.random_forest_model_save)
        #Random forest -s-
        #Train & Test -B-
        self.pb_train_test_data_load.clicked.connect(self.train_test_data_load)
        self.pb_train_and_test.clicked.connect(self.train_test_uygula)
        self.test_and_train_slider.valueChanged.connect(self.test_and_train_slider_changedValue)
        #parkinson top menu --b-
        self.pb_parkinson_veri_yukle.clicked.connect(self.parkinson_veri_yukle)
        self.pb_parkinson_class.clicked.connect(self.parkinson_classfication)
        #parkinson top menu --s-
        #parkinson bottom menu --b-
        self.pb_parkinson_all_data.clicked.connect(self.parkinson_all_data)
        self.pb_parkinson_split.clicked.connect(self.parkinson_train_and_test)
        self.pb_parkinson_class_2.clicked.connect(self.parkinson_classfication_2)
        self.pb_parkinson_reload_split.clicked.connect(self.parkinson_reload)
        #parkinson bottom menu --s-
        self.form_load()
        

#============================================================================================================================================================
#---------Gorsel Showlar Baslangic ---------------------#  
  
    def main_menu_clicked(self):
        if self.gb_main_menu.width()==0:
            self.animation=QPropertyAnimation(self.gb_main_menu,"geometry")
            self.animation.setDuration(500)
            self.animation.setStartValue(QRect(0, 50, 0, 670))
            self.animation.setEndValue(QRect(0, 50, 200, 670))
            self.animation.start()
        else:
            self.animation=QPropertyAnimation(self.gb_main_menu,"geometry")
            self.animation.setDuration(500)
            self.animation.setStartValue(QRect(0, 50, 200,670))
            self.animation.setEndValue(QRect(0, 50, 0, 670))
            self.animation.start()
    
    def mm_pb_knn(self):
        self.sifirla()
        self.animasyon_baslat(self.gb_knn_sinif,200,50,1080,670)
    def mm_pb_rus(self):
        self.sifirla()
        self.animasyon_baslat(self.gb_rus_ros,200,50,1080,670)
    def mm_pb_kmeans(self):
        self.sifirla()
        self.animasyon_baslat(self.gb_k_means,200,50,1080,670)
        self.data_kmeans=kmeans.data()
        self.verileri_tabloya_dok(self.data_kmeans,self.k_means_tbl_data)
    def mm_pb_knn_kume(self):
        self.sifirla()
        self.animasyon_baslat(self.gb_knn_kume,200,50,1080,670)
    def mm_pb_navie(self):
        self.sifirla()
        self.animasyon_baslat(self.gb_navie,200,50,1080,670)
        self.navie_bayes_data_set=NavieBayes.default_training_data()
        self.verileri_tabloya_dok(self.navie_bayes_data_set,self.tbl_navie_data_set)
    def mm_pb_normalizasyon(self):
        self.sifirla()
        self.animasyon_baslat(self.gb_normalizasyon,200,50,1080,670)
    def mm_pb_random_forest(self):
        self.sifirla()
        self.animasyon_baslat(self.gb_randomforest,200,50,1080,670)
    def mm_pb_train_test(self):
        self.sifirla()
        self.animasyon_baslat(self.gb_train_test,200,50,1080,670)
    def mm_pb_parkinson(self):
        self.sifirla()
        self.animasyon_baslat(self.gb_parkinson,200,50,1080,670)
    
        
        
    def animasyon_baslat(self,animasyon,x,y,w,h):
        if animasyon.width()==0 :
            self.animation=QPropertyAnimation(animasyon,"geometry")
            self.animation.setDuration(1000)
            self.animation.setStartValue(QRect(x, y, 0, 0))
            self.animation.setEndValue(QRect(x, y, w, h))
            self.animation.start()

    def buton_animasyon(self,animasyon,x,y,w,h):
        if animasyon.width()==0:
            self.animation=QPropertyAnimation(animasyon,"geometry")
            self.animation.setDuration(500)
            self.animation.setStartValue(QRect(x, y, 0, h))
            self.animation.setEndValue(QRect(x, y, w, h))
            self.animation.start()
            
    def sifirla(self):
        self.gb_rus_ros.setGeometry(QtCore.QRect(200,50,0,0))
        self.gb_k_means.setGeometry(QtCore.QRect(200,50,0,0))
        self.gb_knn_kume.setGeometry(QtCore.QRect(200,50,0,0))
        self.gb_navie.setGeometry(QtCore.QRect(200,50,0,0))
        self.gb_knn_sinif.setGeometry(QtCore.QRect(200,50,0,0))
        self.gb_parkinson.setGeometry(QtCore.QRect(200,50,0,0))
        self.gb_normalizasyon.setGeometry(QtCore.QRect(200,50,0,0))
        self.gb_randomforest.setGeometry(QtCore.QRect(200,50,0,0))
        self.gb_train_test.setGeometry(QtCore.QRect(200,50,0,0))
        
#---------Gorsel Showlar Son ---------------------#  
#============================================================================================================================================================
#-------------Genel Fonksiyonlar  --------- Baslangic ------------------------        
    def show_image(self,img_name,width,height):
        pixMap=QtGui.QPixmap(img_name)
        pixMap=pixMap.scaled(width-5,height-5)
        pixItem=QtGui.QGraphicsPixmapItem(pixMap)
        scene=QGraphicsScene()
        scene.addItem(pixItem)
        return scene
    
    def show_pil_image(self,img,width,height):
        show_image=ImageQt(img)
        pixMap=QtGui.QPixmap.fromImage(show_image)
        pixMap=pixMap.scaled(width-5,height-5)
        pixItem=QtGui.QGraphicsPixmapItem(pixMap)
        scene=QGraphicsScene()
        scene.addItem(pixItem)
        return scene
    
    def verileri_tabloya_dok(self,table_value,table_name):
        num_rows=len(table_value) #tablonun satir sayisi aliniyor
        num_column=len(table_value[0]) #tablonun sutun sayisi aliniyor
        table_name.clear()        #tabloda onceden deger var ise temizleniyor
        table_name.setColumnCount(num_column) #tablonun sutun sayisi set ediliyor
        table_name.setRowCount(num_rows) #tablonun satir sayisi set ediliyor
        for rowNumber,row in enumerate(table_value):#tabloya eklenecek deger satir satir ve
            for columnNumber in range(0,len(table_value[0])):#sutun sutun okunuyor
                table_name.setItem(rowNumber,columnNumber,QtGui.QTableWidgetItem(str(row[columnNumber]))) #okunan degerler tabloya set ediliyor

    def RFclassification(self,X_train,y_train,X_test):
        self.rf_clf=RandomForestClassifier()            
        self.rf_clf.fit(X_train,y_train)
        results=self.rf_clf.predict(X_test)
        return results
    
    def DTclassification(self,X_train,y_train,X_test):
        clf=DecisionTreeClassifier()    
        clf.fit(X_train,y_train)
        results=clf.predict(X_test)
        return results

    def saveData(self,filename,data):
        db=numpy.array(data)
        f=open(filename,'w')
        for i,a in enumerate(db):
            for p,j in enumerate(db[i]):
                if p!=(len(db[i])-1):
                    f.write(j+",")
                else:
                    f.write(j)    
    
    def form_load(self):
        self.w,self.h=self.t1_gv_veriseti.width(),self.t1_gv_veriseti.height()
        self.t1_gv_veriseti.setScene(self.show_image("./resource/knn_data_set.png",self.w,self.h))
#-------------Genel Fonksiyonlar  --------- SON ------------------------      
#============================================================================================================================================================        
#------KNN Siniflandirma BASLANGİC-------------------------    
    def yeni_nokta_knn(self,x,y):
        plt.cla()
        for m in self.veriListesi:
            renk=''
            if m[2]=="kotu":
                renk='b^'
            else:
                renk='ro'
            plt.plot(m[0],m[1],renk,markersize=10)
        plt.plot(x,y,'gd',markersize=15)
        plt.savefig("./resource/knn_new_point.png")
    
    
    def KNN(self,k,x,y):
        sonuc=0
        plt.cla()
        self.uzakliklar=[]
        for m in self.veriListesi:
            oklid=sqrt(pow(int(x)-int(m[0]),2)+pow(int(y)-int(m[1]),2))
            self.uzakliklar.append((oklid,m[2]))
        
        self.uzakliklar.sort()
        
        for i in range(0,int(k)):
            if self.uzakliklar[i][1]=="iyi":
                sonuc=sonuc+1
            else:
                sonuc=sonuc-1
        
        if sonuc>0:
            self.veriListesi.append((int(x),int(y),"iyi"))
        else:
            self.veriListesi.append((int(x),int(y),"kotu"))
        
        for m in self.veriListesi:
            renk=''
            if m[2]=="kotu":
                renk='b^'
            else:
                renk='ro'
            plt.plot(m[0],m[1],renk,markersize=10)
        plt.savefig("./resource/knn_sonuc.png")
#------KNN siniflandirma SON-------------------------    
#============================================================================================================================================================
#---------------RUS VE ROS ------ FONKSİYONLAR---- BASLANGİC ---------
    def rus_ros_slider_changedValue(self):
        deger=self.rus_ros_slider.value()
        self.lbl_rus_ros_slider.setText(str(deger))
        
    def rus_ros_generate_dataset(self,samples,w1,w2):
        self.X_rus_ros, self.y_rus_ros = make_classification(n_classes=2, class_sep=2, weights=[w1, w2],
                           n_informative=3, n_redundant=1, flip_y=0,
                           n_features=20, n_clusters_per_class=1,
                           n_samples=int(samples), random_state=10)

        self.pca = PCA(n_components=2)
        self.X_vis= self.pca.fit_transform(self.X_rus_ros)
        
    def rus_ros_plot(self,X,y,title):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.scatter(X[y==0, 0], X[y==0, 1],alpha=.5, label='Class #0',c="r")
        plt.scatter(X[y==1, 0], X[y==1, 1],alpha=.5, label='Class #1')
        # make nice plotting
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        ax.spines['left'].set_position(('outward', 10))
        ax.spines['bottom'].set_position(('outward', 10))
        ax.set_xlim([-6, 6])
        ax.set_ylim([-6, 6])

        plt.title(title)
        plt.legend()
        plt.tight_layout()
        plt.savefig("./resource/rus_ros_orijinal.png")
    
    def rus_and_ros(self,X,y,X_vis,val):
        if val==0: #rus
            plt.cla()
            rus = RandomUnderSampler(return_indices=True)
            X_resampled, y_resampled, idx_resampled = rus.fit_sample(X, y)
            X_res_vis = self.pca.transform(X_resampled)
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            idx_samples_removed = numpy.setdiff1d(numpy.arange(X_vis.shape[0]),
                                               idx_resampled)
            idx_class_0 = y_resampled == 0
            plt.scatter(X_res_vis[idx_class_0, 0], X_res_vis[idx_class_0, 1],
                        alpha=.5, label='Class #0',c="r")
            plt.scatter(X_res_vis[~idx_class_0, 0], X_res_vis[~idx_class_0, 1],
                        alpha=.5, label='Class #1')
            plt.scatter(X_vis[idx_samples_removed, 0], X_vis[idx_samples_removed, 1],
                        alpha=.1, label='Removed samples',c="g")
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()
            ax.spines['left'].set_position(('outward', 10))
            ax.spines['bottom'].set_position(('outward', 10))
            ax.set_xlim([-6, 6])
            ax.set_ylim([-6, 6])
            plt.title('RUS Method')
            plt.legend()
            plt.tight_layout()
            plt.savefig("./resource/rus.png")
        elif val==1: #ros
            ros = RandomOverSampler()
            X_resampled, y_resampled = ros.fit_sample(X, y)
            X_res_vis = self.pca.transform(X_resampled)
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            plt.scatter(X_res_vis[y_resampled == 0, 0], X_res_vis[y_resampled == 0, 1],label="Class #0", alpha=.5,c='r')
            plt.scatter(X_res_vis[y_resampled == 1, 0], X_res_vis[y_resampled == 1, 1],label="Class #1", alpha=.5)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.get_xaxis().tick_bottom()
            ax.get_yaxis().tick_left()
            ax.spines['left'].set_position(('outward', 10))
            ax.spines['bottom'].set_position(('outward', 10))
            ax.set_xlim([-6, 6])
            ax.set_ylim([-6, 6])
            plt.title('ROS Method')
            plt.legend()
            plt.tight_layout()
            plt.savefig("./resource/ros.png")
        
#---------------RUS VE ROS ------ FONKSİYONLAR---- SON ---------
#============================================================================================================================================================        
#-------------NAVİE BAYES - BASLANGİC ---------------------------------------
    def navie_item_add(self):
        kelime=self.le_navie_kelime.text()
        kategori=self.le_naive_kategori.text()
        kelime=kelime.lower()
        kategori=kategori.lower()
        self.navie_bayes_data_set.append((kelime,kategori))
        self.verileri_tabloya_dok(self.navie_bayes_data_set,self.tbl_navie_data_set)
        self.le_navie_kelime.setText("")
    
    def navie_bayes_siniflandir(self):
        sonuc=NavieBayes.predict(self.le_metin.toPlainText(),NavieBayes.fit(self.navie_bayes_data_set))
        sonuc=sonuc.upper()
        self.lbl_navie_sonuc.setText(sonuc)
        
        
#-------------NAVİE BAYES - SON ---------------------------------------
#============================================================================================================================================================        
#------------NORMALIZASYON BASLANGIC-----------------------

    def norm_data_load(self):
        self.fileName=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Data Dosyası Seçin",".",u"(*.data *.pkl *.txt)"))
        self.tbl_norm_data.clear()
        self.tbl_norm_result.clear()
        if self.fileName:
            f = open(self.fileName)
            self.norm_data=[]
            for i,row in enumerate(f.readlines()):
                currentline = row.split(",")   
                temp=[]
                for column_value in currentline:
                    temp.append(column_value)
        
                self.norm_data.append(temp)
            self.norm_data=numpy.array(self.norm_data)
            if len(self.norm_data[0])!=len(self.norm_data[len(self.norm_data)-1]): #eger son satir ile ilk satirin degeri esit degilse son satiri siliyoruz(iris datada son deger bos)
                self.norm_data=numpy.delete(self.norm_data,[len(self.norm_data)-1]) 
            self.verileri_tabloya_dok(self.norm_data,self.tbl_norm_data)

    
    def normalize_data_save(self):
        save_file_name=unicode(QtGui.QFileDialog.getSaveFileName(self,u"Dosyayı Kaydet",".",u"(*.data)"))
        self.saveData(save_file_name,self.result)

        
    def normalize_uygula(self):
        if self.rb_norm_minmax.isChecked():
            self.result=Normalizasyon.normalizasyon(self.fileName,0)
        elif self.rb_norm_zscore.isChecked():
            self.result=Normalizasyon.normalizasyon(self.fileName,1)
        elif self.rb_norm_median.isChecked():
            self.result=Normalizasyon.normalizasyon(self.fileName,2)
        self.verileri_tabloya_dok(self.result,self.tbl_norm_result)
        
    
#------------NORMALIZASYON SON-----------------------
#============================================================================================================================================================
#----------- Random Forest Baslangic------------------
    def random_forest_data_load(self):
        self.tbl_random_forest_confusionm.clear()
        self.lbl_random_forest_accuraryscore.setText("")
        self.tbl_random_forest_data.clear()
        self.tbl_random_forest_x_test.clear()
        self.tbl_random_forest_x_train.clear()
        self.fileName=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Data Dosyası Seçin",".",u"(*.data *.pkl)"))
        if self.fileName:
            f = open(self.fileName)
            self.rf_data=[]
            for i,row in enumerate(f.readlines()):
                currentline = row.split(",")   
                temp=[]
                for column_value in currentline:
                    temp.append(column_value)
        
                self.rf_data.append(temp)
            self.rf_data=numpy.array(self.rf_data)
            if len(self.rf_data[0])!=len(self.rf_data[len(self.rf_data)-1]): #eger son satir ile ilk satirin degeri esit degilse son satiri siliyoruz(iris datada son deger bos)
                self.rf_data=numpy.delete(self.rf_data,[len(self.rf_data)-1]) 
            self.verileri_tabloya_dok(self.rf_data,self.tbl_random_forest_data)
            
    def random_forest_train_test(self):
        self.tbl_random_forest_confusionm.clear()
        self.lbl_random_forest_accuraryscore.setText("")
        deger=self.random_forest_slider.value()
        t_size=float(deger)/100
        data=numpy.array(self.rf_data)
        a=len(data[0])-1
        X=data[:,:a]
        y=data[:,a]
        self.X_train_random_forest,self.X_test_random_forest,self.y_train_random_forest,self.y_test_random_forest=train_test_split(X,y,test_size=t_size)
        self.verileri_tabloya_dok(self.X_train_random_forest,self.tbl_random_forest_x_train)
        self.verileri_tabloya_dok(self.X_test_random_forest,self.tbl_random_forest_x_test)
    
    def random_forest_uygula(self):
        results=self.RFclassification(self.X_train_random_forest,self.y_train_random_forest,self.X_test_random_forest)
        cm=confusion_matrix(self.y_test_random_forest,results)
        rf_as=(round(accuracy_score(self.y_test_random_forest,results),2))*100
        self.verileri_tabloya_dok(cm,self.tbl_random_forest_confusionm)
        self.lbl_random_forest_accuraryscore.setText("%"+str(rf_as))
        
    def random_forest_slider_changedValue(self):
        deger=self.random_forest_slider.value()
        self.lbl_random_forest_slider.setText(str(deger))
    
    def random_forest_model_save(self):
        save_file_name=unicode(QtGui.QFileDialog.getSaveFileName(self,u"Dosyayı Kaydet",".",u"(*.pkl)"))
        joblib.dump(self.rf_clf,save_file_name)
#----------- Random Forest SON------------------------
#============================================================================================================================================================
#------------Train & Test Baslangic  ---------------
    def train_test_data_load(self):
        self.tbl_train_test_x_train.clear()
        self.tbl_train_test_x_test.clear()
        self.tbl_train_test_y_train.clear()
        self.tbl_train_test_y_test.clear()
        self.fileName=unicode(QtGui.QFileDialog.getOpenFileName(self,u"Data Dosyası Seçin",".",u"(*.data *.pkl)"))
        if self.fileName: #Eger dosya secilmis ise yap
            f = open(self.fileName)
            self.tt_data=[]
            for i,row in enumerate(f.readlines()):
                currentline = row.split(",")   
                temp=[]
                for column_value in currentline:
                    temp.append(column_value)
        
                self.tt_data.append(temp)
            self.tt_data=numpy.array(self.tt_data)
            if len(self.tt_data[0])!=len(self.tt_data[len(self.tt_data)-1]): #eger son satir ile ilk satirin degeri esit degilse son satiri siliyoruz(iris datada son deger bos)
                self.tt_data=numpy.delete(self.tt_data,[len(self.tt_data)-1]) 
            self.verileri_tabloya_dok(self.tt_data,self.tbl_train_test_data)

    def test_and_train_slider_changedValue(self):
        val=self.test_and_train_slider.value()
        self.lbl_train_test.setText("%"+str(val))
        
    def train_test_uygula(self):
        val=self.test_and_train_slider.value()
        t_size=float(val)/100
        data=numpy.array(self.tt_data)
        a=len(data[0])-1
        X=data[:,:a]
        y=data[:,a]
        X_train_tt,X_test_tt,y_train_tt,y_test_tt=train_test_split(X,y,test_size=t_size)
        self.verileri_tabloya_dok(X_train_tt,self.tbl_train_test_x_train)
        self.verileri_tabloya_dok(X_test_tt,self.tbl_train_test_x_test)
        self.verileri_tabloya_dok(y_train_tt,self.tbl_train_test_y_train)
        self.verileri_tabloya_dok(y_test_tt,self.tbl_train_test_y_test)

#------------Train & Test SON ---------------
#============================================================================================================================================================
#-------Parkinson Verileri Global Degiskenlere Ataniyor ----Baslangic------   
    def parkinson_veri(self):

        sst_d=ParkinsonDataSet.readDataFile("./data/parkinson/sst.data")
        dst_d=ParkinsonDataSet.readDataFile("./data/parkinson/dst.data")
        stcp_d=ParkinsonDataSet.readDataFile("./data/parkinson/stcp.data")
        t_sst=ParkinsonDataSet.readDataFile("./data/parkinson/sst_test.data")
        t_dst=ParkinsonDataSet.readDataFile("./data/parkinson/dst_test.data")
        t_stcp=ParkinsonDataSet.readDataFile("./data/parkinson/stcp_test.data")

#Bu bölümde .data uzantısı olmadan verileri klasörden cekebiliyoruz
#        sst_d=numpy.array(SST_Data())
#        dst_d=numpy.array(DST_Data())
#        stcp_d=numpy.array(STCP_Data())
#        t_sst=numpy.array(test_sst())
#        t_dst=numpy.array(test_dst())
#        t_stcp=numpy.array(test_stcp())

        #SST
        self.X_test_sst=t_sst[:,:5]
        self.y_test_sst=t_sst[:,5]
        self.X_train_sst=sst_d[:,:5]
        self.y_train_sst=sst_d[:,5]
        #DST
        self.X_test_dst=t_dst[:,:5]
        self.y_test_dst=t_dst[:,5]
        self.X_train_dst=dst_d[:,:5]
        self.y_train_dst=dst_d[:,5]
        #STCP
        self.X_train_stcp=stcp_d[:,:5]
        self.y_train_stcp=stcp_d[:,5]
        self.X_test_stcp=t_stcp[:,:5]
        self.y_test_stcp=t_stcp[:,5]
#-------Parkinson Verileri Global Degiskenlere Ataniyor ----Son------
#============================================================================================================================================================            
#-------------------- Button Click olaylari ---- Baslangic ----------------------------      

#-----------------RUS VE ROS BUTON OLAYLARI BASLANGİC-----------------
#-------------RUS-ROS--- DATASET OLUSTUR --- BASLANGİC--------
    def rus_ros_dataSet_olustur(self):
        samples=self.rus_ros_n_samples.text()
        val=self.rus_ros_slider.value()
        w1=(100-val)
        w1=float(w1)/100
        w2=1-w1
        self.rus_ros_generate_dataset(samples,w1,w2)
        self.rus_ros_plot(self.X_vis,self.y_rus_ros,"Orijinal Data Set")
        self.rr_w,self.rr_h=self.rus_ros_gv_data.width(),self.rus_ros_gv_data.height()
        self.rus_ros_gv_data.setScene(self.show_image("./resource/rus_ros_orijinal.png",self.rr_w,self.rr_h))
#-------------RUS-ROS--- DATASET OLUSTUR --- SON--------
#--------------------------RUS-ROS -UYGULA---------- BASLANGİC------
    def rus_ros_uygula(self):
        w,h=self.rus_ros_gv_sonuc.width(),self.rus_ros_gv_sonuc.height()
        if self.radiobuton_ros.isChecked():
            self.rus_and_ros(self.X_rus_ros,self.y_rus_ros,self.X_vis,1)
            self.rus_ros_gv_sonuc.setScene(self.show_image("./resource/ros.png",w,h))
        if self.radiobuton_rus.isChecked():
            self.rus_and_ros(self.X_rus_ros,self.y_rus_ros,self.X_vis,0)
            self.rus_ros_gv_sonuc.setScene(self.show_image("./resource/rus.png",w,h))

#--------------------------RUS-ROS -UYGULA---------- SON------
#-----------------RUS VE ROS BUTON OLAYLARI SON-----------------


#-------Parkinson top menu -------- Baslangic -------------
    def parkinson_veri_yukle(self):
        self.parkinson_veri()
        #----SST-----
        self.verileri_tabloya_dok(self.X_train_sst,self.tbl_sst_x_train)
        self.verileri_tabloya_dok(self.y_train_sst,self.tbl_sst_y_train)
        self.verileri_tabloya_dok(self.X_test_sst,self.tbl_sst_x_test)
        #----DST-----
        self.verileri_tabloya_dok(self.X_train_dst,self.tbl_dst_x_train)
        self.verileri_tabloya_dok(self.y_train_dst,self.tbl_dst_y_train)
        self.verileri_tabloya_dok(self.X_test_dst,self.tbl_dst_x_test)
        #----STCP-----
        self.verileri_tabloya_dok(self.X_train_stcp,self.tbl_stcp_x_train)
        self.verileri_tabloya_dok(self.y_train_stcp,self.tbl_stcp_y_train)
        self.verileri_tabloya_dok(self.X_test_stcp,self.tbl_stcp_x_test)
        
    def parkinson_classfication(self):
        #----SST-----
        sst_rf_result=self.RFclassification(self.X_train_sst,self.y_train_sst,self.X_test_sst)
        sst_rf_cm=confusion_matrix(sst_rf_result,self.y_test_sst)
        sst_rf_as=(round(accuracy_score(self.y_test_sst,sst_rf_result),2))*100
        self.verileri_tabloya_dok(sst_rf_cm,self.tbl_sst_rf_cm)
        self.lbl_sst_rf_as.setText("%"+str(sst_rf_as))
        
        sst_dt_result=self.DTclassification(self.X_train_sst,self.y_train_sst,self.X_test_sst)
        sst_dt_cm=confusion_matrix(sst_dt_result,self.y_test_sst)
        sst_dt_as=(round(accuracy_score(self.y_test_sst,sst_dt_result),2))*100
        self.verileri_tabloya_dok(sst_dt_cm,self.tbl_sst_gv_cm)
        self.lbl_sst_gv_as.setText("%"+str(sst_dt_as))
        #----DST-----
        dst_rf_result=self.RFclassification(self.X_train_dst,self.y_train_dst,self.X_test_dst)
        dst_rf_cm=confusion_matrix(dst_rf_result,self.y_test_dst)
        dst_rf_as=(round(accuracy_score(self.y_test_dst,dst_rf_result),2))*100
        self.verileri_tabloya_dok(dst_rf_cm,self.tbl_dst_rf_cm)
        self.lbl_dst_rf_as.setText("%"+str(dst_rf_as))
        
        dst_dt_result=self.DTclassification(self.X_train_dst,self.y_train_dst,self.X_test_dst)
        dst_dt_cm=confusion_matrix(dst_dt_result,self.y_test_dst)
        dst_dt_as=(round(accuracy_score(self.y_test_dst,dst_dt_result),2))*100
        self.verileri_tabloya_dok(dst_dt_cm,self.tbl_dst_gv_cm)
        self.lbl_dst_gv_as.setText("%"+str(dst_dt_as))
        #----STCP-----
        stcp_rf_result=self.RFclassification(self.X_train_stcp,self.y_train_stcp,self.X_test_stcp)
        stcp_rf_cm=confusion_matrix(stcp_rf_result,self.y_test_stcp)
        stcp_rf_as=(round(accuracy_score(self.y_test_stcp,stcp_rf_result),2))*100
        self.verileri_tabloya_dok(stcp_rf_cm,self.tbl_stcp_rf_cm)
        self.lbl_stcp_rf_as.setText("%"+str(stcp_rf_as))
        
        stcp_dt_result=self.DTclassification(self.X_train_stcp,self.y_train_stcp,self.X_test_stcp)
        stcp_dt_cm=confusion_matrix(stcp_dt_result,self.y_test_stcp)
        stcp_dt_as=(round(accuracy_score(self.y_test_stcp,stcp_dt_result),2))*100
        self.verileri_tabloya_dok(stcp_dt_cm,self.tbl_stcp_gv_cm)
        self.lbl_stcp_gv_as.setText("%"+str(stcp_dt_as))
    
#-------Parkinson top menu -------- Son -------------    
    
#-------Parkinson bottom menu ----- baslangic -------    
    def parkinson_all_data(self):
        all_data=ParkinsonDataSet.readDataFile("./data/parkinson/all.data")
#        all_data=numpy.array(allData())
        self.X=all_data[:,:5]
        self.y=all_data[:,5]
        self.verileri_tabloya_dok(all_data,self.tbl_all_data)
        self.pb_parkinson_all_data.setEnabled(False)
        self.pb_parkinson_split.setEnabled(True)
        self.buton_animasyon(self.pb_parkinson_split,100,10,48,48)
    
    def parkinson_train_and_test(self):
        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(self.X,self.y,test_size=0.25)
        self.verileri_tabloya_dok(self.X_train,self.tbl_x_train)
        self.verileri_tabloya_dok(self.X_test,self.tbl_x_test)
        self.pb_parkinson_split.setEnabled(False)
        self.pb_parkinson_class_2.setEnabled(True)
        self.buton_animasyon(self.pb_parkinson_class_2,170,10,48,48)
    
    def parkinson_classfication_2(self):
        #---Random Forest -------- B
        rf_results=self.RFclassification(self.X_train,self.y_train,self.X_test)
        rf_cm=confusion_matrix(rf_results,self.y_test)
        rf_as=(round(accuracy_score(self.y_test,rf_results),2))*100
        self.verileri_tabloya_dok(rf_cm,self.tbl_all_data_rf_cm)
        self.lbl_all_data_rf_as.setText("%"+str(rf_as))
        #---Random Forest -------- S
        #---------Decision Tree --------------B
        gs_results=self.DTclassification(self.X_train,self.y_train,self.X_test)
        gs_cm=confusion_matrix(gs_results,self.y_test)
        gs_as=(round(accuracy_score(self.y_test,gs_results),2))*100
        self.verileri_tabloya_dok(gs_cm,self.tbl_all_data_cd_cm)
        self.lbl_all_data_gv_as.setText("%"+str(gs_as))
#        #---------Decision Tree --------------B
        self.pb_parkinson_class_2.setEnabled(False)
        self.pb_parkinson_reload_split.setEnabled(True)
        self.buton_animasyon(self.pb_parkinson_reload_split,240,10,48,48)
    
    def parkinson_reload(self):
        self.pb_parkinson_reload_split.setEnabled(False)
        self.pb_parkinson_split.setEnabled(True)
        self.lbl_all_data_gv_as.setText("")
        self.lbl_all_data_rf_as.setText("")
        self.tbl_all_data_cd_cm.clear()
        self.tbl_all_data_rf_cm.clear()
        self.tbl_x_test.clear()
        self.tbl_x_train.clear()

#-------Parkinson bottom menu ----- son -------   
        


#-----------KNN - KÜMELEME ----------- BASLANGİC---------
    def knn_cluster_create_dataset(self):
        maxRange=int(self.knn_cluster_max_range.text())
        count=int(self.knn_cluster_count.text())
        self.knn_c_data=KNNCluster.datasetOlustur(maxRange,count)
        self.w,self.h=self.knn_cluster_data.width(),self.knn_cluster_data.height()
        self.knn_cluster_data.setScene(self.show_image("./resource/knn_kume_data.png",self.w,self.h))
        self.verileri_tabloya_dok(self.knn_c_data,self.knn_cluster_tbl)
        
    def knn_cluster(self):
        value=self.knn_cluster_cb.currentIndex()
        KNNCluster.kumele(self.knn_c_data,value)
        self.w,self.h=self.knn_cluster_result.width(),self.knn_cluster_result.height()
        self.knn_cluster_result.setScene(self.show_image("./resource/knn_kume.png",self.w,self.h))

#-----------KNN - KÜMELEME ----------- SON---------

        
    @QtCore.pyqtSignature("bool")
    def on_t1_pb_kumele_clicked(self):
        if self.t1_te_k.toPlainText()!=None and self.t1_te_k.toPlainText()!="" and self.t1_te_x.toPlainText()!=None and self.t1_te_x.toPlainText()!="" and self.t1_te_y.toPlainText()!=None and self.t1_te_y.toPlainText()!="" :
            self.wy,self.hy=self.t1_gv_nokta.width(),self.t1_gv_nokta.height()
            self.yeni_nokta_knn(int(self.t1_te_x.toPlainText()),int(self.t1_te_y.toPlainText()))
            self.t1_gv_nokta.setScene(self.show_image("./resource/knn_new_point.png",self.wy,self.hy))
            self.KNN(int(self.t1_te_k.toPlainText()),int(self.t1_te_x.toPlainText()),int(self.t1_te_y.toPlainText()))
            self.ws,self.hs=self.t1_gv_sonuc.width(),self.t1_gv_sonuc.height()
            self.t1_gv_sonuc.setScene(self.show_image("./resource/knn_sonuc.png",self.ws,self.hs))
#--------- K means Butonlar - Baslangic -------------    
    

        
    @QtCore.pyqtSignature("bool")
    def on_t2_pb_dataload_clicked(self):
        kmeans.plot(self.data_kmeans)
        self.w,self.h=self.t2_gv_data.width(),self.t2_gv_data.height()
        self.t2_gv_data.setScene(self.show_image("./resource/kmeans_ilk.png",self.w,self.h))
    
    @QtCore.pyqtSignature("bool")
    def on_kmeans_pb_ekle_clicked(self):
        x=int(self.kmeans_x.text())
        y=int(self.kmeans_y.text())
        if self.kmeans_etiket.currentIndex()==0:
            etiket="c1"
        elif self.kmeans_etiket.currentIndex()==1:
            etiket="c2"
        self.data_kmeans.append((x,y,etiket))
        self.verileri_tabloya_dok(self.data_kmeans,self.k_means_tbl_data)
    
    @QtCore.pyqtSignature("bool")
    def on_t2_pb_kmeans_clicked(self):
        kmeans.hesapla(self.data_kmeans)
        self.w,self.h=self.t2_gv_sonuc.width(),self.t2_gv_sonuc.height()
        self.t2_gv_sonuc.setScene(self.show_image("./resource/kmeans_son.png",self.w,self.h))
#-------------------- Button Click olaylari ---- SON --------------------------
        
    