from telebot import TeleBot

from config import settings

bot = TeleBot(settings.TELEGRAM_TOKEN)


bot.send_message("881234428", "привет")