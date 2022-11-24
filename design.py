# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'darkdesign.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_TelegramBot(object):
    def setupUi(self, TelegramBot):
        if not TelegramBot.objectName():
            TelegramBot.setObjectName(u"TelegramBot")
        TelegramBot.resize(887, 600)
        TelegramBot.setStyleSheet(u"color: white;\n"
"background-color: #121212;\n"
"font-family: 'Century Gothic';\n"
"font-size: 17px;\n"
"")
        self.centralwidget = QWidget(TelegramBot)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout.addWidget(self.label_8)

        self.change_token = QPushButton(self.centralwidget)
        self.change_token.setObjectName(u"change_token")
        self.change_token.setCursor(QCursor(Qt.PointingHandCursor))
        self.change_token.setStyleSheet(u"font-weight: bold;\n"
"background-color: #0a0a0a;")

        self.verticalLayout.addWidget(self.change_token)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.console_output = QPlainTextEdit(self.centralwidget)
        self.console_output.setObjectName(u"console_output")
        self.console_output.setMaximumSize(QSize(200, 16777215))
        self.console_output.setReadOnly(True)

        self.horizontalLayout.addWidget(self.console_output)

        self.text_show = QPlainTextEdit(self.centralwidget)
        self.text_show.setObjectName(u"text_show")
        self.text_show.setMaximumSize(QSize(16777215, 16777215))
        self.text_show.setStyleSheet(u"background-color: #0a0a0a;")

        self.horizontalLayout.addWidget(self.text_show)

        self.channels_output = QPlainTextEdit(self.centralwidget)
        self.channels_output.setObjectName(u"channels_output")
        self.channels_output.setMaximumSize(QSize(150, 16777215))
        self.channels_output.setStyleSheet(u"")
        self.channels_output.setReadOnly(True)

        self.horizontalLayout.addWidget(self.channels_output)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.selected_ = QLabel(self.centralwidget)
        self.selected_.setObjectName(u"selected_")
        self.selected_.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_4.addWidget(self.selected_)

        self.msg_amount = QLabel(self.centralwidget)
        self.msg_amount.setObjectName(u"msg_amount")

        self.horizontalLayout_4.addWidget(self.msg_amount)

        self.amount_box = QSpinBox(self.centralwidget)
        self.amount_box.setObjectName(u"amount_box")
        self.amount_box.setMinimum(1)

        self.horizontalLayout_4.addWidget(self.amount_box)

        self.ch_amount = QLabel(self.centralwidget)
        self.ch_amount.setObjectName(u"ch_amount")
        self.ch_amount.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_4.addWidget(self.ch_amount)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.est_time = QLabel(self.centralwidget)
        self.est_time.setObjectName(u"est_time")
        self.est_time.setMinimumSize(QSize(0, 50))
        self.est_time.setMaximumSize(QSize(16777215, 16777215))
        self.est_time.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.est_time)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.attach_file = QPushButton(self.centralwidget)
        self.attach_file.setObjectName(u"attach_file")
        self.attach_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.attach_file.setStyleSheet(u"background-color: #0a0a0a;")

        self.gridLayout.addWidget(self.attach_file, 0, 4, 1, 1)

        self.channel_input = QPushButton(self.centralwidget)
        self.channel_input.setObjectName(u"channel_input")
        self.channel_input.setCursor(QCursor(Qt.PointingHandCursor))
        self.channel_input.setStyleSheet(u"background-color: #0a0a0a;")

        self.gridLayout.addWidget(self.channel_input, 0, 3, 1, 1)

        self.message_settings = QPushButton(self.centralwidget)
        self.message_settings.setObjectName(u"message_settings")
        self.message_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.message_settings.setStyleSheet(u"background-color: #0a0a0a;")

        self.gridLayout.addWidget(self.message_settings, 0, 2, 1, 1)

        self.image_input = QPushButton(self.centralwidget)
        self.image_input.setObjectName(u"image_input")
        self.image_input.setCursor(QCursor(Qt.PointingHandCursor))
        self.image_input.setStyleSheet(u"background-color: #0a0a0a;")

        self.gridLayout.addWidget(self.image_input, 0, 0, 1, 1)

        self.message = QPushButton(self.centralwidget)
        self.message.setObjectName(u"message")
        self.message.setCursor(QCursor(Qt.PointingHandCursor))
        self.message.setStyleSheet(u"background-color: #0a0a0a;")

        self.gridLayout.addWidget(self.message, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.close = QPushButton(self.centralwidget)
        self.close.setObjectName(u"close")
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.setStyleSheet(u"font-weight: bold;\n"
"background-color: #0a0a0a;")

        self.horizontalLayout_5.addWidget(self.close)

        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        self.start.setCursor(QCursor(Qt.PointingHandCursor))
        self.start.setStyleSheet(u"font-weight: bold;\n"
"background-color: #0a0a0a;")

        self.horizontalLayout_5.addWidget(self.start)

        self.help = QPushButton(self.centralwidget)
        self.help.setObjectName(u"help")
        self.help.setCursor(QCursor(Qt.PointingHandCursor))
        self.help.setStyleSheet(u"font-weight: bold;\n"
"background-color: #0a0a0a;")

        self.horizontalLayout_5.addWidget(self.help)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        TelegramBot.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelegramBot)

        QMetaObject.connectSlotsByName(TelegramBot)
    # setupUi

    def retranslateUi(self, TelegramBot):
        TelegramBot.setWindowTitle(QCoreApplication.translate("TelegramBot", u"Telegram Bot", None))
        TelegramBot.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.label.setText(QCoreApplication.translate("TelegramBot", u"Telegram Bot", None))
        self.label_8.setText("")
        self.change_token.setText(QCoreApplication.translate("TelegramBot", u"Change bot token", None))
        self.label_2.setText(QCoreApplication.translate("TelegramBot", u"Console", None))
        self.label_3.setText(QCoreApplication.translate("TelegramBot", u"Messages", None))
        self.label_4.setText(QCoreApplication.translate("TelegramBot", u"Channels", None))
        self.selected_.setText(QCoreApplication.translate("TelegramBot", u"Img:", None))
        self.msg_amount.setText(QCoreApplication.translate("TelegramBot", u"Repeats amount:", None))
        self.ch_amount.setText(QCoreApplication.translate("TelegramBot", u"Amount:", None))
        self.est_time.setText("")
        self.attach_file.setText(QCoreApplication.translate("TelegramBot", u"Attach File", None))
        self.channel_input.setText(QCoreApplication.translate("TelegramBot", u"Channels", None))
        self.message_settings.setText(QCoreApplication.translate("TelegramBot", u"Signature", None))
        self.image_input.setText(QCoreApplication.translate("TelegramBot", u"Image", None))
        self.message.setText(QCoreApplication.translate("TelegramBot", u"Message", None))
        self.close.setText(QCoreApplication.translate("TelegramBot", u"Close", None))
        self.start.setText(QCoreApplication.translate("TelegramBot", u"Start", None))
        self.help.setText(QCoreApplication.translate("TelegramBot", u"?", None))
    # retranslateUi

