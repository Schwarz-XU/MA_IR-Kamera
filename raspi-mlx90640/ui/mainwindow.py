# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(443, 416)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Zone11_Floor = QtWidgets.QGridLayout()
        self.Zone11_Floor.setObjectName("Zone11_Floor")
        self.STset_10L2 = QtWidgets.QSpinBox(self.tab_2)
        self.STset_10L2.setMinimum(15)
        self.STset_10L2.setMaximum(45)
        self.STset_10L2.setObjectName("STset_10L2")
        self.Zone11_Floor.addWidget(self.STset_10L2, 4, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setObjectName("label_25")
        self.Zone11_Floor.addWidget(self.label_25, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setObjectName("label_21")
        self.Zone11_Floor.addWidget(self.label_21, 5, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setObjectName("label_22")
        self.Zone11_Floor.addWidget(self.label_22, 0, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setObjectName("label_26")
        self.Zone11_Floor.addWidget(self.label_26, 3, 0, 1, 1)
        self.STset_10L3 = QtWidgets.QSpinBox(self.tab_2)
        self.STset_10L3.setMinimum(15)
        self.STset_10L3.setMaximum(45)
        self.STset_10L3.setObjectName("STset_10L3")
        self.Zone11_Floor.addWidget(self.STset_10L3, 5, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setObjectName("label_23")
        self.Zone11_Floor.addWidget(self.label_23, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setObjectName("label_24")
        self.Zone11_Floor.addWidget(self.label_24, 2, 0, 1, 1)
        self.CM_10L3 = QtWidgets.QComboBox(self.tab_2)
        self.CM_10L3.setObjectName("CM_10L3")
        self.CM_10L3.addItem("")
        self.CM_10L3.addItem("")
        self.CM_10L3.addItem("")
        self.CM_10L3.addItem("")
        self.Zone11_Floor.addWidget(self.CM_10L3, 5, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setObjectName("label_28")
        self.Zone11_Floor.addWidget(self.label_28, 1, 0, 1, 1)
        self.STset_10L1 = QtWidgets.QSpinBox(self.tab_2)
        self.STset_10L1.setMinimum(15)
        self.STset_10L1.setMaximum(45)
        self.STset_10L1.setObjectName("STset_10L1")
        self.Zone11_Floor.addWidget(self.STset_10L1, 2, 1, 1, 1)
        self.CM_10L1 = QtWidgets.QComboBox(self.tab_2)
        self.CM_10L1.setObjectName("CM_10L1")
        self.CM_10L1.addItem("")
        self.CM_10L1.addItem("")
        self.CM_10L1.addItem("")
        self.CM_10L1.addItem("")
        self.Zone11_Floor.addWidget(self.CM_10L1, 2, 2, 1, 1)
        self.CM_10X1 = QtWidgets.QComboBox(self.tab_2)
        self.CM_10X1.setObjectName("CM_10X1")
        self.CM_10X1.addItem("")
        self.CM_10X1.addItem("")
        self.CM_10X1.addItem("")
        self.CM_10X1.addItem("")
        self.Zone11_Floor.addWidget(self.CM_10X1, 1, 2, 1, 1)
        self.STset_10S123 = QtWidgets.QSpinBox(self.tab_2)
        self.STset_10S123.setMinimum(15)
        self.STset_10S123.setMaximum(45)
        self.STset_10S123.setObjectName("STset_10S123")
        self.Zone11_Floor.addWidget(self.STset_10S123, 3, 1, 1, 1)
        self.CM_10L2 = QtWidgets.QComboBox(self.tab_2)
        self.CM_10L2.setObjectName("CM_10L2")
        self.CM_10L2.addItem("")
        self.CM_10L2.addItem("")
        self.CM_10L2.addItem("")
        self.CM_10L2.addItem("")
        self.Zone11_Floor.addWidget(self.CM_10L2, 4, 2, 1, 1)
        self.CM_10S123 = QtWidgets.QComboBox(self.tab_2)
        self.CM_10S123.setObjectName("CM_10S123")
        self.CM_10S123.addItem("")
        self.CM_10S123.addItem("")
        self.CM_10S123.addItem("")
        self.CM_10S123.addItem("")
        self.Zone11_Floor.addWidget(self.CM_10S123, 3, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setObjectName("label_20")
        self.Zone11_Floor.addWidget(self.label_20, 4, 0, 1, 1)
        self.bt_write_floor = QtWidgets.QPushButton(self.tab_2)
        self.bt_write_floor.setObjectName("bt_write_floor")
        self.Zone11_Floor.addWidget(self.bt_write_floor, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.Zone11_Floor, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.Zone11_FW = QtWidgets.QGridLayout()
        self.Zone11_FW.setObjectName("Zone11_FW")
        self.CM_1150 = QtWidgets.QComboBox(self.tab)
        self.CM_1150.setObjectName("CM_1150")
        self.CM_1150.addItem("")
        self.CM_1150.addItem("")
        self.CM_1150.addItem("")
        self.CM_1150.addItem("")
        self.Zone11_FW.addWidget(self.CM_1150, 6, 2, 1, 1)
        self.CM_1110 = QtWidgets.QComboBox(self.tab)
        self.CM_1110.setObjectName("CM_1110")
        self.CM_1110.addItem("")
        self.CM_1110.addItem("")
        self.CM_1110.addItem("")
        self.CM_1110.addItem("")
        self.Zone11_FW.addWidget(self.CM_1110, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.Zone11_FW.addWidget(self.label_4, 0, 2, 1, 1)
        self.CM_1130 = QtWidgets.QComboBox(self.tab)
        self.CM_1130.setObjectName("CM_1130")
        self.CM_1130.addItem("")
        self.CM_1130.addItem("")
        self.CM_1130.addItem("")
        self.CM_1130.addItem("")
        self.Zone11_FW.addWidget(self.CM_1130, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.Zone11_FW.addWidget(self.label_3, 0, 1, 1, 1)
        self.CM_1140 = QtWidgets.QComboBox(self.tab)
        self.CM_1140.setObjectName("CM_1140")
        self.CM_1140.addItem("")
        self.CM_1140.addItem("")
        self.CM_1140.addItem("")
        self.CM_1140.addItem("")
        self.Zone11_FW.addWidget(self.CM_1140, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.Zone11_FW.addWidget(self.label_2, 1, 1, 1, 1)
        self.CM_1120 = QtWidgets.QComboBox(self.tab)
        self.CM_1120.setObjectName("CM_1120")
        self.CM_1120.addItem("")
        self.CM_1120.addItem("")
        self.CM_1120.addItem("")
        self.CM_1120.addItem("")
        self.Zone11_FW.addWidget(self.CM_1120, 3, 2, 1, 1)
        self.CM_1160 = QtWidgets.QComboBox(self.tab)
        self.CM_1160.setObjectName("CM_1160")
        self.CM_1160.addItem("")
        self.CM_1160.addItem("")
        self.CM_1160.addItem("")
        self.CM_1160.addItem("")
        self.Zone11_FW.addWidget(self.CM_1160, 7, 2, 1, 1)
        self.CM_11XX = QtWidgets.QComboBox(self.tab)
        self.CM_11XX.setObjectName("CM_11XX")
        self.CM_11XX.addItem("")
        self.CM_11XX.addItem("")
        self.CM_11XX.addItem("")
        self.CM_11XX.addItem("")
        self.Zone11_FW.addWidget(self.CM_11XX, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.Zone11_FW.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.Zone11_FW.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.Zone11_FW.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.Zone11_FW.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.Zone11_FW.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setObjectName("label_10")
        self.Zone11_FW.addWidget(self.label_10, 7, 0, 1, 1)
        self.STset_1110 = QtWidgets.QSpinBox(self.tab)
        self.STset_1110.setMinimum(15)
        self.STset_1110.setMaximum(45)
        self.STset_1110.setObjectName("STset_1110")
        self.Zone11_FW.addWidget(self.STset_1110, 2, 1, 1, 1)
        self.STset_1120 = QtWidgets.QSpinBox(self.tab)
        self.STset_1120.setMinimum(15)
        self.STset_1120.setMaximum(45)
        self.STset_1120.setObjectName("STset_1120")
        self.Zone11_FW.addWidget(self.STset_1120, 3, 1, 1, 1)
        self.STset_1130 = QtWidgets.QSpinBox(self.tab)
        self.STset_1130.setMinimum(15)
        self.STset_1130.setMaximum(45)
        self.STset_1130.setObjectName("STset_1130")
        self.Zone11_FW.addWidget(self.STset_1130, 4, 1, 1, 1)
        self.STset_1140 = QtWidgets.QSpinBox(self.tab)
        self.STset_1140.setMinimum(15)
        self.STset_1140.setMaximum(45)
        self.STset_1140.setObjectName("STset_1140")
        self.Zone11_FW.addWidget(self.STset_1140, 5, 1, 1, 1)
        self.STset_1150 = QtWidgets.QSpinBox(self.tab)
        self.STset_1150.setMinimum(15)
        self.STset_1150.setMaximum(45)
        self.STset_1150.setObjectName("STset_1150")
        self.Zone11_FW.addWidget(self.STset_1150, 6, 1, 1, 1)
        self.STset_1160 = QtWidgets.QSpinBox(self.tab)
        self.STset_1160.setMinimum(15)
        self.STset_1160.setMaximum(45)
        self.STset_1160.setObjectName("STset_1160")
        self.Zone11_FW.addWidget(self.STset_1160, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.Zone11_FW.addWidget(self.label, 1, 0, 1, 1)
        self.bt_write_frontwall = QtWidgets.QPushButton(self.tab)
        self.bt_write_frontwall.setObjectName("bt_write_frontwall")
        self.Zone11_FW.addWidget(self.bt_write_frontwall, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.Zone11_FW, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Zone11_SW = QtWidgets.QGridLayout()
        self.Zone11_SW.setObjectName("Zone11_SW")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setObjectName("label_17")
        self.Zone11_SW.addWidget(self.label_17, 4, 0, 1, 1)
        self.STset_123A = QtWidgets.QSpinBox(self.tab_3)
        self.STset_123A.setMinimum(15)
        self.STset_123A.setMaximum(45)
        self.STset_123A.setObjectName("STset_123A")
        self.Zone11_SW.addWidget(self.STset_123A, 4, 1, 1, 1)
        self.CM_125A = QtWidgets.QComboBox(self.tab_3)
        self.CM_125A.setObjectName("CM_125A")
        self.CM_125A.addItem("")
        self.CM_125A.addItem("")
        self.CM_125A.addItem("")
        self.CM_125A.addItem("")
        self.Zone11_SW.addWidget(self.CM_125A, 6, 2, 1, 1)
        self.STset_121A = QtWidgets.QSpinBox(self.tab_3)
        self.STset_121A.setMinimum(15)
        self.STset_121A.setMaximum(45)
        self.STset_121A.setObjectName("STset_121A")
        self.Zone11_SW.addWidget(self.STset_121A, 2, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setObjectName("label_18")
        self.Zone11_SW.addWidget(self.label_18, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.Zone11_SW.addWidget(self.label_11, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.Zone11_SW.addWidget(self.label_13, 1, 1, 1, 1)
        self.STset_122A = QtWidgets.QSpinBox(self.tab_3)
        self.STset_122A.setMinimum(15)
        self.STset_122A.setMaximum(45)
        self.STset_122A.setObjectName("STset_122A")
        self.Zone11_SW.addWidget(self.STset_122A, 3, 1, 1, 1)
        self.CM_121A = QtWidgets.QComboBox(self.tab_3)
        self.CM_121A.setObjectName("CM_121A")
        self.CM_121A.addItem("")
        self.CM_121A.addItem("")
        self.CM_121A.addItem("")
        self.CM_121A.addItem("")
        self.Zone11_SW.addWidget(self.CM_121A, 2, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setObjectName("label_15")
        self.Zone11_SW.addWidget(self.label_15, 2, 0, 1, 1)
        self.STset_124A = QtWidgets.QSpinBox(self.tab_3)
        self.STset_124A.setMinimum(15)
        self.STset_124A.setMaximum(45)
        self.STset_124A.setObjectName("STset_124A")
        self.Zone11_SW.addWidget(self.STset_124A, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")
        self.Zone11_SW.addWidget(self.label_12, 0, 1, 1, 1)
        self.STset_125A = QtWidgets.QSpinBox(self.tab_3)
        self.STset_125A.setMinimum(15)
        self.STset_125A.setMaximum(45)
        self.STset_125A.setObjectName("STset_125A")
        self.Zone11_SW.addWidget(self.STset_125A, 6, 1, 1, 1)
        self.CM_123A = QtWidgets.QComboBox(self.tab_3)
        self.CM_123A.setObjectName("CM_123A")
        self.CM_123A.addItem("")
        self.CM_123A.addItem("")
        self.CM_123A.addItem("")
        self.CM_123A.addItem("")
        self.Zone11_SW.addWidget(self.CM_123A, 4, 2, 1, 1)
        self.CM_12XA = QtWidgets.QComboBox(self.tab_3)
        self.CM_12XA.setObjectName("CM_12XA")
        self.CM_12XA.addItem("")
        self.CM_12XA.addItem("")
        self.CM_12XA.addItem("")
        self.CM_12XA.addItem("")
        self.Zone11_SW.addWidget(self.CM_12XA, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setObjectName("label_16")
        self.Zone11_SW.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setObjectName("label_19")
        self.Zone11_SW.addWidget(self.label_19, 6, 0, 1, 1)
        self.CM_124A = QtWidgets.QComboBox(self.tab_3)
        self.CM_124A.setObjectName("CM_124A")
        self.CM_124A.addItem("")
        self.CM_124A.addItem("")
        self.CM_124A.addItem("")
        self.CM_124A.addItem("")
        self.Zone11_SW.addWidget(self.CM_124A, 5, 2, 1, 1)
        self.CM_122A = QtWidgets.QComboBox(self.tab_3)
        self.CM_122A.setObjectName("CM_122A")
        self.CM_122A.addItem("")
        self.CM_122A.addItem("")
        self.CM_122A.addItem("")
        self.CM_122A.addItem("")
        self.Zone11_SW.addWidget(self.CM_122A, 3, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName("label_14")
        self.Zone11_SW.addWidget(self.label_14, 1, 0, 1, 1)
        self.bt_write_sidewall = QtWidgets.QPushButton(self.tab_3)
        self.bt_write_sidewall.setObjectName("bt_write_sidewall")
        self.Zone11_SW.addWidget(self.bt_write_sidewall, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.Zone11_SW, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_25.setText(_translate("MainWindow", "Surface temperature (℃)"))
        self.label_21.setText(_translate("MainWindow", "10L3"))
        self.label_22.setText(_translate("MainWindow", "Control mode"))
        self.label_26.setText(_translate("MainWindow", "10S123"))
        self.label_23.setText(_translate("MainWindow", "min. : 10℃ max.: 50℃"))
        self.label_24.setText(_translate("MainWindow", "10L1"))
        self.CM_10L3.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_10L3.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_10L3.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_10L3.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.label_28.setText(_translate("MainWindow", "Zone11_Side wall"))
        self.CM_10L1.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_10L1.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_10L1.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_10L1.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.CM_10X1.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_10X1.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_10X1.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_10X1.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.CM_10L2.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_10L2.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_10L2.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_10L2.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.CM_10S123.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_10S123.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_10S123.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_10S123.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.label_20.setText(_translate("MainWindow", "10L2"))
        self.bt_write_floor.setText(_translate("MainWindow", "Write Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Zone11_Floor"))
        self.CM_1150.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_1150.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_1150.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_1150.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.CM_1110.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_1110.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_1110.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_1110.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.label_4.setText(_translate("MainWindow", "Control mode"))
        self.CM_1130.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_1130.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_1130.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_1130.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.label_3.setText(_translate("MainWindow", "Surface temperature (℃)"))
        self.CM_1140.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_1140.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_1140.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_1140.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.label_2.setText(_translate("MainWindow", "min. : 10℃ max.: 50℃"))
        self.CM_1120.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_1120.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_1120.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_1120.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.CM_1160.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_1160.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_1160.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_1160.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.CM_11XX.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_11XX.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_11XX.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_11XX.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.label_5.setText(_translate("MainWindow", "1110"))
        self.label_6.setText(_translate("MainWindow", "1120"))
        self.label_7.setText(_translate("MainWindow", "1130"))
        self.label_8.setText(_translate("MainWindow", "1140"))
        self.label_9.setText(_translate("MainWindow", "1150"))
        self.label_10.setText(_translate("MainWindow", "1160"))
        self.label.setText(_translate("MainWindow", "Zone11_Front wall"))
        self.bt_write_frontwall.setText(_translate("MainWindow", "Write Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Zone11_FrontWall"))
        self.label_17.setText(_translate("MainWindow", "123A"))
        self.CM_125A.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_125A.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_125A.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_125A.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.label_18.setText(_translate("MainWindow", "124A"))
        self.label_11.setText(_translate("MainWindow", "Control mode"))
        self.label_13.setText(_translate("MainWindow", "min. : 10℃ max.: 50℃"))
        self.CM_121A.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_121A.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_121A.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_121A.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.label_15.setText(_translate("MainWindow", "121A"))
        self.label_12.setText(_translate("MainWindow", "Surface temperature (℃)"))
        self.CM_123A.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_123A.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_123A.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_123A.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.CM_12XA.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_12XA.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_12XA.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_12XA.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.label_16.setText(_translate("MainWindow", "122A"))
        self.label_19.setText(_translate("MainWindow", "125A"))
        self.CM_124A.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_124A.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_124A.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_124A.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.CM_122A.setItemText(0, _translate("MainWindow", "Off", "0"))
        self.CM_122A.setItemText(1, _translate("MainWindow", "Auto", "1"))
        self.CM_122A.setItemText(2, _translate("MainWindow", "Reset", "10"))
        self.CM_122A.setItemText(3, _translate("MainWindow", "Manual", "20"))
        self.label_14.setText(_translate("MainWindow", "Zone11_Side wall"))
        self.bt_write_sidewall.setText(_translate("MainWindow", "Write Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Zone11_SideWall"))
