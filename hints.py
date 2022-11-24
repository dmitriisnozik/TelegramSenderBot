# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hints.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_hints(object):
    def setupUi(self, hints):
        if not hints.objectName():
            hints.setObjectName(u"hints")
        hints.resize(566, 300)
        hints.setStyleSheet(u"color: white;\n"
"background-color: #121212;\n"
"font-family: 'Century Gothic';\n"
"font-size: 18px;")
        self.verticalLayout = QVBoxLayout(hints)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(hints)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font-size: 15px;")

        self.verticalLayout.addWidget(self.label_6)

        self.label = QLabel(hints)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(hints)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(hints)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font-size:15px;")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(hints)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(hints)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setItalic(True)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"font-size:15px;")

        self.verticalLayout.addWidget(self.label_5)

        self.label_7 = QLabel(hints)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(hints)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font-size: 15px;")

        self.verticalLayout.addWidget(self.label_8)

        self.label_10 = QLabel(hints)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.label_9 = QLabel(hints)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)


        self.retranslateUi(hints)

        QMetaObject.connectSlotsByName(hints)
    # setupUi

    def retranslateUi(self, hints):
        hints.setWindowTitle(QCoreApplication.translate("hints", u"Help", None))
        hints.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.label_6.setText(QCoreApplication.translate("hints", u"Bot is using HTML parse mode", None))
        self.label.setText(QCoreApplication.translate("hints", u"Text formatting hints", None))
        self.label_2.setText(QCoreApplication.translate("hints", u"<html><head/><body><p>Use &lt;b&gt;&lt;/b&gt; for bold</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("hints", u"<html><head/><body><p><span style=\" font-weight:400;\">&lt;b&gt;bold&lt;/b&gt; = </span>bold</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("hints", u"<html><head/><body><p>Use &lt;i&gt;&lt;/i&gt; for italic</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("hints", u"<html><head/><body><p><span style=\" font-style:normal;\">&lt;i&gt;italic&lt;/i&gt;</span> = italic</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("hints", u"<html><head/><body><p><span style=\" font-size:14pt;\">Use &lt;u&gt;&lt;/u&gt; for underline</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("hints", u"<html><head/><body><p><span style=\" font-size:11pt;\">&lt;u&gt;underline&lt;/u&gt; = </span><span style=\" font-size:11pt; text-decoration: underline;\">underline</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("hints", u"<html><head/><body><p><span style=\" font-size:14pt;\">Use &lt;del&gt;&lt;/del&gt; for strikethrough text</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("hints", u"<html><head/><body><p><span style=\" font-size:14pt;\">Use &lt;a href=your site here&gt;your text here&lt;/a&gt; to add link</span></p></body></html>", None))
    # retranslateUi

