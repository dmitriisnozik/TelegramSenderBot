# -*- coding: utf8 -*-
import sys
from PyQt6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QFontDatabase
from styles.design import Ui_TelegramBot
from styles.token_input import Ui_Input
from styles.signature import Ui_signatureform
from styles.help import Ui_help
from styles.hints import Ui_hints
from styles.token_help import Ui_tokenhelpform
import telebot
import os.path
from datetime import datetime

# Data folder creation
try:
    os.mkdir('data')
except FileExistsError:
    pass


# Storage opening/creating function
def open_storage(path):
    try:
        open(path)
    except FileNotFoundError:
        open(path, 'w').write('')


# Data storage files check/creation
open_storage('data/temp_token.txt')
open_storage('data/temp_message.txt')
open_storage('data/temp_channels.txt')
open_storage('data/temp_signature.txt')
open_storage('data/signature_keys.txt')

# Token
bot = telebot.TeleBot(open('data/temp_token.txt').read())


# Token input/change window
class InputWindow(QWidget):
    def __init__(self):
        super(InputWindow, self).__init__()
        self.ui = Ui_Input()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("fonts/Century-Gothic.ttf")

        self.ui.widgetButton.clicked.connect(self.submit)
        self.ui.tokenhelp.clicked.connect(self.open_help)

    def open_help(self):
        token_help.show()
    
    def submit(self):
        token_file_text = self.ui.widgetLineEdit.text()
        open('data/temp_token.txt', 'w').write(token_file_text)  # Save token to file
        window.show()
        widget.close()


# Help window
class HelpWindow(QWidget):
    def __init__(self):
        super(HelpWindow, self).__init__()
        self.ui = Ui_help()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Century-Gothic.ttf")

        self.ui.hints_open.clicked.connect(self.open_hints)
    
    def open_hints(self):
        hints.show()


# Text formatting hints
class HintsWindow(QWidget):
    def __init__(self):
        super(HintsWindow, self).__init__()
        self.ui = Ui_hints()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Century-Gothic.ttf")


# Token help window (what token is)
class TokenHelp(QWidget):
    def __init__(self):
        super(TokenHelp, self).__init__()
        self.ui = Ui_tokenhelpform()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Century-Gothic.ttf")


# Signature edit window
class SignatureEdit(QWidget):
    def __init__(self):
        super(SignatureEdit, self).__init__()
        self.ui = Ui_signatureform()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("fonts/Century-Gothic.ttf")

        self.ui.label.setText('Add signature:')

        # Buttons description
        self.ui.add_button.clicked.connect(self.clicked_add)
        self.ui.save_button.clicked.connect(self.clicked_save)
        self.ui.clear_button.clicked.connect(self.clicked_clear)
        self.ui.update_button.clicked.connect(self.update)

        list_name = (open('data/temp_channels.txt').read()).replace('\n', ' ').replace('  ', ' ')
        list_name = list_name.split(' ')  # Extracting channel names
        self.ui.channel_select.clear()
        for name in list_name:
            self.ui.channel_select.insertItem(86400, name)

        # Show signatures from list in data
        signature_file = open('data/temp_signature.txt').read()
        keys_file = open('data/signature_keys.txt').read()
        signature_list = signature_file.split(':::')
        signature_list.remove('')
        keys_list = keys_file.split(':::')
        keys_list.remove('')
        for i in range(len(keys_list)):
            self.ui.read_only.appendPlainText(f'{keys_list[i]} : {signature_list[i]}')

    # Add signature to list
    def clicked_add(self):
        self.ui.read_only.appendPlainText(
            f'{self.ui.channel_select.currentText()} : {self.ui.sign_input.toPlainText()}'
        )
        new_key = self.ui.channel_select.currentText()
        open('data/signature_keys.txt', 'a').write(':::' + new_key)
        new_signature = self.ui.sign_input.toPlainText()
        open('data/temp_signature.txt', 'a').write(':::' + new_signature)

    # Delete all signatures
    def clicked_clear(self):
        self.ui.read_only.clear()
        try:
            open('data/temp_signature.txt', 'w').write('')
            open('data/signature_keys.txt', 'w').write('')
        except FileNotFoundError:
            open_storage('data/temp_signature.txt')

    # Update list of channels
    def update(self):
        self.ui.channel_select.clear()
        try:
            list_name = (open('data/temp_channels.txt').read()).replace('\n', ' ').replace('  ', ' ')
            open('data/temp_channels.txt', 'w').write(list_name)  # Channel list transformation
            list_name = (open('data/temp_channels.txt').read()).split(' ')
            for i in range(len(list_name)):
                self.ui.channel_select.insertItem(86400, list_name[i])
        except FileNotFoundError:
            open_storage('data/temp_channels.txt')

    def clicked_save(self):
        signature_edit.close()


