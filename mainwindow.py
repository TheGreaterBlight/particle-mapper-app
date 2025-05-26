# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(490, 458)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.firstConsole = QPlainTextEdit(self.tab)
        self.firstConsole.setObjectName(u"firstConsole")

        self.gridLayout.addWidget(self.firstConsole, 1, 3, 15, 1)

        self.agregarRed = QSpinBox(self.tab)
        self.agregarRed.setObjectName(u"agregarRed")
        self.agregarRed.setMaximum(255)

        self.gridLayout.addWidget(self.agregarRed, 9, 0, 1, 3)

        self.agregarBlue = QSpinBox(self.tab)
        self.agregarBlue.setObjectName(u"agregarBlue")
        self.agregarBlue.setMaximum(255)

        self.gridLayout.addWidget(self.agregarBlue, 13, 0, 1, 3)

        self.agregaFinalButton = QPushButton(self.tab)
        self.agregaFinalButton.setObjectName(u"agregaFinalButton")
        self.agregaFinalButton.setMinimumSize(QSize(137, 0))

        self.gridLayout.addWidget(self.agregaFinalButton, 15, 0, 1, 3)

        self.Consola_de_Dispositivo_Lbl = QLabel(self.tab)
        self.Consola_de_Dispositivo_Lbl.setObjectName(u"Consola_de_Dispositivo_Lbl")

        self.gridLayout.addWidget(self.Consola_de_Dispositivo_Lbl, 0, 3, 1, 1)

        self.agregarDestinoX = QSpinBox(self.tab)
        self.agregarDestinoX.setObjectName(u"agregarDestinoX")
        self.agregarDestinoX.setMaximum(500)

        self.gridLayout.addWidget(self.agregarDestinoX, 5, 0, 1, 2)

        self.agregarGreen = QSpinBox(self.tab)
        self.agregarGreen.setObjectName(u"agregarGreen")
        self.agregarGreen.setMaximum(255)

        self.gridLayout.addWidget(self.agregarGreen, 11, 0, 1, 3)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 0, 2, 1)

        self.agregarOrigenX = QSpinBox(self.tab)
        self.agregarOrigenX.setObjectName(u"agregarOrigenX")
        self.agregarOrigenX.setMaximum(500)

        self.gridLayout.addWidget(self.agregarOrigenX, 3, 0, 1, 2)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 2)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)

        self.agregarDestinoY = QSpinBox(self.tab)
        self.agregarDestinoY.setObjectName(u"agregarDestinoY")
        self.agregarDestinoY.setMaximum(500)

        self.gridLayout.addWidget(self.agregarDestinoY, 5, 2, 1, 1)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)

        self.agregarInicioButton = QPushButton(self.tab)
        self.agregarInicioButton.setObjectName(u"agregarInicioButton")
        self.agregarInicioButton.setMinimumSize(QSize(137, 0))

        self.gridLayout.addWidget(self.agregarInicioButton, 14, 0, 1, 3)

        self.agregarID = QLineEdit(self.tab)
        self.agregarID.setObjectName(u"agregarID")
        self.agregarID.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.gridLayout.addWidget(self.agregarID, 0, 1, 2, 2)

        self.agregarVelocidad = QLineEdit(self.tab)
        self.agregarVelocidad.setObjectName(u"agregarVelocidad")
        self.agregarVelocidad.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.gridLayout.addWidget(self.agregarVelocidad, 7, 0, 1, 3)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 2)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 2)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 12, 0, 1, 1)

        self.agregarOrigenY = QSpinBox(self.tab)
        self.agregarOrigenY.setObjectName(u"agregarOrigenY")
        self.agregarOrigenY.setMaximum(500)

        self.gridLayout.addWidget(self.agregarOrigenY, 3, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.leerArchivoButton = QPushButton(self.tab_2)
        self.leerArchivoButton.setObjectName(u"leerArchivoButton")
        self.leerArchivoButton.setGeometry(QRect(20, 80, 171, 23))
        self.guardarSesionButton = QPushButton(self.tab_2)
        self.guardarSesionButton.setObjectName(u"guardarSesionButton")
        self.guardarSesionButton.setGeometry(QRect(20, 30, 171, 23))
        self.secondConsole = QPlainTextEdit(self.tab_2)
        self.secondConsole.setObjectName(u"secondConsole")
        self.secondConsole.setGeometry(QRect(230, 20, 231, 371))
        self.Consola_de_Dispositivo_Lbl2 = QLabel(self.tab_2)
        self.Consola_de_Dispositivo_Lbl2.setObjectName(u"Consola_de_Dispositivo_Lbl2")
        self.Consola_de_Dispositivo_Lbl2.setGeometry(QRect(230, 0, 151, 16))
        self.abrirGraficadorButton = QPushButton(self.tab_2)
        self.abrirGraficadorButton.setObjectName(u"abrirGraficadorButton")
        self.abrirGraficadorButton.setGeometry(QRect(20, 350, 171, 23))
        self.abrirGraficadorButtonButOnlyPointsButton = QPushButton(self.tab_2)
        self.abrirGraficadorButtonButOnlyPointsButton.setObjectName(u"abrirGraficadorButtonButOnlyPointsButton")
        self.abrirGraficadorButtonButOnlyPointsButton.setGeometry(QRect(20, 320, 171, 23))
        self.abrirGraficadorButtonButNearestPoints = QPushButton(self.tab_2)
        self.abrirGraficadorButtonButNearestPoints.setObjectName(u"abrirGraficadorButtonButNearestPoints")
        self.abrirGraficadorButtonButNearestPoints.setGeometry(QRect(20, 290, 171, 23))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.consolaTabla = QTableWidget(self.tab_3)
        self.consolaTabla.setObjectName(u"consolaTabla")
        self.consolaTabla.setGeometry(QRect(5, 11, 451, 351))
        self.barraDeBusqueda = QLineEdit(self.tab_3)
        self.barraDeBusqueda.setObjectName(u"barraDeBusqueda")
        self.barraDeBusqueda.setGeometry(QRect(0, 370, 281, 21))
        self.busquedaButton = QPushButton(self.tab_3)
        self.busquedaButton.setObjectName(u"busquedaButton")
        self.busquedaButton.setGeometry(QRect(370, 370, 75, 20))
        self.refrescarButton = QPushButton(self.tab_3)
        self.refrescarButton.setObjectName(u"refrescarButton")
        self.refrescarButton.setGeometry(QRect(290, 370, 75, 20))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.thirdConsole = QPlainTextEdit(self.tab_4)
        self.thirdConsole.setObjectName(u"thirdConsole")
        self.thirdConsole.setGeometry(QRect(233, 20, 231, 371))
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 0, 121, 16))
        self.generarListaAdyacenciaButton = QPushButton(self.tab_4)
        self.generarListaAdyacenciaButton.setObjectName(u"generarListaAdyacenciaButton")
        self.generarListaAdyacenciaButton.setGeometry(QRect(30, 360, 161, 23))
        self.abrirGraficadorButtonKrusk = QPushButton(self.tab_4)
        self.abrirGraficadorButtonKrusk.setObjectName(u"abrirGraficadorButtonKrusk")
        self.abrirGraficadorButtonKrusk.setGeometry(QRect(30, 330, 161, 23))
        self.abrirGraficadorButtonPrimm = QPushButton(self.tab_4)
        self.abrirGraficadorButtonPrimm.setObjectName(u"abrirGraficadorButtonPrimm")
        self.abrirGraficadorButtonPrimm.setGeometry(QRect(30, 300, 161, 23))
        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Sopita.com v2.0", u"MainWindow", None))
        self.agregaFinalButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.Consola_de_Dispositivo_Lbl.setText(QCoreApplication.translate("MainWindow", u"Consola de Dispositivo", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.agregarInicioButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Men\u00fa", None))
        self.leerArchivoButton.setText(QCoreApplication.translate("MainWindow", u"Leer archivo", None))
        self.guardarSesionButton.setText(QCoreApplication.translate("MainWindow", u"Guardar sesi\u00f3n actual", None))
        self.Consola_de_Dispositivo_Lbl2.setText(QCoreApplication.translate("MainWindow", u"Consola de Dispositivo", None))
        self.abrirGraficadorButton.setText(QCoreApplication.translate("MainWindow", u"Abrir Graficador", None))
        self.abrirGraficadorButtonButOnlyPointsButton.setText(QCoreApplication.translate("MainWindow", u"Abrir Graf. pero solo ver Puntos", None))
        self.abrirGraficadorButtonButNearestPoints.setText(QCoreApplication.translate("MainWindow", u"Abrir Graf. Puntos Cercanos -  FB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Sesi\u00f3n", None))
        self.busquedaButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.refrescarButton.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Lista de Adyacencia", None))
        self.generarListaAdyacenciaButton.setText(QCoreApplication.translate("MainWindow", u"Generar Lista de Adyacencia", None))
        self.abrirGraficadorButtonKrusk.setText(QCoreApplication.translate("MainWindow", u"Abrir Graf. Algoritmo de Kruskal", None))
        self.abrirGraficadorButtonPrimm.setText(QCoreApplication.translate("MainWindow", u"Abrir Graf. Algoritmo de Primm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Grafo Menu", None))
    # retranslateUi

