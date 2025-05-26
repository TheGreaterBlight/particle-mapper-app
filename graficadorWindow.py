# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graficador.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GraficadorWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(662, 648)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gBuscarButton = QPushButton(self.centralwidget)
        self.gBuscarButton.setObjectName(u"gBuscarButton")

        self.gridLayout.addWidget(self.gBuscarButton, 0, 2, 1, 1)

        self.gLimpiarButton = QPushButton(self.centralwidget)
        self.gLimpiarButton.setObjectName(u"gLimpiarButton")

        self.gridLayout.addWidget(self.gLimpiarButton, 0, 3, 1, 1)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 4)

        self.gSearchBar = QLineEdit(self.centralwidget)
        self.gSearchBar.setObjectName(u"gSearchBar")

        self.gridLayout.addWidget(self.gSearchBar, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gBuscarButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.gLimpiarButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
    # retranslateUi

