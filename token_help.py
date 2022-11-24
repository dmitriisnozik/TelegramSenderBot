# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'token_help.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_tokenhelpform(object):
    def setupUi(self, tokenhelpform):
        if not tokenhelpform.objectName():
            tokenhelpform.setObjectName(u"tokenhelpform")
        tokenhelpform.resize(469, 70)
        tokenhelpform.setStyleSheet(u"color: white;\n"
"background-color: #121212;\n"
"font-family: 'Century Gothic';\n"
"font-size: 15px;")
        self.label = QLabel(tokenhelpform)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 471, 51))

        self.retranslateUi(tokenhelpform)

        QMetaObject.connectSlotsByName(tokenhelpform)
    # setupUi

    def retranslateUi(self, tokenhelpform):
        tokenhelpform.setWindowTitle(QCoreApplication.translate("tokenhelpform", u"Token Help", None))
        tokenhelpform.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.label.setText(QCoreApplication.translate("tokenhelpform", u"To get your bot token you have to write @BotFather in telegram", None))
    # retranslateUi

