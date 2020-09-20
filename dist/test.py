# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'style.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        MainWindow.setStyleSheet(u"\n"
"	background-color: #312C3A;\n"
"	color: #fff;\n"
"	opacity: 0;\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 701, 41))
        self.label_2.setStyleSheet(u"font-size: 16px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.add_member_button = QPushButton(self.centralwidget)
        self.add_member_button.setObjectName(u"add_member_button")
        self.add_member_button.setGeometry(QRect(320, 440, 141, 31))
        self.add_member_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_member_button.setStyleSheet(u"QPushButton{\n"
"background-color: #221F33;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #585470;\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 310, 261, 151))
        self.input_name = QLineEdit(self.widget)
        self.input_name.setObjectName(u"input_name")
        self.input_name.setGeometry(QRect(0, 0, 261, 31))
        self.input_name.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.input_kind = QLineEdit(self.widget)
        self.input_kind.setObjectName(u"input_kind")
        self.input_kind.setGeometry(QRect(0, 40, 261, 31))
        self.input_kind.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.input_status = QLineEdit(self.widget)
        self.input_status.setObjectName(u"input_status")
        self.input_status.setGeometry(QRect(0, 80, 261, 31))
        self.input_status.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.input_place = QLineEdit(self.widget)
        self.input_place.setObjectName(u"input_place")
        self.input_place.setGeometry(QRect(0, 120, 261, 31))
        self.input_place.setStyleSheet(u"background-color: #fff;\n"
"color: #000;")
        self.clear_all_button = QPushButton(self.centralwidget)
        self.clear_all_button.setObjectName(u"clear_all_button")
        self.clear_all_button.setGeometry(QRect(490, 430, 171, 31))
        self.clear_all_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_all_button.setStyleSheet(u"QPushButton{\n"
"background-color: #221F33;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #705454;\n"
"}")
        self.load_button = QPushButton(self.centralwidget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setGeometry(QRect(490, 390, 171, 31))
        self.load_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.load_button.setStyleSheet(u"QPushButton{\n"
"background-color: #221F33;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #585470;\n"
"}")
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(490, 350, 171, 31))
        self.save_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_button.setStyleSheet(u"QPushButton{\n"
"background-color: #221F33;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #585470;\n"
"}")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(30, 50, 631, 251))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(49, 44, 58, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setStyleSheet(u"QTableWidget#tableWidget QHeaderView::section{color: #fff; background-color: #585470;}\n"
"QTableWidget#tableWidget{color: #fff;}")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(153)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(153)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 310, 161, 71))
        self.label.setStyleSheet(u"background-color: #585470;\n"
"border: 1px solid black;")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0434\u043b\u044f \u0432\u0432\u043e\u0434\u0430, \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0430 \u0438 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e \u0436\u0438\u0432\u043e\u0442\u043d\u044b\u0445 \u0432 \u0437\u043e\u043e\u043f\u0430\u0440\u043a\u0435", None))
        self.add_member_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.input_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.input_kind.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434", None))
        self.input_status.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.input_place.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e", None))
        self.clear_all_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0431\u0430\u0437\u0443", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e", None));
        self.label.setText("")
    # retranslateUi

