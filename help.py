# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
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
from PySide6.QtWidgets import (QApplication, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_help(object):
    def setupUi(self, help):
        if not help.objectName():
            help.setObjectName(u"help")
        help.resize(400, 300)
        help.setStyleSheet(u"color: white;\n"
"background-color: #121212;\n"
"font-family: 'Century Gothic';\n"
"font-size: 17px;")
        self.verticalLayout = QVBoxLayout(help)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hints_open = QPushButton(help)
        self.hints_open.setObjectName(u"hints_open")
        self.hints_open.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout.addWidget(self.hints_open)

        self.plainTextEdit = QPlainTextEdit(help)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.retranslateUi(help)

        QMetaObject.connectSlotsByName(help)
    # setupUi

    def retranslateUi(self, help):
        help.setWindowTitle(QCoreApplication.translate("help", u"Help", None))
        help.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.hints_open.setText(QCoreApplication.translate("help", u"Text formatting", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("help", u"Help:\n"
"\n"
"\n"
"You must add bot in your channels\n"
"\n"
"You can write, edit and send message using text field without selecting text file\n"
"\n"
"Length of text with photo is limited - 1000 symbols including spaces and signature\n"
"\n"
"HTML text formatting is not working with photos\n"
"\n"
"Bot can handle only one schedule request, if you need to schedule messages on different time open new bot application\n"
"\n"
"List of channels in message settings is not updating, to update list you have to close bot and open again\n"
"\n"
"Channels your add (usign file or writing manually) must be separated by space or enter\n"
"\n"
"To send text withoud photo you should ignore select path button or select not supported file\n"
"\n"
"To send message right now you should ingore schedule/delay edit button, or close it without clicking save button\n"
"\n"
"Delay between messages means time between two messages since first message sent\n"
"\n"
"Schedule means time to send first message", None))
    # retranslateUi

