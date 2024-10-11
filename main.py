import telebot
from config import token
from maps import plate_draw, mall_draw

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    welcome_text = (
        "Привет! Я твой бот.\n"
        "Доступные команды:\n"
        "/plate <цвет> - Получить изображение 'plate' с маркерами цвета <цвет>\n"
        "/mall <цвет> - Получить изображение 'mall' с маркерами цвета <цвет>"
    )
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=["plate"])
def plate(message):
    args = message.text.split()
    color = args[1] if len(args) > 1 else 'red'  
    plate_draw(marker_color=color)  
    with open("out.png", "rb") as f:
        bot.send_photo(message.chat.id, f)

    
@bot.message_handler(commands=["mall"])
def mall(message):
    args = message.text.split()
    color = args[1] if len(args) > 1 else 'blue'  
    mall_draw(marker_color=color)  
    with open("out1.png", "rb") as f:
        bot.send_photo(message.chat.id, f)

bot.polling(non_stop=True)