# Main menu
class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_TelegramBot()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("fonts/Century-Gothic.ttf")

        # Getting bot token from file in data
        token_str = (open('data/temp_token.txt').read()).split(':')
        self.ui.label_8.setText(f'Current token: {token_str[0]}')

        # Buttons description
        self.ui.message.clicked.connect(self.open_text)
        self.ui.channel_input.clicked.connect(self.open_list)
        self.ui.image_input.clicked.connect(self.open_image)
        self.ui.start.clicked.connect(self.launch)
        self.ui.change_token.clicked.connect(self.token_change)
        self.ui.message_settings.clicked.connect(self.message_sign)
        self.ui.attach_file.clicked.connect(self.select_document)
        self.ui.help.clicked.connect(self.help_open)
        self.ui.close.clicked.connect(self.close_)

    # Start sending messages
    def launch(self):
        channel_name = (open('data/temp_channels.txt').read()).replace('\n', ' ').replace('  ', ' ')
        channel_name = channel_name.split(' ')  # Extracting channel names
        signature_file = open('data/temp_signature.txt').read()  # Getting signature text
        keys_file = open('data/signature_keys.txt').read()  # Getting channels with signature list
        signature_list = signature_file.split(':::')
        signature_list.remove('')  # Extracting signatures
        keys_list = keys_file.split(':::')
        keys_list.remove('')  # Extracting channels with signature

        # Making sure if image is selected
        try:
            image_arr = str(image_path).split('\'')
            image = image_arr[1]
        except NameError:
            image = ''

        # Making sure if file is selected
        try:
            doc_arr = str(doc_path).split('\'')
            doc = doc_arr[1]
        except NameError:
            doc = ''

        message = self.ui.text_show.toPlainText()  # Getting message from field
        amount = self.ui.amount_box.text()  # Getting messages amount from field

        for i in range(int(amount)):
            for j in range(len(channel_name)):      
                if image:
                    handle_text_photo(channel_name[j], message, image, signature_list, keys_list) 
                    console_datetime = datetime.now().strftime('%d-%m-%Y %H:%M')
                    self.ui.console_output.appendPlainText(
                        f'{console_datetime} | {channel_name[j]}, message {i+1} sent with photo'
                    )  # Sending feedback in console field
                elif doc:
                    handle_document(channel_name[j], message, doc, signature_list, keys_list)
                    console_datetime = datetime.now().strftime('%d-%m-%Y %H:%M')
                    self.ui.console_output.appendPlainText(
                        f'{console_datetime} | {channel_name[j]}, message {i+1} sent with file'
                    )  # Sending feedback in console field
                else:
                    only_text(channel_name[j], message, signature_list, keys_list)
                    console_datetime = datetime.now().strftime('%d-%m-%Y %H:%M')
                    self.ui.console_output.appendPlainText(
                        f'{console_datetime} | {channel_name[j]}, message {i+1} sent without photo or file'
                    )  # Sending feedback in console field

    # Menu buttons
    def open_text(self):
        text_file_name = QFileDialog.getOpenFileName()
        self.ui.text_show.insertPlainText(
            open(text_file_name[0], encoding='UTF-8').read()
        )  # Showing message in message field

    def select_document(self):
        doc_file_name = QFileDialog.getOpenFileName()
        global doc_path
        try:
            doc_path = open(doc_file_name[0])
            doc_text = str(doc_path).split('\'')
            doc_text = doc_text[1].split('/')  # Extracting document name
            self.ui.attach_file.setText('File selected')  # Change button text
            self.ui.selected_.setText(f'Doc: {doc_text[-1]}')  # Showing selected document name
        except FileNotFoundError:
            pass

    def open_image(self):
        image_file_name = QFileDialog.getOpenFileName()
        global image_path
        try:
            image_path = open(image_file_name[0])
            image_text = str(image_path).split('\'')
            image_text = image_text[1].split('/')  # Extracting image name
            self.ui.image_input.setText('File selected')  # Change button text
            self.ui.selected_.setText(f'Img: {image_text[-1]}')  # Showing selected image name
        except FileNotFoundError:
            pass

    def open_list(self):
        list_file_name = QFileDialog.getOpenFileName()
        try:
            channel_name = (open(list_file_name[0])).read().replace('\n', ' ').replace('  ', ' ')
            open('data/temp_channels.txt', 'w').write(channel_name)  # Saving channel list in temp file in data
            channel_name = channel_name.split(' ')  # Extracting channel names
            self.ui.channels_output.clear()
            for i in range(len(channel_name)):
                self.ui.channels_output.insertPlainText(f'{channel_name[i]}\n')
            self.ui.ch_amount.setText(f'Amount: {len(channel_name)}')  # Change text of channel counter
        except FileNotFoundError:
            pass

    def message_sign(self):
        signature_edit.show()

    def help_open(self):
        help_.show()

    def close_(self):
        window.close()

    def token_change(self):
        window.close()
        widget.show()


