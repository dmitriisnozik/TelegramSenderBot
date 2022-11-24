# -*- coding: utf8 -*-
import sys
from PyQt6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from design import Ui_TelegramBot
from token_input import Ui_Input
from signature import Ui_signatureform
from help import Ui_help
from hints import Ui_hints
from token_help import Ui_tokenhelpform
from PySide6.QtGui import QFontDatabase
import telebot
import os.path
from datetime import datetime

#Data folder creation
try:
    os.mkdir('data')
except Exception:
    pass

# Token storage creation
try:
    token_r = open('data/temp_token.txt')
except Exception: 
    token_c = open('data/temp_token.txt', 'w')
    token_c.write('default')
    token_r = open('data/temp_token.txt')

# Token
bot = telebot.TeleBot(token_r.read())

# Message
message_c = open('data/temp_message.txt', 'w')

# Channel list storage
try: 
    channels_r = open('data/temp_channels.txt')
except Exception:
    channels_c = open('data/temp_channels.txt', 'w')
    channels_c.write('default')
    channels_r = open('data/temp_channels.txt')

# Signature storage
try: 
    sign_r = open('data/temp_signature.txt')
    open('data/signaturedata.txt')
except Exception:
    open('data/signaturedata.txt', 'w').write('')
    sign_c = open('data/temp_signature.txt', 'w')
    sign_c.write('')
    sign_r = open('data/temp_signature.txt')

# Keys storage
try: 
    keys_r = open('data/signature_keys.txt')
except Exception:
    keys_c = open('data/signature_keys.txt', 'w')
    keys_c.write('')
    keys_r = open('data/signature_keys.txt')


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
        token_file = open('data/temp_token.txt', 'w')
        token_file.write(token_file_text)  # Save token to file
        window.show()
        widget.close()


# Help window
class helpWindow(QWidget):
    def __init__(self):
        super(helpWindow, self).__init__()
        self.ui = Ui_help()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Century-Gothic.ttf")

        self.ui.hints_open.clicked.connect(self.open_hints)
    
    def open_hints(self):
        hints.show()


# Text formatting hints
class hintsWindow(QWidget):
    def __init__(self):
        super(hintsWindow, self).__init__()
        self.ui = Ui_hints()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Century-Gothic.ttf")


# Token help window (what token is)
class tokenHelp(QWidget):
    def __init__(self):
        super(tokenHelp, self).__init__()
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

        list_path = open('data/temp_channels.txt')  # Getting channel names list
        list_name = (list_path.read())
        list_name = list_name.replace('\n', ' ').replace('  ', ' ')
        list_name = list_name.split(' ')  # Extracting channel names
        self.ui.channel_select.clear()
        for i in range(len(list_name)):
            self.ui.channel_select.insertItem(86400, list_name[i])

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
        exist_keys = open('data/signature_keys.txt').read()
        open('data/signature_keys.txt', 'w').write(exist_keys + ':::' + new_key)
        new_signature = self.ui.sign_input.toPlainText()
        exist_signatures = open('data/temp_signature.txt', 'r').read()
        open('data/temp_signature.txt', 'w').write(exist_signatures + ':::' + new_signature)

    # Delete all signatures
    def clicked_clear(self):
        self.ui.read_only.clear()
        open('data/temp_signature.txt', 'w').write('')
        open('data/signature_keys.txt', 'w').write('')

    # Update list of channels
    def update(self):
        self.ui.channel_select.clear()
        list_path = open('data/temp_channels.txt')
        list_name = (list_path.read())
        list_name = list_name.replace('\n', ' ')
        list_name = list_name.replace('  ', ' ')
        data = open('data/temp_channels.txt', 'w').write(list_name)
        list_name = open('data/temp_channels.txt').read()
        list_name = list_name.split(' ')
        self.ui.channel_select.clear()
        for i in range(len(list_name)):
            self.ui.channel_select.insertItem(86400, list_name[i])

    def clicked_save(self):
        signatureedit.close()


# Main menu
class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_TelegramBot()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("fonts/Century-Gothic.ttf")

        # Getting bot token from file in data
        token_str = open('data/temp_token.txt').read()
        token_str = token_str.split(':')
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
        channel_names = open('data/temp_channels.txt')
        global channel_name
        channel_name = (channel_names.read())
        channel_name = channel_name.replace('\n', ' ')
        channel_name = channel_name.replace('  ', ' ')
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
        except Exception:
            image = ''

        # Making sure if file is selected
        try:
            doc_arr = str(doc_path).split('\'')
            doc = doc_arr[1]
        except Exception:
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
        textfilename = QFileDialog.getOpenFileName()
        global text_path 
        text_path = open(textfilename[0], encoding='UTF-8')
        self.ui.text_show.insertPlainText(text_path.read())  # Showing message in message field

    def select_document(self):
        docfilename = QFileDialog.getOpenFileName()
        global doc_path
        doc_path = open(docfilename[0])
        doc_text = str(doc_path).split('\'')
        doc_text = doc_text[1].split('/')  # Extracting document name
        self.ui.image_input.setText('File selected')  # Change button text
        self.ui.selected_.setText(f'Doc: {doc_text[-1]}')  # Showing selected document name
        print(doc_path)

    def open_image(self):
        imagefilename = QFileDialog.getOpenFileName()
        global image_path
        image_path = open(imagefilename[0])
        image_text = str(image_path).split('\'')
        image_text = image_text[1].split('/')  # Extracting image name
        self.ui.image_input.setText('File selected')  # Change button text
        self.ui.selected_.setText(f'Img: {image_text[-1]}')  # Showing selected image name

    def open_list(self):
        listfilename = QFileDialog.getOpenFileName()
        global list_path
        list_path = open(listfilename[0])
        channel_name = (list_path.read())
        channel_name = channel_name.replace('\n', ' ')
        channel_name = channel_name.replace('  ', ' ')
        channels_c = open('data/temp_channels.txt', 'w')  # Saving channel list in temp file in data
        channels_c.write(channel_name)
        channel_name = channel_name.split(' ')  # Extracting channel names
        self.ui.channels_output.clear()
        for i in range(len(channel_name)):
            self.ui.channels_output.insertPlainText(f'{channel_name[i]}\n')
        self.ui.ch_amount.setText(f'Amount: {len(channel_name)}')  # Change text of channel counter

    def message_sign(self):
        signatureedit.show()

    def help_open(self):
        help.show()

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
    signatureedit = SignatureEdit()
    help = helpWindow()
    hints = hintsWindow()
    token_help = tokenHelp()

    token_file = open('data/temp_token.txt')
    if ':' not in token_file.read():  # Make sure if bot token in data
        widget.show()
    else:
        window.show()

    sys.exit(app.exec())
