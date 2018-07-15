# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasarim.ui'
#
# Created: Tue Jan 02 18:48:48 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        Dialog.setMaximumSize(QtCore.QSize(1280, 720))
        Dialog.setStyleSheet(_fromUtf8("#Dialog{\n"
"background-color:white;}\n"
"QGraphicsView{\n"
"border:2px solid #FF895D}\n"
"QLabel{\n"
"color:#FF895D}\n"
"QGroupBox{\n"
"background-color: white;\n"
"text-align:center;}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}\n"
"QComboBox{\n"
"color:#FF895D;\n"
"background-color:#fff;\n"
"}\n"
"QTableWidget{\n"
"border:2px solid #FF895D;}"))
        self.gb_main_menu = QtGui.QGroupBox(Dialog)
        self.gb_main_menu.setGeometry(QtCore.QRect(0, 50, 200, 670))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gb_main_menu.setFont(font)
        self.gb_main_menu.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"text-align: left;\n"
"padding-left:15px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}\n"
"#gb_main_menu{\n"
"background-color:#FF895D}"))
        self.gb_main_menu.setTitle(_fromUtf8(""))
        self.gb_main_menu.setObjectName(_fromUtf8("gb_main_menu"))
        self.pb_main_menu_1 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_main_menu_1.setGeometry(QtCore.QRect(2, 0, 195, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pb_main_menu_1.setFont(font)
        self.pb_main_menu_1.setObjectName(_fromUtf8("pb_main_menu_1"))
        self.pb_main_menu_2 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_main_menu_2.setGeometry(QtCore.QRect(2, 30, 195, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pb_main_menu_2.setFont(font)
        self.pb_main_menu_2.setObjectName(_fromUtf8("pb_main_menu_2"))
        self.pb_main_menu_3 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_main_menu_3.setGeometry(QtCore.QRect(2, 60, 195, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pb_main_menu_3.setFont(font)
        self.pb_main_menu_3.setObjectName(_fromUtf8("pb_main_menu_3"))
        self.pb_main_menu_4 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_main_menu_4.setGeometry(QtCore.QRect(2, 90, 195, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pb_main_menu_4.setFont(font)
        self.pb_main_menu_4.setObjectName(_fromUtf8("pb_main_menu_4"))
        self.pb_main_menu_5 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_main_menu_5.setGeometry(QtCore.QRect(2, 120, 195, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pb_main_menu_5.setFont(font)
        self.pb_main_menu_5.setObjectName(_fromUtf8("pb_main_menu_5"))
        self.pb_main_menu_6 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_main_menu_6.setGeometry(QtCore.QRect(2, 150, 195, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pb_main_menu_6.setFont(font)
        self.pb_main_menu_6.setObjectName(_fromUtf8("pb_main_menu_6"))
        self.pb_main_menu_7 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_main_menu_7.setGeometry(QtCore.QRect(2, 180, 195, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pb_main_menu_7.setFont(font)
        self.pb_main_menu_7.setObjectName(_fromUtf8("pb_main_menu_7"))
        self.pb_main_menu_8 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_main_menu_8.setGeometry(QtCore.QRect(2, 210, 195, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pb_main_menu_8.setFont(font)
        self.pb_main_menu_8.setObjectName(_fromUtf8("pb_main_menu_8"))
        self.pb_main_menu_9 = QtGui.QPushButton(self.gb_main_menu)
        self.pb_main_menu_9.setGeometry(QtCore.QRect(2, 240, 195, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pb_main_menu_9.setFont(font)
        self.pb_main_menu_9.setObjectName(_fromUtf8("pb_main_menu_9"))
        self.gb_top_menu = QtGui.QGroupBox(Dialog)
        self.gb_top_menu.setGeometry(QtCore.QRect(0, 0, 1280, 51))
        self.gb_top_menu.setStyleSheet(_fromUtf8("#gb_top_menu{\n"
"background-color:#FF895D;\n"
"border:2px solid #FF895D; }"))
        self.gb_top_menu.setTitle(_fromUtf8(""))
        self.gb_top_menu.setObjectName(_fromUtf8("gb_top_menu"))
        self.pb_hamburger_menu = QtGui.QPushButton(self.gb_top_menu)
        self.pb_hamburger_menu.setGeometry(QtCore.QRect(0, 0, 48, 48))
        self.pb_hamburger_menu.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_hamburger_menu.setStyleSheet(_fromUtf8("#pb_hamburger_menu{\n"
"color: grey;\n"
"            border-image: url(./icons/menu.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_hamburger_menu:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/menu_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_hamburger_menu.setText(_fromUtf8(""))
        self.pb_hamburger_menu.setObjectName(_fromUtf8("pb_hamburger_menu"))
        self.gb_knn_sinif = QtGui.QGroupBox(Dialog)
        self.gb_knn_sinif.setGeometry(QtCore.QRect(200, 50, 1080, 670))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.gb_knn_sinif.setFont(font)
        self.gb_knn_sinif.setStyleSheet(_fromUtf8("#gb_knn_sinif{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_knn_sinif::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}\n"
""))
        self.gb_knn_sinif.setObjectName(_fromUtf8("gb_knn_sinif"))
        self.t1_gv_nokta = QtGui.QGraphicsView(self.gb_knn_sinif)
        self.t1_gv_nokta.setGeometry(QtCore.QRect(10, 390, 425, 270))
        self.t1_gv_nokta.setObjectName(_fromUtf8("t1_gv_nokta"))
        self.label = QtGui.QLabel(self.gb_knn_sinif)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.gb_knn_sinif)
        self.label_2.setGeometry(QtCore.QRect(510, 350, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.t1_gv_veriseti = QtGui.QGraphicsView(self.gb_knn_sinif)
        self.t1_gv_veriseti.setGeometry(QtCore.QRect(10, 50, 425, 270))
        self.t1_gv_veriseti.setObjectName(_fromUtf8("t1_gv_veriseti"))
        self.gb_new_point = QtGui.QGroupBox(self.gb_knn_sinif)
        self.gb_new_point.setGeometry(QtCore.QRect(550, 30, 271, 301))
        self.gb_new_point.setTitle(_fromUtf8(""))
        self.gb_new_point.setObjectName(_fromUtf8("gb_new_point"))
        self.t1_te_x = QtGui.QPlainTextEdit(self.gb_new_point)
        self.t1_te_x.setGeometry(QtCore.QRect(190, 90, 51, 31))
        self.t1_te_x.setObjectName(_fromUtf8("t1_te_x"))
        self.label_3 = QtGui.QLabel(self.gb_new_point)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.gb_new_point)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.t1_te_y = QtGui.QPlainTextEdit(self.gb_new_point)
        self.t1_te_y.setGeometry(QtCore.QRect(190, 130, 51, 31))
        self.t1_te_y.setObjectName(_fromUtf8("t1_te_y"))
        self.label_4 = QtGui.QLabel(self.gb_new_point)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.t1_te_k = QtGui.QPlainTextEdit(self.gb_new_point)
        self.t1_te_k.setGeometry(QtCore.QRect(190, 30, 51, 31))
        self.t1_te_k.setObjectName(_fromUtf8("t1_te_k"))
        self.t1_pb_kumele = QtGui.QPushButton(self.gb_new_point)
        self.t1_pb_kumele.setGeometry(QtCore.QRect(50, 180, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.t1_pb_kumele.setFont(font)
        self.t1_pb_kumele.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}"))
        self.t1_pb_kumele.setObjectName(_fromUtf8("t1_pb_kumele"))
        self.label_6 = QtGui.QLabel(self.gb_knn_sinif)
        self.label_6.setGeometry(QtCore.QRect(10, 360, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.t1_gv_sonuc = QtGui.QGraphicsView(self.gb_knn_sinif)
        self.t1_gv_sonuc.setGeometry(QtCore.QRect(510, 390, 425, 270))
        self.t1_gv_sonuc.setObjectName(_fromUtf8("t1_gv_sonuc"))
        self.gb_k_means = QtGui.QGroupBox(Dialog)
        self.gb_k_means.setGeometry(QtCore.QRect(200, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_k_means.setFont(font)
        self.gb_k_means.setStyleSheet(_fromUtf8("#gb_k_means{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_k_means::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}\n"
"QGroupBox{\n"
"background-color: white;\n"
"text-align:center;}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}\n"
"QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}\n"
"QComboBox{\n"
"color:#FF895D;\n"
"background-color:#fff;\n"
"}\n"
"QTableWidget{\n"
"border:2px solid #FF895D;}"))
        self.gb_k_means.setObjectName(_fromUtf8("gb_k_means"))
        self.t2_gv_sonuc = QtGui.QGraphicsView(self.gb_k_means)
        self.t2_gv_sonuc.setGeometry(QtCore.QRect(640, 380, 420, 270))
        self.t2_gv_sonuc.setObjectName(_fromUtf8("t2_gv_sonuc"))
        self.t2_pb_kmeans = QtGui.QPushButton(self.gb_k_means)
        self.t2_pb_kmeans.setGeometry(QtCore.QRect(510, 460, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t2_pb_kmeans.setFont(font)
        self.t2_pb_kmeans.setObjectName(_fromUtf8("t2_pb_kmeans"))
        self.t2_pb_dataload = QtGui.QPushButton(self.gb_k_means)
        self.t2_pb_dataload.setGeometry(QtCore.QRect(370, 270, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t2_pb_dataload.setFont(font)
        self.t2_pb_dataload.setObjectName(_fromUtf8("t2_pb_dataload"))
        self.t2_gv_data = QtGui.QGraphicsView(self.gb_k_means)
        self.t2_gv_data.setGeometry(QtCore.QRect(60, 380, 420, 270))
        self.t2_gv_data.setObjectName(_fromUtf8("t2_gv_data"))
        self.k_means_tbl_data = QtGui.QTableWidget(self.gb_k_means)
        self.k_means_tbl_data.setGeometry(QtCore.QRect(50, 50, 291, 281))
        self.k_means_tbl_data.setObjectName(_fromUtf8("k_means_tbl_data"))
        self.k_means_tbl_data.setColumnCount(0)
        self.k_means_tbl_data.setRowCount(0)
        self.label_37 = QtGui.QLabel(self.gb_k_means)
        self.label_37.setGeometry(QtCore.QRect(50, 35, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.groupBox = QtGui.QGroupBox(self.gb_k_means)
        self.groupBox.setGeometry(QtCore.QRect(370, 50, 221, 191))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_40 = QtGui.QLabel(self.groupBox)
        self.label_40.setGeometry(QtCore.QRect(30, 50, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.kmeans_x = QtGui.QLineEdit(self.groupBox)
        self.kmeans_x.setGeometry(QtCore.QRect(70, 50, 110, 20))
        self.kmeans_x.setObjectName(_fromUtf8("kmeans_x"))
        self.label_41 = QtGui.QLabel(self.groupBox)
        self.label_41.setGeometry(QtCore.QRect(30, 80, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.kmeans_y = QtGui.QLineEdit(self.groupBox)
        self.kmeans_y.setGeometry(QtCore.QRect(70, 80, 110, 20))
        self.kmeans_y.setObjectName(_fromUtf8("kmeans_y"))
        self.kmeans_etiket = QtGui.QComboBox(self.groupBox)
        self.kmeans_etiket.setGeometry(QtCore.QRect(70, 110, 110, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kmeans_etiket.setFont(font)
        self.kmeans_etiket.setObjectName(_fromUtf8("kmeans_etiket"))
        self.kmeans_etiket.addItem(_fromUtf8(""))
        self.kmeans_etiket.addItem(_fromUtf8(""))
        self.kmeans_pb_ekle = QtGui.QPushButton(self.groupBox)
        self.kmeans_pb_ekle.setGeometry(QtCore.QRect(130, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kmeans_pb_ekle.setFont(font)
        self.kmeans_pb_ekle.setObjectName(_fromUtf8("kmeans_pb_ekle"))
        self.gb_rus_ros = QtGui.QGroupBox(Dialog)
        self.gb_rus_ros.setGeometry(QtCore.QRect(200, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_rus_ros.setFont(font)
        self.gb_rus_ros.setStyleSheet(_fromUtf8("#gb_rus_ros{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_rus_ros::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}\n"
"QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}"))
        self.gb_rus_ros.setObjectName(_fromUtf8("gb_rus_ros"))
        self.gb_rus_data_set = QtGui.QGroupBox(self.gb_rus_ros)
        self.gb_rus_data_set.setGeometry(QtCore.QRect(10, 20, 1011, 321))
        self.gb_rus_data_set.setStyleSheet(_fromUtf8("#gb_rus_data_set{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_rus_data_set::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}"))
        self.gb_rus_data_set.setObjectName(_fromUtf8("gb_rus_data_set"))
        self.rus_ros_gv_data = QtGui.QGraphicsView(self.gb_rus_data_set)
        self.rus_ros_gv_data.setGeometry(QtCore.QRect(300, 20, 420, 270))
        self.rus_ros_gv_data.setObjectName(_fromUtf8("rus_ros_gv_data"))
        self.rus_ros_n_samples = QtGui.QLineEdit(self.gb_rus_data_set)
        self.rus_ros_n_samples.setGeometry(QtCore.QRect(40, 70, 161, 20))
        self.rus_ros_n_samples.setObjectName(_fromUtf8("rus_ros_n_samples"))
        self.rus_ros_slider = QtGui.QSlider(self.gb_rus_data_set)
        self.rus_ros_slider.setGeometry(QtCore.QRect(40, 120, 161, 22))
        self.rus_ros_slider.setStyleSheet(_fromUtf8("#rus_ros_slider:groove:horizontall {\n"
"    background: #FF895D;\n"
"    position: absolute;\n"
"    left: 1px; right: 1px;\n"
"}\n"
"#rus_ros_slider:handle:horizontall {\n"
"    height: 10px;\n"
"    background: #1B435D ;\n"
"    margin: 0 4px; /* expand outside the groove */\n"
"}"))
        self.rus_ros_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rus_ros_slider.setObjectName(_fromUtf8("rus_ros_slider"))
        self.lbl_rus_ros_slider = QtGui.QLabel(self.gb_rus_data_set)
        self.lbl_rus_ros_slider.setGeometry(QtCore.QRect(210, 125, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rus_ros_slider.setFont(font)
        self.lbl_rus_ros_slider.setObjectName(_fromUtf8("lbl_rus_ros_slider"))
        self.label_38 = QtGui.QLabel(self.gb_rus_data_set)
        self.label_38.setGeometry(QtCore.QRect(40, 50, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_39 = QtGui.QLabel(self.gb_rus_data_set)
        self.label_39.setGeometry(QtCore.QRect(40, 100, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.rus_ros_pb_create_dataset = QtGui.QPushButton(self.gb_rus_data_set)
        self.rus_ros_pb_create_dataset.setGeometry(QtCore.QRect(40, 170, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rus_ros_pb_create_dataset.setFont(font)
        self.rus_ros_pb_create_dataset.setObjectName(_fromUtf8("rus_ros_pb_create_dataset"))
        self.rus_ros_gv_sonuc = QtGui.QGraphicsView(self.gb_rus_ros)
        self.rus_ros_gv_sonuc.setGeometry(QtCore.QRect(310, 360, 420, 270))
        self.rus_ros_gv_sonuc.setObjectName(_fromUtf8("rus_ros_gv_sonuc"))
        self.radiobuton_rus = QtGui.QRadioButton(self.gb_rus_ros)
        self.radiobuton_rus.setGeometry(QtCore.QRect(60, 420, 131, 17))
        self.radiobuton_rus.setObjectName(_fromUtf8("radiobuton_rus"))
        self.rus_ros_pb = QtGui.QPushButton(self.gb_rus_ros)
        self.rus_ros_pb.setGeometry(QtCore.QRect(60, 510, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rus_ros_pb.setFont(font)
        self.rus_ros_pb.setObjectName(_fromUtf8("rus_ros_pb"))
        self.radiobuton_ros = QtGui.QRadioButton(self.gb_rus_ros)
        self.radiobuton_ros.setGeometry(QtCore.QRect(60, 460, 141, 17))
        self.radiobuton_ros.setObjectName(_fromUtf8("radiobuton_ros"))
        self.gb_knn_kume = QtGui.QGroupBox(Dialog)
        self.gb_knn_kume.setGeometry(QtCore.QRect(200, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_knn_kume.setFont(font)
        self.gb_knn_kume.setStyleSheet(_fromUtf8("#gb_knn_kume{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_knn_kume::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}\n"
"QGroupBox{\n"
"background-color: white;\n"
"text-align:center;}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}\n"
"QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}\n"
"QComboBox{\n"
"color:#FF895D;\n"
"background-color:#fff;\n"
"}\n"
"QTableWidget{\n"
"border:2px solid #FF895D;}"))
        self.gb_knn_kume.setObjectName(_fromUtf8("gb_knn_kume"))
        self.groupBox_2 = QtGui.QGroupBox(self.gb_knn_kume)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 50, 281, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.knn_cluster_max_range = QtGui.QLineEdit(self.groupBox_2)
        self.knn_cluster_max_range.setGeometry(QtCore.QRect(120, 50, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.knn_cluster_max_range.setFont(font)
        self.knn_cluster_max_range.setObjectName(_fromUtf8("knn_cluster_max_range"))
        self.knn_cluster_count = QtGui.QLineEdit(self.groupBox_2)
        self.knn_cluster_count.setGeometry(QtCore.QRect(120, 90, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.knn_cluster_count.setFont(font)
        self.knn_cluster_count.setObjectName(_fromUtf8("knn_cluster_count"))
        self.knn_cluster_pb_create_dataset = QtGui.QPushButton(self.groupBox_2)
        self.knn_cluster_pb_create_dataset.setGeometry(QtCore.QRect(150, 120, 81, 31))
        self.knn_cluster_pb_create_dataset.setObjectName(_fromUtf8("knn_cluster_pb_create_dataset"))
        self.label_42 = QtGui.QLabel(self.groupBox_2)
        self.label_42.setGeometry(QtCore.QRect(20, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_43 = QtGui.QLabel(self.groupBox_2)
        self.label_43.setGeometry(QtCore.QRect(20, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.knn_cluster_data = QtGui.QGraphicsView(self.gb_knn_kume)
        self.knn_cluster_data.setGeometry(QtCore.QRect(470, 50, 420, 270))
        self.knn_cluster_data.setObjectName(_fromUtf8("knn_cluster_data"))
        self.knn_cluster_result = QtGui.QGraphicsView(self.gb_knn_kume)
        self.knn_cluster_result.setGeometry(QtCore.QRect(470, 370, 420, 270))
        self.knn_cluster_result.setObjectName(_fromUtf8("knn_cluster_result"))
        self.knn_pb_cluster = QtGui.QPushButton(self.gb_knn_kume)
        self.knn_pb_cluster.setGeometry(QtCore.QRect(920, 100, 131, 51))
        self.knn_pb_cluster.setObjectName(_fromUtf8("knn_pb_cluster"))
        self.knn_cluster_cb = QtGui.QComboBox(self.gb_knn_kume)
        self.knn_cluster_cb.setGeometry(QtCore.QRect(920, 60, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.knn_cluster_cb.setFont(font)
        self.knn_cluster_cb.setObjectName(_fromUtf8("knn_cluster_cb"))
        self.knn_cluster_cb.addItem(_fromUtf8(""))
        self.knn_cluster_cb.addItem(_fromUtf8(""))
        self.knn_cluster_cb.addItem(_fromUtf8(""))
        self.label_44 = QtGui.QLabel(self.gb_knn_kume)
        self.label_44.setGeometry(QtCore.QRect(470, 30, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.label_45 = QtGui.QLabel(self.gb_knn_kume)
        self.label_45.setGeometry(QtCore.QRect(480, 340, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.knn_cluster_tbl = QtGui.QTableWidget(self.gb_knn_kume)
        self.knn_cluster_tbl.setGeometry(QtCore.QRect(40, 270, 281, 381))
        self.knn_cluster_tbl.setObjectName(_fromUtf8("knn_cluster_tbl"))
        self.knn_cluster_tbl.setColumnCount(0)
        self.knn_cluster_tbl.setRowCount(0)
        self.label_46 = QtGui.QLabel(self.gb_knn_kume)
        self.label_46.setGeometry(QtCore.QRect(40, 250, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.gb_navie = QtGui.QGroupBox(Dialog)
        self.gb_navie.setGeometry(QtCore.QRect(200, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_navie.setFont(font)
        self.gb_navie.setStyleSheet(_fromUtf8("#gb_navie{\n"
"background-color: white;\n"
"text-align:center;}\n"
"#gb_navie::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}"))
        self.gb_navie.setObjectName(_fromUtf8("gb_navie"))
        self.gb_navie_create_dataset = QtGui.QGroupBox(self.gb_navie)
        self.gb_navie_create_dataset.setGeometry(QtCore.QRect(10, 30, 361, 621))
        self.gb_navie_create_dataset.setTitle(_fromUtf8(""))
        self.gb_navie_create_dataset.setObjectName(_fromUtf8("gb_navie_create_dataset"))
        self.tbl_navie_data_set = QtGui.QTableWidget(self.gb_navie_create_dataset)
        self.tbl_navie_data_set.setGeometry(QtCore.QRect(20, 170, 301, 431))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tbl_navie_data_set.setFont(font)
        self.tbl_navie_data_set.setObjectName(_fromUtf8("tbl_navie_data_set"))
        self.tbl_navie_data_set.setColumnCount(0)
        self.tbl_navie_data_set.setRowCount(0)
        self.groupBox_3 = QtGui.QGroupBox(self.gb_navie_create_dataset)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 10, 301, 151))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.le_navie_kelime = QtGui.QLineEdit(self.groupBox_3)
        self.le_navie_kelime.setGeometry(QtCore.QRect(100, 30, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_navie_kelime.setFont(font)
        self.le_navie_kelime.setObjectName(_fromUtf8("le_navie_kelime"))
        self.label_59 = QtGui.QLabel(self.groupBox_3)
        self.label_59.setGeometry(QtCore.QRect(20, 25, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.le_naive_kategori = QtGui.QLineEdit(self.groupBox_3)
        self.le_naive_kategori.setGeometry(QtCore.QRect(100, 65, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_naive_kategori.setFont(font)
        self.le_naive_kategori.setObjectName(_fromUtf8("le_naive_kategori"))
        self.label_60 = QtGui.QLabel(self.groupBox_3)
        self.label_60.setGeometry(QtCore.QRect(20, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.pb_navie_veriekle = QtGui.QPushButton(self.groupBox_3)
        self.pb_navie_veriekle.setGeometry(QtCore.QRect(180, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_navie_veriekle.setFont(font)
        self.pb_navie_veriekle.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}"))
        self.pb_navie_veriekle.setObjectName(_fromUtf8("pb_navie_veriekle"))
        self.groupBox_4 = QtGui.QGroupBox(self.gb_navie)
        self.groupBox_4.setGeometry(QtCore.QRect(390, 20, 671, 631))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_61 = QtGui.QLabel(self.groupBox_4)
        self.label_61.setGeometry(QtCore.QRect(10, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.pb_navie_siniflandir = QtGui.QPushButton(self.groupBox_4)
        self.pb_navie_siniflandir.setGeometry(QtCore.QRect(490, 390, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_navie_siniflandir.setFont(font)
        self.pb_navie_siniflandir.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}"))
        self.pb_navie_siniflandir.setObjectName(_fromUtf8("pb_navie_siniflandir"))
        self.lbl_navie_sonuc = QtGui.QLabel(self.groupBox_4)
        self.lbl_navie_sonuc.setGeometry(QtCore.QRect(160, 400, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_navie_sonuc.setFont(font)
        self.lbl_navie_sonuc.setText(_fromUtf8(""))
        self.lbl_navie_sonuc.setObjectName(_fromUtf8("lbl_navie_sonuc"))
        self.le_metin = QtGui.QPlainTextEdit(self.groupBox_4)
        self.le_metin.setGeometry(QtCore.QRect(10, 60, 631, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_metin.setFont(font)
        self.le_metin.setObjectName(_fromUtf8("le_metin"))
        self.lbl_navie_sonuc_2 = QtGui.QLabel(self.groupBox_4)
        self.lbl_navie_sonuc_2.setGeometry(QtCore.QRect(20, 400, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_navie_sonuc_2.setFont(font)
        self.lbl_navie_sonuc_2.setObjectName(_fromUtf8("lbl_navie_sonuc_2"))
        self.gb_parkinson = QtGui.QGroupBox(Dialog)
        self.gb_parkinson.setGeometry(QtCore.QRect(200, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_parkinson.setFont(font)
        self.gb_parkinson.setStyleSheet(_fromUtf8("#gb_parkinson{\n"
"background-color: white;\n"
"text-align:center;\n"
"background-attachment:scroll;}\n"
"#gb_parkinson::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}\n"
"QTableWidget {\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                stop: 0 #FF92BB, stop: 1 white);\n"
"    border:2px solid #FF895D;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background: #FF895D;\n"
"    border: 2px outset red;\n"
"}\n"
"QScrollArea{\n"
"background:white;}"))
        self.gb_parkinson.setObjectName(_fromUtf8("gb_parkinson"))
        self.scrollArea = QtGui.QScrollArea(self.gb_parkinson)
        self.scrollArea.setGeometry(QtCore.QRect(0, 20, 1080, 2000))
        self.scrollArea.setStyleSheet(_fromUtf8("QGroupBox{\n"
"background-color: white;\n"
"text-align:center;\n"
"background-attachment:scroll;}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"    color: #FF895D;\n"
"}\n"
"QTableWidget {\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                stop: 0 #FF92BB, stop: 1 white);\n"
"    border:2px solid #FF895D;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background: #FF895D;\n"
"    border: 2px outset red;\n"
"}\n"
""))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1078, 4000))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(1078, 4000))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gb_sst = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.gb_sst.setGeometry(QtCore.QRect(0, 70, 1080, 575))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_sst.setFont(font)
        self.gb_sst.setObjectName(_fromUtf8("gb_sst"))
        self.tbl_sst_x_train = QtGui.QTableWidget(self.gb_sst)
        self.tbl_sst_x_train.setGeometry(QtCore.QRect(10, 60, 200, 500))
        self.tbl_sst_x_train.setObjectName(_fromUtf8("tbl_sst_x_train"))
        self.tbl_sst_x_train.setColumnCount(0)
        self.tbl_sst_x_train.setRowCount(0)
        self.label_7 = QtGui.QLabel(self.gb_sst)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tbl_sst_y_train = QtGui.QTableWidget(self.gb_sst)
        self.tbl_sst_y_train.setGeometry(QtCore.QRect(230, 60, 100, 500))
        self.tbl_sst_y_train.setObjectName(_fromUtf8("tbl_sst_y_train"))
        self.tbl_sst_y_train.setColumnCount(0)
        self.tbl_sst_y_train.setRowCount(0)
        self.label_8 = QtGui.QLabel(self.gb_sst)
        self.label_8.setGeometry(QtCore.QRect(230, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tbl_sst_x_test = QtGui.QTableWidget(self.gb_sst)
        self.tbl_sst_x_test.setGeometry(QtCore.QRect(340, 60, 200, 500))
        self.tbl_sst_x_test.setObjectName(_fromUtf8("tbl_sst_x_test"))
        self.tbl_sst_x_test.setColumnCount(0)
        self.tbl_sst_x_test.setRowCount(0)
        self.label_9 = QtGui.QLabel(self.gb_sst)
        self.label_9.setGeometry(QtCore.QRect(340, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tbl_sst_rf_cm = QtGui.QTableWidget(self.gb_sst)
        self.tbl_sst_rf_cm.setGeometry(QtCore.QRect(570, 60, 200, 200))
        self.tbl_sst_rf_cm.setObjectName(_fromUtf8("tbl_sst_rf_cm"))
        self.tbl_sst_rf_cm.setColumnCount(0)
        self.tbl_sst_rf_cm.setRowCount(0)
        self.label_10 = QtGui.QLabel(self.gb_sst)
        self.label_10.setGeometry(QtCore.QRect(570, 300, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.tbl_sst_gv_cm = QtGui.QTableWidget(self.gb_sst)
        self.tbl_sst_gv_cm.setGeometry(QtCore.QRect(570, 320, 200, 200))
        self.tbl_sst_gv_cm.setObjectName(_fromUtf8("tbl_sst_gv_cm"))
        self.tbl_sst_gv_cm.setColumnCount(0)
        self.tbl_sst_gv_cm.setRowCount(0)
        self.label_11 = QtGui.QLabel(self.gb_sst)
        self.label_11.setGeometry(QtCore.QRect(830, 40, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.gb_sst)
        self.label_12.setGeometry(QtCore.QRect(570, 40, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.gb_sst)
        self.label_13.setGeometry(QtCore.QRect(830, 300, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lbl_sst_rf_as = QtGui.QLabel(self.gb_sst)
        self.lbl_sst_rf_as.setGeometry(QtCore.QRect(830, 60, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sst_rf_as.setFont(font)
        self.lbl_sst_rf_as.setText(_fromUtf8(""))
        self.lbl_sst_rf_as.setObjectName(_fromUtf8("lbl_sst_rf_as"))
        self.lbl_sst_gv_as = QtGui.QLabel(self.gb_sst)
        self.lbl_sst_gv_as.setGeometry(QtCore.QRect(830, 330, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sst_gv_as.setFont(font)
        self.lbl_sst_gv_as.setText(_fromUtf8(""))
        self.lbl_sst_gv_as.setObjectName(_fromUtf8("lbl_sst_gv_as"))
        self.gb_buttons = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.gb_buttons.setGeometry(QtCore.QRect(0, 0, 1080, 70))
        self.gb_buttons.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.gb_buttons.setObjectName(_fromUtf8("gb_buttons"))
        self.pb_parkinson_veri_yukle = QtGui.QPushButton(self.gb_buttons)
        self.pb_parkinson_veri_yukle.setGeometry(QtCore.QRect(30, 10, 48, 48))
        self.pb_parkinson_veri_yukle.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_parkinson_veri_yukle.setStyleSheet(_fromUtf8("#pb_parkinson_veri_yukle{\n"
"color: grey;\n"
"            border-image: url(./icons/data_load.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_parkinson_veri_yukle:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/data_load_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_parkinson_veri_yukle.setText(_fromUtf8(""))
        self.pb_parkinson_veri_yukle.setObjectName(_fromUtf8("pb_parkinson_veri_yukle"))
        self.pb_parkinson_class = QtGui.QPushButton(self.gb_buttons)
        self.pb_parkinson_class.setGeometry(QtCore.QRect(120, 10, 48, 48))
        self.pb_parkinson_class.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_parkinson_class.setStyleSheet(_fromUtf8("#pb_parkinson_class{\n"
"color: grey;\n"
"            border-image: url(./icons/class.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_parkinson_class:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/class_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_parkinson_class.setText(_fromUtf8(""))
        self.pb_parkinson_class.setObjectName(_fromUtf8("pb_parkinson_class"))
        self.gb_dst = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.gb_dst.setGeometry(QtCore.QRect(0, 645, 1080, 575))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_dst.setFont(font)
        self.gb_dst.setObjectName(_fromUtf8("gb_dst"))
        self.tbl_dst_rf_cm = QtGui.QTableWidget(self.gb_dst)
        self.tbl_dst_rf_cm.setGeometry(QtCore.QRect(570, 60, 200, 200))
        self.tbl_dst_rf_cm.setObjectName(_fromUtf8("tbl_dst_rf_cm"))
        self.tbl_dst_rf_cm.setColumnCount(0)
        self.tbl_dst_rf_cm.setRowCount(0)
        self.tbl_dst_x_train = QtGui.QTableWidget(self.gb_dst)
        self.tbl_dst_x_train.setGeometry(QtCore.QRect(10, 60, 200, 500))
        self.tbl_dst_x_train.setObjectName(_fromUtf8("tbl_dst_x_train"))
        self.tbl_dst_x_train.setColumnCount(0)
        self.tbl_dst_x_train.setRowCount(0)
        self.label_14 = QtGui.QLabel(self.gb_dst)
        self.label_14.setGeometry(QtCore.QRect(830, 40, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.gb_dst)
        self.label_15.setGeometry(QtCore.QRect(230, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.lbl_dst_rf_as = QtGui.QLabel(self.gb_dst)
        self.lbl_dst_rf_as.setGeometry(QtCore.QRect(830, 60, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_dst_rf_as.setFont(font)
        self.lbl_dst_rf_as.setText(_fromUtf8(""))
        self.lbl_dst_rf_as.setObjectName(_fromUtf8("lbl_dst_rf_as"))
        self.lbl_dst_gv_as = QtGui.QLabel(self.gb_dst)
        self.lbl_dst_gv_as.setGeometry(QtCore.QRect(830, 330, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_dst_gv_as.setFont(font)
        self.lbl_dst_gv_as.setText(_fromUtf8(""))
        self.lbl_dst_gv_as.setObjectName(_fromUtf8("lbl_dst_gv_as"))
        self.tbl_dst_y_train = QtGui.QTableWidget(self.gb_dst)
        self.tbl_dst_y_train.setGeometry(QtCore.QRect(230, 60, 100, 500))
        self.tbl_dst_y_train.setObjectName(_fromUtf8("tbl_dst_y_train"))
        self.tbl_dst_y_train.setColumnCount(0)
        self.tbl_dst_y_train.setRowCount(0)
        self.label_16 = QtGui.QLabel(self.gb_dst)
        self.label_16.setGeometry(QtCore.QRect(830, 300, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.tbl_dst_x_test = QtGui.QTableWidget(self.gb_dst)
        self.tbl_dst_x_test.setGeometry(QtCore.QRect(340, 60, 200, 500))
        self.tbl_dst_x_test.setObjectName(_fromUtf8("tbl_dst_x_test"))
        self.tbl_dst_x_test.setColumnCount(0)
        self.tbl_dst_x_test.setRowCount(0)
        self.label_17 = QtGui.QLabel(self.gb_dst)
        self.label_17.setGeometry(QtCore.QRect(340, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.tbl_dst_gv_cm = QtGui.QTableWidget(self.gb_dst)
        self.tbl_dst_gv_cm.setGeometry(QtCore.QRect(570, 320, 200, 200))
        self.tbl_dst_gv_cm.setObjectName(_fromUtf8("tbl_dst_gv_cm"))
        self.tbl_dst_gv_cm.setColumnCount(0)
        self.tbl_dst_gv_cm.setRowCount(0)
        self.label_18 = QtGui.QLabel(self.gb_dst)
        self.label_18.setGeometry(QtCore.QRect(10, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.gb_dst)
        self.label_19.setGeometry(QtCore.QRect(570, 40, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.gb_dst)
        self.label_20.setGeometry(QtCore.QRect(570, 300, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gb_stcp = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.gb_stcp.setGeometry(QtCore.QRect(0, 1220, 1080, 575))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_stcp.setFont(font)
        self.gb_stcp.setObjectName(_fromUtf8("gb_stcp"))
        self.tbl_stcp_x_train = QtGui.QTableWidget(self.gb_stcp)
        self.tbl_stcp_x_train.setGeometry(QtCore.QRect(10, 60, 200, 500))
        self.tbl_stcp_x_train.setObjectName(_fromUtf8("tbl_stcp_x_train"))
        self.tbl_stcp_x_train.setColumnCount(0)
        self.tbl_stcp_x_train.setRowCount(0)
        self.label_21 = QtGui.QLabel(self.gb_stcp)
        self.label_21.setGeometry(QtCore.QRect(10, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.tbl_stcp_y_train = QtGui.QTableWidget(self.gb_stcp)
        self.tbl_stcp_y_train.setGeometry(QtCore.QRect(230, 60, 100, 500))
        self.tbl_stcp_y_train.setObjectName(_fromUtf8("tbl_stcp_y_train"))
        self.tbl_stcp_y_train.setColumnCount(0)
        self.tbl_stcp_y_train.setRowCount(0)
        self.label_22 = QtGui.QLabel(self.gb_stcp)
        self.label_22.setGeometry(QtCore.QRect(230, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.tbl_stcp_x_test = QtGui.QTableWidget(self.gb_stcp)
        self.tbl_stcp_x_test.setGeometry(QtCore.QRect(340, 60, 200, 500))
        self.tbl_stcp_x_test.setObjectName(_fromUtf8("tbl_stcp_x_test"))
        self.tbl_stcp_x_test.setColumnCount(0)
        self.tbl_stcp_x_test.setRowCount(0)
        self.label_23 = QtGui.QLabel(self.gb_stcp)
        self.label_23.setGeometry(QtCore.QRect(340, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.tbl_stcp_rf_cm = QtGui.QTableWidget(self.gb_stcp)
        self.tbl_stcp_rf_cm.setGeometry(QtCore.QRect(570, 60, 200, 200))
        self.tbl_stcp_rf_cm.setObjectName(_fromUtf8("tbl_stcp_rf_cm"))
        self.tbl_stcp_rf_cm.setColumnCount(0)
        self.tbl_stcp_rf_cm.setRowCount(0)
        self.label_24 = QtGui.QLabel(self.gb_stcp)
        self.label_24.setGeometry(QtCore.QRect(570, 300, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.tbl_stcp_gv_cm = QtGui.QTableWidget(self.gb_stcp)
        self.tbl_stcp_gv_cm.setGeometry(QtCore.QRect(570, 320, 200, 200))
        self.tbl_stcp_gv_cm.setObjectName(_fromUtf8("tbl_stcp_gv_cm"))
        self.tbl_stcp_gv_cm.setColumnCount(0)
        self.tbl_stcp_gv_cm.setRowCount(0)
        self.label_25 = QtGui.QLabel(self.gb_stcp)
        self.label_25.setGeometry(QtCore.QRect(830, 40, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.gb_stcp)
        self.label_26.setGeometry(QtCore.QRect(570, 40, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.gb_stcp)
        self.label_27.setGeometry(QtCore.QRect(830, 300, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.lbl_stcp_rf_as = QtGui.QLabel(self.gb_stcp)
        self.lbl_stcp_rf_as.setGeometry(QtCore.QRect(830, 60, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_stcp_rf_as.setFont(font)
        self.lbl_stcp_rf_as.setText(_fromUtf8(""))
        self.lbl_stcp_rf_as.setObjectName(_fromUtf8("lbl_stcp_rf_as"))
        self.lbl_stcp_gv_as = QtGui.QLabel(self.gb_stcp)
        self.lbl_stcp_gv_as.setGeometry(QtCore.QRect(830, 330, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_stcp_gv_as.setFont(font)
        self.lbl_stcp_gv_as.setText(_fromUtf8(""))
        self.lbl_stcp_gv_as.setObjectName(_fromUtf8("lbl_stcp_gv_as"))
        self.gb_all_data = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.gb_all_data.setGeometry(QtCore.QRect(0, 1860, 1080, 575))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_all_data.setFont(font)
        self.gb_all_data.setObjectName(_fromUtf8("gb_all_data"))
        self.tbl_all_data = QtGui.QTableWidget(self.gb_all_data)
        self.tbl_all_data.setGeometry(QtCore.QRect(10, 60, 200, 500))
        self.tbl_all_data.setObjectName(_fromUtf8("tbl_all_data"))
        self.tbl_all_data.setColumnCount(0)
        self.tbl_all_data.setRowCount(0)
        self.label_28 = QtGui.QLabel(self.gb_all_data)
        self.label_28.setGeometry(QtCore.QRect(10, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.tbl_x_train = QtGui.QTableWidget(self.gb_all_data)
        self.tbl_x_train.setGeometry(QtCore.QRect(230, 60, 200, 500))
        self.tbl_x_train.setObjectName(_fromUtf8("tbl_x_train"))
        self.tbl_x_train.setColumnCount(0)
        self.tbl_x_train.setRowCount(0)
        self.label_29 = QtGui.QLabel(self.gb_all_data)
        self.label_29.setGeometry(QtCore.QRect(230, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.tbl_x_test = QtGui.QTableWidget(self.gb_all_data)
        self.tbl_x_test.setGeometry(QtCore.QRect(440, 60, 200, 500))
        self.tbl_x_test.setObjectName(_fromUtf8("tbl_x_test"))
        self.tbl_x_test.setColumnCount(0)
        self.tbl_x_test.setRowCount(0)
        self.label_30 = QtGui.QLabel(self.gb_all_data)
        self.label_30.setGeometry(QtCore.QRect(440, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.tbl_all_data_rf_cm = QtGui.QTableWidget(self.gb_all_data)
        self.tbl_all_data_rf_cm.setGeometry(QtCore.QRect(680, 60, 200, 200))
        self.tbl_all_data_rf_cm.setObjectName(_fromUtf8("tbl_all_data_rf_cm"))
        self.tbl_all_data_rf_cm.setColumnCount(0)
        self.tbl_all_data_rf_cm.setRowCount(0)
        self.label_31 = QtGui.QLabel(self.gb_all_data)
        self.label_31.setGeometry(QtCore.QRect(680, 290, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.tbl_all_data_cd_cm = QtGui.QTableWidget(self.gb_all_data)
        self.tbl_all_data_cd_cm.setGeometry(QtCore.QRect(680, 310, 200, 200))
        self.tbl_all_data_cd_cm.setObjectName(_fromUtf8("tbl_all_data_cd_cm"))
        self.tbl_all_data_cd_cm.setColumnCount(0)
        self.tbl_all_data_cd_cm.setRowCount(0)
        self.label_32 = QtGui.QLabel(self.gb_all_data)
        self.label_32.setGeometry(QtCore.QRect(910, 40, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(self.gb_all_data)
        self.label_33.setGeometry(QtCore.QRect(680, 40, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.gb_all_data)
        self.label_34.setGeometry(QtCore.QRect(920, 300, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.lbl_all_data_rf_as = QtGui.QLabel(self.gb_all_data)
        self.lbl_all_data_rf_as.setGeometry(QtCore.QRect(910, 60, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_all_data_rf_as.setFont(font)
        self.lbl_all_data_rf_as.setText(_fromUtf8(""))
        self.lbl_all_data_rf_as.setObjectName(_fromUtf8("lbl_all_data_rf_as"))
        self.lbl_all_data_gv_as = QtGui.QLabel(self.gb_all_data)
        self.lbl_all_data_gv_as.setGeometry(QtCore.QRect(920, 320, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_all_data_gv_as.setFont(font)
        self.lbl_all_data_gv_as.setText(_fromUtf8(""))
        self.lbl_all_data_gv_as.setObjectName(_fromUtf8("lbl_all_data_gv_as"))
        self.label_35 = QtGui.QLabel(self.gb_all_data)
        self.label_35.setGeometry(QtCore.QRect(820, 20, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.gb_all_data)
        self.label_36.setGeometry(QtCore.QRect(820, 270, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gb_parkinson_bottom_menu = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.gb_parkinson_bottom_menu.setGeometry(QtCore.QRect(0, 1790, 1080, 70))
        self.gb_parkinson_bottom_menu.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.gb_parkinson_bottom_menu.setObjectName(_fromUtf8("gb_parkinson_bottom_menu"))
        self.pb_parkinson_all_data = QtGui.QPushButton(self.gb_parkinson_bottom_menu)
        self.pb_parkinson_all_data.setGeometry(QtCore.QRect(30, 10, 48, 48))
        self.pb_parkinson_all_data.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_parkinson_all_data.setStyleSheet(_fromUtf8("#pb_parkinson_all_data{\n"
"color: grey;\n"
"            border-image: url(./icons/data_load.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_parkinson_all_data:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/data_load_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_parkinson_all_data.setText(_fromUtf8(""))
        self.pb_parkinson_all_data.setObjectName(_fromUtf8("pb_parkinson_all_data"))
        self.pb_parkinson_class_2 = QtGui.QPushButton(self.gb_parkinson_bottom_menu)
        self.pb_parkinson_class_2.setGeometry(QtCore.QRect(170, 10, 0, 0))
        self.pb_parkinson_class_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_parkinson_class_2.setStyleSheet(_fromUtf8("#pb_parkinson_class_2{\n"
"color: grey;\n"
"            border-image: url(./icons/class.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_parkinson_class_2:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/class_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_parkinson_class_2.setText(_fromUtf8(""))
        self.pb_parkinson_class_2.setObjectName(_fromUtf8("pb_parkinson_class_2"))
        self.pb_parkinson_split = QtGui.QPushButton(self.gb_parkinson_bottom_menu)
        self.pb_parkinson_split.setGeometry(QtCore.QRect(100, 10, 0, 0))
        self.pb_parkinson_split.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_parkinson_split.setStyleSheet(_fromUtf8("#pb_parkinson_split{\n"
"color: grey;\n"
"            border-image: url(./icons/split.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_parkinson_split:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/split_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_parkinson_split.setText(_fromUtf8(""))
        self.pb_parkinson_split.setObjectName(_fromUtf8("pb_parkinson_split"))
        self.pb_parkinson_reload_split = QtGui.QPushButton(self.gb_parkinson_bottom_menu)
        self.pb_parkinson_reload_split.setGeometry(QtCore.QRect(240, 10, 0, 0))
        self.pb_parkinson_reload_split.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_parkinson_reload_split.setStyleSheet(_fromUtf8("#pb_parkinson_reload_split{\n"
"color: grey;\n"
"            border-image: url(./icons/reload.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_parkinson_reload_split:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/reload_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_parkinson_reload_split.setText(_fromUtf8(""))
        self.pb_parkinson_reload_split.setObjectName(_fromUtf8("pb_parkinson_reload_split"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gb_normalizasyon = QtGui.QGroupBox(Dialog)
        self.gb_normalizasyon.setGeometry(QtCore.QRect(200, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_normalizasyon.setFont(font)
        self.gb_normalizasyon.setObjectName(_fromUtf8("gb_normalizasyon"))
        self.pb_normalizasyon_dataload = QtGui.QPushButton(self.gb_normalizasyon)
        self.pb_normalizasyon_dataload.setGeometry(QtCore.QRect(330, 50, 48, 48))
        self.pb_normalizasyon_dataload.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_normalizasyon_dataload.setStyleSheet(_fromUtf8("#pb_normalizasyon_dataload{\n"
"color: grey;\n"
"            border-image: url(./icons/data_load.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_normalizasyon_dataload:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/data_load_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_normalizasyon_dataload.setText(_fromUtf8(""))
        self.pb_normalizasyon_dataload.setObjectName(_fromUtf8("pb_normalizasyon_dataload"))
        self.tbl_norm_data = QtGui.QTableWidget(self.gb_normalizasyon)
        self.tbl_norm_data.setGeometry(QtCore.QRect(30, 100, 351, 481))
        self.tbl_norm_data.setObjectName(_fromUtf8("tbl_norm_data"))
        self.tbl_norm_data.setColumnCount(0)
        self.tbl_norm_data.setRowCount(0)
        self.tbl_norm_result = QtGui.QTableWidget(self.gb_normalizasyon)
        self.tbl_norm_result.setGeometry(QtCore.QRect(650, 100, 351, 481))
        self.tbl_norm_result.setObjectName(_fromUtf8("tbl_norm_result"))
        self.tbl_norm_result.setColumnCount(0)
        self.tbl_norm_result.setRowCount(0)
        self.pb_normalize = QtGui.QPushButton(self.gb_normalizasyon)
        self.pb_normalize.setGeometry(QtCore.QRect(450, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_normalize.setFont(font)
        self.pb_normalize.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}"))
        self.pb_normalize.setObjectName(_fromUtf8("pb_normalize"))
        self.gb_norm_options = QtGui.QGroupBox(self.gb_normalizasyon)
        self.gb_norm_options.setGeometry(QtCore.QRect(420, 160, 181, 151))
        self.gb_norm_options.setTitle(_fromUtf8(""))
        self.gb_norm_options.setObjectName(_fromUtf8("gb_norm_options"))
        self.rb_norm_minmax = QtGui.QRadioButton(self.gb_norm_options)
        self.rb_norm_minmax.setGeometry(QtCore.QRect(40, 30, 82, 17))
        self.rb_norm_minmax.setObjectName(_fromUtf8("rb_norm_minmax"))
        self.rb_norm_zscore = QtGui.QRadioButton(self.gb_norm_options)
        self.rb_norm_zscore.setGeometry(QtCore.QRect(40, 70, 82, 17))
        self.rb_norm_zscore.setObjectName(_fromUtf8("rb_norm_zscore"))
        self.rb_norm_median = QtGui.QRadioButton(self.gb_norm_options)
        self.rb_norm_median.setGeometry(QtCore.QRect(40, 110, 82, 17))
        self.rb_norm_median.setObjectName(_fromUtf8("rb_norm_median"))
        self.pb_normalizasyon_datasave = QtGui.QPushButton(self.gb_normalizasyon)
        self.pb_normalizasyon_datasave.setGeometry(QtCore.QRect(950, 50, 48, 48))
        self.pb_normalizasyon_datasave.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_normalizasyon_datasave.setStyleSheet(_fromUtf8("#pb_normalizasyon_datasave{\n"
"color: grey;\n"
"            border-image: url(./icons/save.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_normalizasyon_datasave:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/save_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_normalizasyon_datasave.setText(_fromUtf8(""))
        self.pb_normalizasyon_datasave.setObjectName(_fromUtf8("pb_normalizasyon_datasave"))
        self.gb_randomforest = QtGui.QGroupBox(Dialog)
        self.gb_randomforest.setGeometry(QtCore.QRect(200, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_randomforest.setFont(font)
        self.gb_randomforest.setObjectName(_fromUtf8("gb_randomforest"))
        self.pb_random_forest_data_load = QtGui.QPushButton(self.gb_randomforest)
        self.pb_random_forest_data_load.setGeometry(QtCore.QRect(260, 40, 48, 48))
        self.pb_random_forest_data_load.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_random_forest_data_load.setStyleSheet(_fromUtf8("#pb_random_forest_data_load{\n"
"color: grey;\n"
"            border-image: url(./icons/data_load.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_random_forest_data_load:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/data_load_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_random_forest_data_load.setText(_fromUtf8(""))
        self.pb_random_forest_data_load.setObjectName(_fromUtf8("pb_random_forest_data_load"))
        self.tbl_random_forest_data = QtGui.QTableWidget(self.gb_randomforest)
        self.tbl_random_forest_data.setGeometry(QtCore.QRect(30, 90, 281, 501))
        self.tbl_random_forest_data.setObjectName(_fromUtf8("tbl_random_forest_data"))
        self.tbl_random_forest_data.setColumnCount(0)
        self.tbl_random_forest_data.setRowCount(0)
        self.tbl_random_forest_x_train = QtGui.QTableWidget(self.gb_randomforest)
        self.tbl_random_forest_x_train.setGeometry(QtCore.QRect(330, 90, 231, 501))
        self.tbl_random_forest_x_train.setObjectName(_fromUtf8("tbl_random_forest_x_train"))
        self.tbl_random_forest_x_train.setColumnCount(0)
        self.tbl_random_forest_x_train.setRowCount(0)
        self.tbl_random_forest_x_test = QtGui.QTableWidget(self.gb_randomforest)
        self.tbl_random_forest_x_test.setGeometry(QtCore.QRect(580, 90, 231, 501))
        self.tbl_random_forest_x_test.setObjectName(_fromUtf8("tbl_random_forest_x_test"))
        self.tbl_random_forest_x_test.setColumnCount(0)
        self.tbl_random_forest_x_test.setRowCount(0)
        self.tbl_random_forest_confusionm = QtGui.QTableWidget(self.gb_randomforest)
        self.tbl_random_forest_confusionm.setGeometry(QtCore.QRect(840, 390, 221, 191))
        self.tbl_random_forest_confusionm.setObjectName(_fromUtf8("tbl_random_forest_confusionm"))
        self.tbl_random_forest_confusionm.setColumnCount(0)
        self.tbl_random_forest_confusionm.setRowCount(0)
        self.label_47 = QtGui.QLabel(self.gb_randomforest)
        self.label_47.setGeometry(QtCore.QRect(840, 370, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.label_48 = QtGui.QLabel(self.gb_randomforest)
        self.label_48.setGeometry(QtCore.QRect(840, 320, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.lbl_random_forest_accuraryscore = QtGui.QLabel(self.gb_randomforest)
        self.lbl_random_forest_accuraryscore.setGeometry(QtCore.QRect(970, 320, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_random_forest_accuraryscore.setFont(font)
        self.lbl_random_forest_accuraryscore.setText(_fromUtf8(""))
        self.lbl_random_forest_accuraryscore.setObjectName(_fromUtf8("lbl_random_forest_accuraryscore"))
        self.pb_random_forest = QtGui.QPushButton(self.gb_randomforest)
        self.pb_random_forest.setGeometry(QtCore.QRect(840, 250, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_random_forest.setFont(font)
        self.pb_random_forest.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}"))
        self.pb_random_forest.setObjectName(_fromUtf8("pb_random_forest"))
        self.pb_random_forest_modelsave = QtGui.QPushButton(self.gb_randomforest)
        self.pb_random_forest_modelsave.setGeometry(QtCore.QRect(1010, 590, 48, 48))
        self.pb_random_forest_modelsave.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_random_forest_modelsave.setStyleSheet(_fromUtf8("#pb_random_forest_modelsave{\n"
"color: grey;\n"
"            border-image: url(./icons/save.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_random_forest_modelsave:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/save_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_random_forest_modelsave.setText(_fromUtf8(""))
        self.pb_random_forest_modelsave.setObjectName(_fromUtf8("pb_random_forest_modelsave"))
        self.label_49 = QtGui.QLabel(self.gb_randomforest)
        self.label_49.setGeometry(QtCore.QRect(30, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.label_50 = QtGui.QLabel(self.gb_randomforest)
        self.label_50.setGeometry(QtCore.QRect(330, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.label_51 = QtGui.QLabel(self.gb_randomforest)
        self.label_51.setGeometry(QtCore.QRect(580, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.pb_random_forest_tandt = QtGui.QPushButton(self.gb_randomforest)
        self.pb_random_forest_tandt.setGeometry(QtCore.QRect(840, 192, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_random_forest_tandt.setFont(font)
        self.pb_random_forest_tandt.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}"))
        self.pb_random_forest_tandt.setObjectName(_fromUtf8("pb_random_forest_tandt"))
        self.random_forest_slider = QtGui.QSlider(self.gb_randomforest)
        self.random_forest_slider.setGeometry(QtCore.QRect(840, 150, 161, 22))
        self.random_forest_slider.setStyleSheet(_fromUtf8("#random_forest_slider:groove:horizontall {\n"
"    background: #FF895D;\n"
"    position: absolute;\n"
"    left: 1px; right: 1px;\n"
"}\n"
"#random_forest_slider:handle:horizontall {\n"
"    height: 10px;\n"
"    background: #1B435D ;\n"
"    margin: 0 4px; /* expand outside the groove */\n"
"}"))
        self.random_forest_slider.setOrientation(QtCore.Qt.Horizontal)
        self.random_forest_slider.setObjectName(_fromUtf8("random_forest_slider"))
        self.lbl_random_forest_slider = QtGui.QLabel(self.gb_randomforest)
        self.lbl_random_forest_slider.setGeometry(QtCore.QRect(1010, 150, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_random_forest_slider.setFont(font)
        self.lbl_random_forest_slider.setObjectName(_fromUtf8("lbl_random_forest_slider"))
        self.label_52 = QtGui.QLabel(self.gb_randomforest)
        self.label_52.setGeometry(QtCore.QRect(840, 120, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.gb_train_test = QtGui.QGroupBox(Dialog)
        self.gb_train_test.setGeometry(QtCore.QRect(200, 50, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_train_test.setFont(font)
        self.gb_train_test.setObjectName(_fromUtf8("gb_train_test"))
        self.pb_train_and_test = QtGui.QPushButton(self.gb_train_test)
        self.pb_train_and_test.setGeometry(QtCore.QRect(30, 572, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb_train_and_test.setFont(font)
        self.pb_train_and_test.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: #FF895D;\n"
"color: #fff;\n"
"border-radius:1px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#1B435D;\n"
"color: #D5EEFF;\n"
"}"))
        self.pb_train_and_test.setObjectName(_fromUtf8("pb_train_and_test"))
        self.tbl_train_test_data = QtGui.QTableWidget(self.gb_train_test)
        self.tbl_train_test_data.setGeometry(QtCore.QRect(20, 60, 281, 421))
        self.tbl_train_test_data.setObjectName(_fromUtf8("tbl_train_test_data"))
        self.tbl_train_test_data.setColumnCount(0)
        self.tbl_train_test_data.setRowCount(0)
        self.tbl_train_test_x_train = QtGui.QTableWidget(self.gb_train_test)
        self.tbl_train_test_x_train.setGeometry(QtCore.QRect(320, 60, 250, 600))
        self.tbl_train_test_x_train.setObjectName(_fromUtf8("tbl_train_test_x_train"))
        self.tbl_train_test_x_train.setColumnCount(0)
        self.tbl_train_test_x_train.setRowCount(0)
        self.lbl_train_test = QtGui.QLabel(self.gb_train_test)
        self.lbl_train_test.setGeometry(QtCore.QRect(200, 530, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_train_test.setFont(font)
        self.lbl_train_test.setObjectName(_fromUtf8("lbl_train_test"))
        self.label_53 = QtGui.QLabel(self.gb_train_test)
        self.label_53.setGeometry(QtCore.QRect(20, 40, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.test_and_train_slider = QtGui.QSlider(self.gb_train_test)
        self.test_and_train_slider.setGeometry(QtCore.QRect(30, 530, 161, 22))
        self.test_and_train_slider.setStyleSheet(_fromUtf8("#test_and_train_slider:groove:horizontall {\n"
"    background: #FF895D;\n"
"    position: absolute;\n"
"    left: 1px; right: 1px;\n"
"}\n"
"#test_and_train_slider:handle:horizontall {\n"
"    height: 10px;\n"
"    background: #1B435D ;\n"
"    margin: 0 4px; /* expand outside the groove */\n"
"}"))
        self.test_and_train_slider.setPageStep(5)
        self.test_and_train_slider.setOrientation(QtCore.Qt.Horizontal)
        self.test_and_train_slider.setObjectName(_fromUtf8("test_and_train_slider"))
        self.label_54 = QtGui.QLabel(self.gb_train_test)
        self.label_54.setGeometry(QtCore.QRect(30, 500, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.pb_train_test_data_load = QtGui.QPushButton(self.gb_train_test)
        self.pb_train_test_data_load.setGeometry(QtCore.QRect(250, 10, 48, 48))
        self.pb_train_test_data_load.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pb_train_test_data_load.setStyleSheet(_fromUtf8("#pb_train_test_data_load{\n"
"color: grey;\n"
"            border-image: url(./icons/data_load.png) 3 10 3 10;\n"
"            border-top: 3px transparent;\n"
"            border-bottom: 3px transparent;\n"
"            border-right: 10px transparent;\n"
"            border-left: 10px transparent;}\n"
"\n"
"#pb_train_test_data_load:hover{\n"
"color: grey;\n"
"            border-image: url(./icons/data_load_hover.png) 5 12 5 12;\n"
"            border-top: 5px transparent;\n"
"            border-bottom: 5px transparent;\n"
"            border-right: 12px transparent;\n"
"            border-left: 12px transparent;}\n"
""))
        self.pb_train_test_data_load.setText(_fromUtf8(""))
        self.pb_train_test_data_load.setObjectName(_fromUtf8("pb_train_test_data_load"))
        self.label_55 = QtGui.QLabel(self.gb_train_test)
        self.label_55.setGeometry(QtCore.QRect(320, 40, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.tbl_train_test_y_train = QtGui.QTableWidget(self.gb_train_test)
        self.tbl_train_test_y_train.setGeometry(QtCore.QRect(580, 60, 100, 600))
        self.tbl_train_test_y_train.setObjectName(_fromUtf8("tbl_train_test_y_train"))
        self.tbl_train_test_y_train.setColumnCount(0)
        self.tbl_train_test_y_train.setRowCount(0)
        self.label_56 = QtGui.QLabel(self.gb_train_test)
        self.label_56.setGeometry(QtCore.QRect(580, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.label_57 = QtGui.QLabel(self.gb_train_test)
        self.label_57.setGeometry(QtCore.QRect(690, 40, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.label_58 = QtGui.QLabel(self.gb_train_test)
        self.label_58.setGeometry(QtCore.QRect(950, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.tbl_train_test_x_test = QtGui.QTableWidget(self.gb_train_test)
        self.tbl_train_test_x_test.setGeometry(QtCore.QRect(690, 60, 250, 600))
        self.tbl_train_test_x_test.setObjectName(_fromUtf8("tbl_train_test_x_test"))
        self.tbl_train_test_x_test.setColumnCount(0)
        self.tbl_train_test_x_test.setRowCount(0)
        self.tbl_train_test_y_test = QtGui.QTableWidget(self.gb_train_test)
        self.tbl_train_test_y_test.setGeometry(QtCore.QRect(950, 60, 100, 600))
        self.tbl_train_test_y_test.setObjectName(_fromUtf8("tbl_train_test_y_test"))
        self.tbl_train_test_y_test.setColumnCount(0)
        self.tbl_train_test_y_test.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "134410010 Bedirhan Sağlam Makine Öğrenmesi Ödev", None))
        self.pb_main_menu_1.setText(_translate("Dialog", "KNN ile Sınıflandırma", None))
        self.pb_main_menu_2.setText(_translate("Dialog", "RUS Ve ROS Method", None))
        self.pb_main_menu_3.setText(_translate("Dialog", "K-Means ile Kümeleme", None))
        self.pb_main_menu_4.setText(_translate("Dialog", "KNN ile Kümeleme", None))
        self.pb_main_menu_5.setText(_translate("Dialog", "Navie Bayes", None))
        self.pb_main_menu_6.setText(_translate("Dialog", "Normalizasyon", None))
        self.pb_main_menu_7.setText(_translate("Dialog", "Random Forest", None))
        self.pb_main_menu_8.setText(_translate("Dialog", "Train and Test Split", None))
        self.pb_main_menu_9.setText(_translate("Dialog", "Parkinson", None))
        self.gb_knn_sinif.setTitle(_translate("Dialog", "KNN İLE SINIFLANDIRMA", None))
        self.label.setText(_translate("Dialog", "Veri Seti", None))
        self.label_2.setText(_translate("Dialog", "Sonuç :", None))
        self.label_3.setText(_translate("Dialog", "K değerini giriniz :", None))
        self.label_5.setText(_translate("Dialog", "y değerini giriniz :", None))
        self.label_4.setText(_translate("Dialog", "x değerini giriniz :", None))
        self.t1_pb_kumele.setText(_translate("Dialog", "SINIFLANDIR", None))
        self.label_6.setText(_translate("Dialog", "Girilen Yeni Nokta", None))
        self.gb_k_means.setTitle(_translate("Dialog", "K-Means ile Kümeleme", None))
        self.t2_pb_kmeans.setText(_translate("Dialog", "KÜMELE", None))
        self.t2_pb_dataload.setText(_translate("Dialog", "Verileri Yükle", None))
        self.label_37.setText(_translate("Dialog", "Veri Seti :", None))
        self.groupBox.setTitle(_translate("Dialog", "Verisetine Yeni Eleman Ekle", None))
        self.label_40.setText(_translate("Dialog", "X :", None))
        self.label_41.setText(_translate("Dialog", "Y :", None))
        self.kmeans_etiket.setItemText(0, _translate("Dialog", "c1", None))
        self.kmeans_etiket.setItemText(1, _translate("Dialog", "c2", None))
        self.kmeans_pb_ekle.setText(_translate("Dialog", "Ekle", None))
        self.gb_rus_ros.setTitle(_translate("Dialog", "RUS ve ROS Method", None))
        self.gb_rus_data_set.setTitle(_translate("Dialog", "Dataset Oluştur", None))
        self.lbl_rus_ros_slider.setText(_translate("Dialog", "0", None))
        self.label_38.setText(_translate("Dialog", "Örnek Sayısı :", None))
        self.label_39.setText(_translate("Dialog", "Yüzde Dağılımı :", None))
        self.rus_ros_pb_create_dataset.setText(_translate("Dialog", "Veri Seti Oluştur", None))
        self.radiobuton_rus.setText(_translate("Dialog", "RUS", None))
        self.rus_ros_pb.setText(_translate("Dialog", "Uygula", None))
        self.radiobuton_ros.setText(_translate("Dialog", "ROS", None))
        self.gb_knn_kume.setTitle(_translate("Dialog", "KNN ile Kümeleme", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Veri Seti Oluştur", None))
        self.knn_cluster_pb_create_dataset.setText(_translate("Dialog", "Tamam", None))
        self.label_42.setText(_translate("Dialog", "Üst Sınır         :", None))
        self.label_43.setText(_translate("Dialog", "Eleman sayısı :", None))
        self.knn_pb_cluster.setText(_translate("Dialog", "KÜMELE", None))
        self.knn_cluster_cb.setItemText(0, _translate("Dialog", "Öklid", None))
        self.knn_cluster_cb.setItemText(1, _translate("Dialog", "Manhattan", None))
        self.knn_cluster_cb.setItemText(2, _translate("Dialog", "Minkowski", None))
        self.label_44.setText(_translate("Dialog", "VERİ SETİ GRAFİĞİ :", None))
        self.label_45.setText(_translate("Dialog", "SONUÇ GRAFİĞİ :", None))
        self.label_46.setText(_translate("Dialog", "VERİ SETİ :", None))
        self.gb_navie.setTitle(_translate("Dialog", "NAVİE BAYES", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Yeni Kelime veya Kategori Ekle", None))
        self.label_59.setText(_translate("Dialog", "Kelime :", None))
        self.label_60.setText(_translate("Dialog", "Kategori :", None))
        self.pb_navie_veriekle.setText(_translate("Dialog", "Ekle", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Metin Sınıflandırma", None))
        self.label_61.setText(_translate("Dialog", "Metin Giriniz :", None))
        self.pb_navie_siniflandir.setText(_translate("Dialog", "Sınıflandır", None))
        self.lbl_navie_sonuc_2.setText(_translate("Dialog", "Kategori :", None))
        self.gb_parkinson.setTitle(_translate("Dialog", "Parkinson", None))
        self.gb_sst.setTitle(_translate("Dialog", "SST", None))
        self.label_7.setText(_translate("Dialog", "X_Train :", None))
        self.label_8.setText(_translate("Dialog", "y_Train :", None))
        self.label_9.setText(_translate("Dialog", "X_Test :", None))
        self.label_10.setText(_translate("Dialog", "Decision Tree Confusion Matrix", None))
        self.label_11.setText(_translate("Dialog", "Random Forest Accuracy Score :", None))
        self.label_12.setText(_translate("Dialog", "Random Forest Confusion Matrix :", None))
        self.label_13.setText(_translate("Dialog", "Decision Tree Accuracy Score :", None))
        self.gb_buttons.setTitle(_translate("Dialog", "Top Menu", None))
        self.pb_parkinson_veri_yukle.setToolTip(_translate("Dialog", "Verileri Yükle", None))
        self.pb_parkinson_class.setToolTip(_translate("Dialog", "Verileri Sınıflandır", None))
        self.gb_dst.setTitle(_translate("Dialog", "DST", None))
        self.label_14.setText(_translate("Dialog", "Random Forest Accuracy Score :", None))
        self.label_15.setText(_translate("Dialog", "y_Train :", None))
        self.label_16.setText(_translate("Dialog", "Decision Tree Accuracy Score :", None))
        self.label_17.setText(_translate("Dialog", "X_Test :", None))
        self.label_18.setText(_translate("Dialog", "X_Train :", None))
        self.label_19.setText(_translate("Dialog", "Random Forest Confusion Matrix :", None))
        self.label_20.setText(_translate("Dialog", "Decision Tree Confusion Matrix", None))
        self.gb_stcp.setTitle(_translate("Dialog", "STCP", None))
        self.label_21.setText(_translate("Dialog", "X_Train :", None))
        self.label_22.setText(_translate("Dialog", "y_Train :", None))
        self.label_23.setText(_translate("Dialog", "X_Test :", None))
        self.label_24.setText(_translate("Dialog", "Decision Tree Confusion Matrix", None))
        self.label_25.setText(_translate("Dialog", "Random Forest Accuracy Score :", None))
        self.label_26.setText(_translate("Dialog", "Random Forest Confusion Matrix :", None))
        self.label_27.setText(_translate("Dialog", "Decision Tree Accuracy Score :", None))
        self.gb_all_data.setTitle(_translate("Dialog", "ALL DATA", None))
        self.label_28.setText(_translate("Dialog", "All Data", None))
        self.label_29.setText(_translate("Dialog", "X_Train :", None))
        self.label_30.setText(_translate("Dialog", "X_Test :", None))
        self.label_31.setText(_translate("Dialog", "Confusion Matrix :", None))
        self.label_32.setText(_translate("Dialog", "Accuracy Score :", None))
        self.label_33.setText(_translate("Dialog", "Confusion Matrix :", None))
        self.label_34.setText(_translate("Dialog", "Accuracy Score :", None))
        self.label_35.setText(_translate("Dialog", "Random Forest", None))
        self.label_36.setText(_translate("Dialog", "Decision Tree", None))
        self.gb_parkinson_bottom_menu.setTitle(_translate("Dialog", "Bottom Menu", None))
        self.pb_parkinson_all_data.setToolTip(_translate("Dialog", "Verileri Yükle", None))
        self.pb_parkinson_class_2.setToolTip(_translate("Dialog", "Verileri Sınıflandır", None))
        self.pb_parkinson_split.setToolTip(_translate("Dialog", "Verileri Ayır", None))
        self.pb_parkinson_reload_split.setToolTip(_translate("Dialog", "Yeniden Sınıflandır", None))
        self.gb_normalizasyon.setTitle(_translate("Dialog", "Normalizasyon", None))
        self.pb_normalizasyon_dataload.setToolTip(_translate("Dialog", "Verileri Dosyadan Yükle", None))
        self.pb_normalize.setText(_translate("Dialog", "Uygula", None))
        self.rb_norm_minmax.setText(_translate("Dialog", "Min Max", None))
        self.rb_norm_zscore.setText(_translate("Dialog", "Z Score", None))
        self.rb_norm_median.setText(_translate("Dialog", "Medyan", None))
        self.pb_normalizasyon_datasave.setToolTip(_translate("Dialog", "Kaydet", None))
        self.gb_randomforest.setTitle(_translate("Dialog", "Random Forest", None))
        self.pb_random_forest_data_load.setToolTip(_translate("Dialog", "Verileri Dosyadan Yükle", None))
        self.label_47.setText(_translate("Dialog", "CONFUSİON MATRİX :", None))
        self.label_48.setText(_translate("Dialog", "ACCURARY SCORE :", None))
        self.pb_random_forest.setText(_translate("Dialog", "RANDOM FOREST", None))
        self.pb_random_forest_modelsave.setToolTip(_translate("Dialog", "Kaydet", None))
        self.label_49.setText(_translate("Dialog", "DATA:", None))
        self.label_50.setText(_translate("Dialog", "X Train:", None))
        self.label_51.setText(_translate("Dialog", "X Test:", None))
        self.pb_random_forest_tandt.setText(_translate("Dialog", "TRAİN AND TEST", None))
        self.lbl_random_forest_slider.setText(_translate("Dialog", "0", None))
        self.label_52.setText(_translate("Dialog", "TEST YÜZDESİ :", None))
        self.gb_train_test.setTitle(_translate("Dialog", "Train and Test Split", None))
        self.pb_train_and_test.setText(_translate("Dialog", "TRAİN AND TEST", None))
        self.lbl_train_test.setText(_translate("Dialog", "0", None))
        self.label_53.setText(_translate("Dialog", "DATA:", None))
        self.label_54.setText(_translate("Dialog", "TEST YÜZDESİ :", None))
        self.pb_train_test_data_load.setToolTip(_translate("Dialog", "Verileri Dosyadan Yükle", None))
        self.label_55.setText(_translate("Dialog", "X TRAİN :", None))
        self.label_56.setText(_translate("Dialog", "Y TRAİN :", None))
        self.label_57.setText(_translate("Dialog", "X TEST :", None))
        self.label_58.setText(_translate("Dialog", "Y TEST :", None))

