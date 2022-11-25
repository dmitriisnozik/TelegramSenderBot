Telegram Sender Bot is a TeleBot telegram bot that sending messages with or withoud attached files and images.
In this bot you also can add signature which will be added to message depending to channel.
# Since this bot is my first python project ever, some functions can not working well

To start sending you should create a new bot account using @BotFather telegram account, that will give you token for further use
Bot is taking as list of channels input .txt file, where written down all channels separated by space or \n
To write your message you can use message field or choose .txt file with your message, if you use second way, selecting new files won't replace message, but message will apend as another one and they will be sent as different messages
To attach document or image to your image you should use relevant buttons, bot can handle only one file
If you're selected image or document, text formatting won't work and your message length is limited by 1000 symbols (including spaces, etc.), if you're out of limit message will be separated and sent as several
To add signature to your message your have to select channel list, open signature edit window, select channel from list, write signature and click 'add', if channel list in signature edit window is not updating, you need to click 'update' button
Console is used to send feedback to user (when, where and what message was sent)

If you have some questions about text formatting or bot using, you can find info in '?' button
