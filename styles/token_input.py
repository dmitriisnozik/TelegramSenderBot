# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'token_input.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Input(object):
    def setupUi(self, Input):
        if not Input.objectName():
            Input.setObjectName(u"Input")
        Input.resize(300, 125)
        Input.setMinimumSize(QSize(300, 125))
        Input.setMaximumSize(QSize(300, 125))
        Input.setStyleSheet(u"color: white;\n"
"background-color: #121212;\n"
"font-family: 'Century Gothic';\n"
"font-size: 20px;")
        self.verticalLayout_2 = QVBoxLayout(Input)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.widgetLabel = QLabel(Input)
        self.widgetLabel.setObjectName(u"widgetLabel")

        self.horizontalLayout.addWidget(self.widgetLabel)

        self.tokenhelp = QPushButton(Input)
        self.tokenhelp.setObjectName(u"tokenhelp")
        self.tokenhelp.setMaximumSize(QSize(30, 16777215))
        self.tokenhelp.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout.addWidget(self.tokenhelp)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widgetLineEdit = QLineEdit(Input)
        self.widgetLineEdit.setObjectName(u"widgetLineEdit")

        self.verticalLayout.addWidget(self.widgetLineEdit)

        self.widgetButton = QPushButton(Input)
        self.widgetButton.setObjectName(u"widgetButton")
        self.widgetButton.setStyleSheet(u"font-weight: bold;\n"
"letter-spacing: 1px;")

        self.verticalLayout.addWidget(self.widgetButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Input)

        QMetaObject.connectSlotsByName(Input)
    # setupUi

    def retranslateUi(self, Input):
        Input.setWindowTitle(QCoreApplication.translate("Input", u"Select Token", None))
        Input.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.widgetLabel.setText(QCoreApplication.translate("Input", u"Type your bot token here", None))
        self.tokenhelp.setText(QCoreApplication.translate("Input", u"?", None))
        self.widgetButton.setText(QCoreApplication.translate("Input", u"Submit", None))
    # retranslateUi

