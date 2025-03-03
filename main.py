# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog, QSlider
from PIL.ImageQt import ImageQt
from PIL import Image
from baturalp import *
import cv2
import numpy as np


class Ui_MainWindow(object):
    img = None
    effectImage= None
    resetImage = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectImageButton.setGeometry(QtCore.QRect(260, 10, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectImageButton.sizePolicy().hasHeightForWidth())
        self.selectImageButton.setSizePolicy(sizePolicy)
        self.selectImageButton.setObjectName("selectImageButton")
        self.selectImageButton.clicked.connect(self.openImage)
        self.selectedImage = QtWidgets.QLabel(self.centralwidget)
        self.selectedImage.setGeometry(QtCore.QRect(10, 50, 331, 291))
        self.selectedImage.setText("")
        self.selectedImage.setPixmap(QtGui.QPixmap("../../ImageProcessingProject/test.jpg"))
        self.selectedImage.setScaledContents(True)
        self.selectedImage.setObjectName("selectedImage")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(350, 50, 511, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.basicOperations = QtWidgets.QWidget()
        self.basicOperations.setObjectName("basicOperations")
        self.label = QtWidgets.QLabel(self.basicOperations)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.basicOperations)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 10, 331, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.basicOperations)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 30, 315, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(74, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.cropButton = QtWidgets.QPushButton(self.basicOperations)
        self.cropButton.setGeometry(QtCore.QRect(420, 30, 75, 23))
        self.cropButton.setObjectName("cropButton")
        self.cropButton.setText("Crop!")
        self.cropButton.clicked.connect(self.crop_image)
        self.tabWidget.addTab(self.basicOperations, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 360, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.rotate_right)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 360, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.rotate_left)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.flipButton = QtWidgets.QPushButton(self.basicOperations)
        self.flipButton.setGeometry(QtCore.QRect(100, 80, 75, 23))
        self.flipButton.setObjectName("flipButton")
        self.mirrorButton = QtWidgets.QPushButton(self.basicOperations)
        self.mirrorButton.setGeometry(QtCore.QRect(220, 80, 75, 23))
        self.mirrorButton.setObjectName("mirrorButton")
        self.invertButton = QtWidgets.QPushButton(self.basicOperations)
        self.invertButton.setGeometry(QtCore.QRect(330, 80, 75, 23))
        self.invertButton.setObjectName("invertButton")
        self.flipButton.clicked.connect(self.flip_image)
        self.mirrorButton.clicked.connect(self.mirror_image)
        self.invertButton.clicked.connect(self.invert_image)
        self.brightnessSlider = QtWidgets.QSlider(self.basicOperations)
        self.brightnessSlider.setGeometry(QtCore.QRect(120, 130, 160, 22))
        self.brightnessSlider.setMinimum(0)
        self.brightnessSlider.setMaximum(20)
        self.brightnessSlider.setSingleStep(1)
        self.brightnessSlider.setProperty("value", 10)
        self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.brightnessSlider.valueChanged.connect(self.brightness_change)
        self.contrastSlider = QtWidgets.QSlider(self.basicOperations)
        self.contrastSlider.setGeometry(QtCore.QRect(120, 160, 160, 22))
        self.contrastSlider.setMinimum(0)
        self.contrastSlider.setMaximum(20)
        self.contrastSlider.setSingleStep(1)
        self.contrastSlider.setProperty("value", 10)
        self.contrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.contrastSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.contrastSlider.setObjectName("contrastSlider")
        self.contrastSlider.valueChanged.connect(self.contrast_change)
        self.label_5 = QtWidgets.QLabel(self.basicOperations)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 101, 16))
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 461, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutEffects = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayoutEffects.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutEffects.setObjectName("gridLayoutEffects")
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.random_filter_1)
        self.gridLayoutEffects.addWidget(self.pushButton_11, 1, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.pencil_scetch)
        self.gridLayoutEffects.addWidget(self.pushButton_13, 3, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.sepia)
        self.gridLayoutEffects.addWidget(self.pushButton_14, 4, 1, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(self.blur)
        self.gridLayoutEffects.addWidget(self.pushButton_19, 4, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.bathroom_effect2)
        self.gridLayoutEffects.addWidget(self.pushButton_6, 2, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.bw_pencil)
        self.gridLayoutEffects.addWidget(self.pushButton_9, 0, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(self.swirl)
        self.gridLayoutEffects.addWidget(self.pushButton_23, 2, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.fisheyelast)
        self.gridLayoutEffects.addWidget(self.pushButton_16, 1, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.twist)
        self.gridLayoutEffects.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(self.blue_shift)
        self.gridLayoutEffects.addWidget(self.pushButton_22, 1, 0, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_26.clicked.connect(self.cold)
        self.gridLayoutEffects.addWidget(self.pushButton_26, 5, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.bathroom_effect)
        self.gridLayoutEffects.addWidget(self.pushButton_17, 2, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.colored_pencil)
        self.gridLayoutEffects.addWidget(self.pushButton_8, 0, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.water_color)
        self.gridLayoutEffects.addWidget(self.pushButton_10, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.emboss)
        self.gridLayoutEffects.addWidget(self.pushButton_5, 4, 3, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_25.clicked.connect(self.sharpen)
        self.gridLayoutEffects.addWidget(self.pushButton_25, 4, 0, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.clicked.connect(self.oil_painting)
        self.gridLayoutEffects.addWidget(self.pushButton_21, 0, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.warm)
        self.gridLayoutEffects.addWidget(self.pushButton_15, 5, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(self.bileteral)
        self.gridLayoutEffects.addWidget(self.pushButton_18, 3, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.gray)
        self.gridLayoutEffects.addWidget(self.pushButton_4, 5, 3, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(self.black_and_white)
        self.gridLayoutEffects.addWidget(self.pushButton_20, 5, 2, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.clicked.connect(self.solarization)
        self.gridLayoutEffects.addWidget(self.pushButton_24, 3, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.frosted_glass)
        self.gridLayoutEffects.addWidget(self.pushButton_12, 2, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.negative_filter)
        self.gridLayoutEffects.addWidget(self.pushButton_7, 3, 3, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_27.clicked.connect(self.edges)
        self.gridLayoutEffects.addWidget(self.pushButton_27, 6, 0, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_28.clicked.connect(self.random_filter_2)
        self.gridLayoutEffects.addWidget(self.pushButton_28, 6, 1, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_29.clicked.connect(self.random_filter_3)
        self.gridLayoutEffects.addWidget(self.pushButton_29, 6, 2, 1, 1)
        self.resetImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetImageButton.setGeometry(QtCore.QRect(360, 10, 81, 31))
        self.resetImageButton.clicked.connect(self.reset_image)
        self.label_7 = QtWidgets.QLabel(self.basicOperations)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label_7.setObjectName("label_7")



        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectImageButton.setText(_translate("MainWindow", "Select Image"))
        self.label.setText(_translate("MainWindow", "Crop Image:"))
        self.label_3.setText(_translate("MainWindow", "W"))
        self.label_6.setText(_translate("MainWindow", "H"))
        self.label_4.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.flipButton.setText(_translate("MainWindow", "Flip!"))
        self.mirrorButton.setText(_translate("MainWindow", "Mirror!"))
        self.invertButton.setText(_translate("MainWindow", "Invert!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.basicOperations), _translate("MainWindow", "Basic Operations"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Image Enchancement"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Artistic Effects and Filters"))
        self.pushButton.setText(_translate("MainWindow", "Rotate Left"))
        self.pushButton_2.setText(_translate("MainWindow", "Rotate Right"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.label_5.setText(_translate("MainWindow", "Change Brightness:"))
        self.pushButton_11.setText(_translate("MainWindow", "Random Filter"))
        self.pushButton_13.setText(_translate("MainWindow", "Pencil Sketch"))
        self.pushButton_14.setText(_translate("MainWindow", "Sepia"))
        self.pushButton_19.setText(_translate("MainWindow", "Blur"))
        self.pushButton_6.setText(_translate("MainWindow", "Bathroom Effect2"))
        self.pushButton_9.setText(_translate("MainWindow", "BlackAndWhite Pencil"))
        self.pushButton_23.setText(_translate("MainWindow", "Swirl"))
        self.pushButton_16.setText(_translate("MainWindow", "Fisheye"))
        self.pushButton_3.setText(_translate("MainWindow", "Twist"))
        self.pushButton_22.setText(_translate("MainWindow", "BlueShift Filter"))
        self.pushButton_26.setText(_translate("MainWindow", "Cold Filter"))
        self.pushButton_17.setText(_translate("MainWindow", "Bathroom Effect"))
        self.pushButton_8.setText(_translate("MainWindow", "Color Pencil"))
        self.pushButton_10.setText(_translate("MainWindow", "Water Color"))
        self.pushButton_5.setText(_translate("MainWindow", "Emboss"))
        self.pushButton_25.setText(_translate("MainWindow", "Sharper Filter"))
        self.pushButton_21.setText(_translate("MainWindow", "Oil Painting"))
        self.pushButton_15.setText(_translate("MainWindow", "Warm Filter"))
        self.pushButton_18.setText(_translate("MainWindow", "Bileteral Filter"))
        self.pushButton_4.setText(_translate("MainWindow", "Gray"))
        self.pushButton_20.setText(_translate("MainWindow", "BlackAndWhite"))
        self.pushButton_24.setText(_translate("MainWindow", "Solarization"))
        self.pushButton_12.setText(_translate("MainWindow", "Frosted Glass"))
        self.pushButton_7.setText(_translate("MainWindow", "Negative Filter"))
        self.pushButton_27.setText(_translate("MainWindow", "Edges Filter"))
        self.pushButton_28.setText(_translate("MainWindow", "Random Filter 2"))
        self.pushButton_29.setText(_translate("MainWindow", "Random Filter 3"))
        self.resetImageButton.setText(_translate("MainWindow", "Reset Image"))
        self.label_7.setText(_translate("MainWindow", "Change Contrast:"))

    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        self.img = cv2.imread(imagePath)
        self.effectImage = self.img
        self.resetImage = self.img
        pixmap = QPixmap(imagePath)
        self.selectedImage.setPixmap(pixmap)
        cv2.imwrite("temp.jpg", self.img)
    def reset_image(self):
        self.img = self.resetImage
        self.effectImage = self.resetImage
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()

    def rotate_right(self):
        self.img = cv2.imread("temp.jpg")
        self.img = rotate_right(self.img)
        self.effectImage = rotate_right(self.effectImage)
        cv2.imwrite("temp.jpg",self.img)
        self.toPixmap()
    def rotate_left(self):
        self.img = cv2.imread("temp.jpg")
        self.img = rotate_left(self.img)
        self.effectImage = rotate_left(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def oil_painting(self):
        self.effectImage = cv2.imread("temp.jpg")


        self.img = oil_painting(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def water_color(self):
        self.effectImage = cv2.imread("temp.jpg")
        self.img = watercolor( self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def bw_pencil(self):
        self.effectImage = cv2.imread("temp.jpg")


        self.img = bw_pencil(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def colored_pencil(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = colored_pencil(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def blue_shift(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = blue_shift_filter(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def random_filter_1(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = random_filter(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def pencil_scetch(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = pencil_sketch(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def bileteral(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = bilateral(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def negative_filter(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = negative_filter(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def sharpen(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = sharpen(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def sepia(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = sepia(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()

    def blur(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = gaussianBlur(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()

    def emboss(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = emboss(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def cold(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = coldImage(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def warm(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = warmImage(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def black_and_white(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = black_white(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def edges(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = edges_filter(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def gray(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = gray(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def random_filter_2(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = random_filter_2(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def random_filter_3(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = random_filter_3(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def gama_correction(self):
        gamma_correction(self.img)
    def log_transform(self):
        logtransform(self.img)


    def flip_image(self):
        self.img = cv2.imread("temp.jpg")
        self.img = flip_image(self.img)
        self.img = np.array(self.img)
        self.img = cv2.cvtColor(self.img,cv2.COLOR_RGB2BGR)
        self.effectImage = flip_image(self.effectImage)
        self.effectImage = np.array(self.effectImage)
        self.effectImage = cv2.cvtColor(self.effectImage, cv2.COLOR_RGB2BGR)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def invert_image(self):
        self.img = cv2.imread("temp.jpg")
        self.img = invert_image(self.img)
        self.effectImage = invert_image(self.effectImage)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def mirror_image(self):
        self.img = cv2.imread("temp.jpg")
        self.img = mirror_image(self.img)
        self.img = np.array(self.img)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        self.effectImage = mirror_image(self.effectImage)
        self.effectImage = np.array(self.effectImage)
        self.effectImage = cv2.cvtColor(self.effectImage, cv2.COLOR_RGB2BGR)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def frosted_glass(self):
        self.effectImage = cv2.imread("temp.jpg")

        self.img = cv2.resize(self.effectImage,(600,600))
        self.img = frostedgalss(self.img)
        cv2.imwrite("temp.jpg", self.img)
        self.toPixmap()
    def brightness_change(self):
        temp = self.img
        temp2 = self.effectImage
        self.img = change_brightness_of_image(self.img,self.brightnessSlider.value())
        self.img= np.array(self.img)
        self.img= cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        cv2.imwrite("temp.jpg", self.img)
        self.img = temp
        self.toPixmap()
    def contrast_change(self):
        temp = self.img
        temp2 = self.effectImage
        self.img = change_contrast_of_image(self.img, self.contrastSlider.value())
        self.img = np.array(self.img)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        cv2.imwrite("temp.jpg", self.img)
        self.img = temp
        self.toPixmap()
    def fisheyelast(self):
        self.effectImage = cv2.imread("temp.jpg")

        r, g, b = cv2.split(self.effectImage)
        r, g, b = fisheyelast(r), fisheyelast(g), fisheyelast(b)
        img = np.dstack((r, g, b))
        self.img = img
        cv2.imwrite("temp.jpg", img)
        self.toPixmap()
    def histogram(self):
        r, g, b = cv2.split(self.img)
        r, g, b = histogram(r), histogram(g), histogram(b)
        img = np.dstack((r, g, b))
        self.img = img
        cv2.imwrite("temp.jpg", img)
        self.toPixmap()
    def solarization(self):
        self.effectImage = cv2.imread("temp.jpg")

        r, g, b = cv2.split(self.effectImage)
        r, g, b = solarization(r), solarization(g), solarization(b)
        img = np.dstack((r, g, b))
        self.img = img
        cv2.imwrite("temp.jpg", img)
        self.toPixmap()

    def twist(self):
        self.effectImage = cv2.imread("temp.jpg")

        r, g, b = cv2.split(self.effectImage)
        r, g, b = twist(r), twist(g), twist(b)
        img = np.dstack((r, g, b))
        self.img = img
        cv2.imwrite("temp.jpg", img)
        self.toPixmap()
    def bathroom_effect(self):
        self.effectImage = cv2.imread("temp.jpg")

        r, g, b = cv2.split(self.effectImage)
        r, g, b = bathroom_effect(r), bathroom_effect(g), bathroom_effect(b)
        img = np.dstack((r, g, b))
        self.img = img
        cv2.imwrite("temp.jpg", img)
        self.toPixmap()
    def bathroom_effect2(self):
        self.effectImage = cv2.imread("temp.jpg")

        r, g, b = cv2.split(self.effectImage)
        r, g, b = bath2_effect(r), bath2_effect(g), bath2_effect(b)
        img = np.dstack((r, g, b))
        self.img = img
        cv2.imwrite("temp.jpg", img)
        self.toPixmap()

    def swirl(self):
        self.effectImage = cv2.imread("temp.jpg")
        r, g, b = cv2.split(self.effectImage)
        koef = 0.7
        r, g, b = swirl(r, koef), swirl(g, koef), swirl(b, koef)
        img = np.dstack((r, g, b))
        self.img = img
        cv2.imwrite("temp.jpg", img)
        self.toPixmap()
    def crop_image(self):

        x = int(self.lineEdit.text())
        y = int(self.lineEdit_2.text())
        w = int(self.lineEdit_3.text())
        h = int(self.lineEdit_4.text())
        cropped_img = cv2.imread("temp.jpg")
        height, width, channel = cropped_img.shape
        if((y+h)>=width or (x+w)>=height):
            print("nope")
        else:
            cropped_img = crop_image(cropped_img, w, h, x, y)
            self.effectImage = crop_image(self.effectImage, w, h, x, y)
            cv2.imwrite("temp.jpg", cropped_img)
            self.img = cropped_img
            url = "temp.jpg"
            qImg = QPixmap(url)
            self.selectedImage.setPixmap(qImg)

    def toPixmap(self):
        url = "temp.jpg"
        qImg = QPixmap(url)
        self.selectedImage.setPixmap(qImg)
        """height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        qImg = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(qImg)
        self.selectedImage.setPixmap(pixmap)"""
    """def toPixmap2(self):
        rgb_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        PIL_image = Image.fromarray(rgb_image).convert('RGB')
        pixmap = QPixmap.fromImage(ImageQt(PIL_image))
        self.selectedImage.setPixmap(pixmap)"""







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
