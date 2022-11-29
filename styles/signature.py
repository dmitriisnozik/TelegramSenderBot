# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signatureform.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtGui
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_signatureform(object):
    def setupUi(self, signatureform):
        if not signatureform.objectName():
            signatureform.setObjectName(u"signatureform")
        signatureform.resize(425, 350)
        signatureform.setStyleSheet(u"color: white;\n"
"background-color: #121212;\n"
"font-family: 'Century Gothic';\n"
"font-size: 15px;")
        self.verticalLayout_2 = QVBoxLayout(signatureform)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(signatureform)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.read_only = QPlainTextEdit(signatureform)
        self.read_only.setObjectName(u"read_only")
        self.read_only.setReadOnly(True)

        self.gridLayout.addWidget(self.read_only, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.channel_select = QComboBox(signatureform)
        self.channel_select.setObjectName(u"channel_select")
        self.channel_select.setMinimumSize(QSize(200, 45))
        self.channel_select.setMaximumSize(QSize(200, 45))

        self.horizontalLayout.addWidget(self.channel_select)

        self.sign_input = QPlainTextEdit(signatureform)
        self.sign_input.setObjectName(u"sign_input")
        self.sign_input.setMaximumSize(QSize(200, 50))

        self.horizontalLayout.addWidget(self.sign_input)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_button = QPushButton(signatureform)
        self.add_button.setObjectName(u"add_button")

        self.verticalLayout.addWidget(self.add_button)

        self.update_button = QPushButton(signatureform)
        self.update_button.setObjectName(u"update_button")

        self.verticalLayout.addWidget(self.update_button)

        self.clear_button = QPushButton(signatureform)
        self.clear_button.setObjectName(u"clear_button")

        self.verticalLayout.addWidget(self.clear_button)

        self.save_button = QPushButton(signatureform)
        self.save_button.setObjectName(u"save_button")

        self.verticalLayout.addWidget(self.save_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(signatureform)

        QMetaObject.connectSlotsByName(signatureform)
    # setupUi

    def retranslateUi(self, signatureform):
        signatureform.setWindowTitle(QCoreApplication.translate("signatureform", u"Add signature", None))
        signatureform.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.label.setText(QCoreApplication.translate("signatureform", u"Add signature:", None))
        self.add_button.setText(QCoreApplication.translate("signatureform", u"Add", None))
        self.update_button.setText(QCoreApplication.translate("signatureform", u"Update", None))
        self.clear_button.setText(QCoreApplication.translate("signatureform", u"Clear", None))
        self.save_button.setText(QCoreApplication.translate("signatureform", u"Save", None))
    # retranslateUi

