from telebot import TeleBot

from config import settings


def send_message(habit):
    """Отправка сообщения в ТГ"""
    bot = TeleBot(settings.TELEGRAM_TOKEN)
    reward = ""
    if habit.related_habit:
        reward = f"\n\nЧё кого?\nСходи ка в место под названием {habit.related_habit.place}\n и можешь {habit.related_habit.action}\n" \
                 f"Это займёт у тебя {habit.related_habit.time_to_complete}"
    elif habit.award:
        reward = f"\n\nМои congratulations, пёс\nТвоя награда: {habit.award}"

    text = f"Ё, сап человек с почтой: {habit.user.email}\nТы ничего не забыл? Например пойти в\nМесто под названием: {habit.place}\n" \
           f"Ты обещал придти в {habit.time}\nЭто займёт у тебя {habit.time_to_complete} минуту(ы)\nПросто сделай это ===> {habit.action}{reward}"

    bot.send_message(habit.user.telegram_id, text)