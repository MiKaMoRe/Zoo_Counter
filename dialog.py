# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 150)
        Dialog.setMinimumSize(QSize(320, 150))
        Dialog.setMaximumSize(QSize(320, 150))
        Dialog.setStyleSheet(u"background-color: #fff;\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 281, 61))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.accept = QPushButton(Dialog)
        self.accept.setObjectName(u"accept")
        self.accept.setGeometry(QRect(50, 100, 75, 23))
        self.accept.setCursor(QCursor(Qt.PointingHandCursor))
        self.accept.setStyleSheet(u"background-color: #5a191a;\n"
"color: #fff;")
        self.reject = QPushButton(Dialog)
        self.reject.setObjectName(u"reject")
        self.reject.setGeometry(QRect(180, 100, 75, 23))
        self.reject.setCursor(QCursor(Qt.PointingHandCursor))
        self.reject.setStyleSheet(u"background-color: #21a31e;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u0441\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u0432\u0430\u0448\u0438\u0445 \u0436\u0438\u0432\u043e\u0442\u043d\u044b\u0445?", None))
        self.accept.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430", None))
        self.reject.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442", None))
    # retranslateUi