# Bot functions
# Sending message with picture
@bot.message_handler(content_types=["text", "photo"])
def handle_text_photo(channel_name, message, image, signature_list, keys_list): 
    if channel_name in keys_list:  # Checking if channel name in list of channels with signature
        sign_index = keys_list.index(channel_name)
        message = message + '\n\n' + signature_list[sign_index]
        bot.send_photo(channel_name, open(image, 'rb'), caption=(message, parse_mode := 'HTML'))
    else:
        bot.send_photo(channel_name, open(image, 'rb'), caption=(message, parse_mode := 'HTML'))


# Sending message with attached file
def handle_document(channel_name, message, doc, signature_list, keys_list):
    if channel_name in keys_list:  # Checking if channel name in list of channels with signature
        sign_index = keys_list.index(channel_name)
        message = message + '\n\n' + signature_list[sign_index]
        bot.send_document(channel_name, open(doc, 'rb'), caption=(message, parse_mode := 'HTML'))
    else:
        bot.send_document(channel_name, open(doc, 'rb'), caption=(message, parse_mode := 'HTML'))


# Sending message without any file or picture
def only_text(channel_name, message, signature_list, keys_list):
    if channel_name in keys_list:  # Checking if channel name in list of channels with signature
        sign_index = keys_list.index(channel_name)
        message = message + '\n\n' + signature_list[sign_index]
        bot.send_message(channel_name, message, parse_mode := 'HTML')
    else:
        bot.send_message(channel_name, message, parse_mode := 'HTML')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    widget = InputWindow()
    window = Main()
    signature_edit = SignatureEdit()
    help_ = HelpWindow()
    hints = HintsWindow()
    token_help = TokenHelp()

    token_file = open('data/temp_token.txt')
    if ':' not in token_file.read():  # Make sure if bot token in data
        widget.show()
    else:
        window.show()

    sys.exit(app.exec())
