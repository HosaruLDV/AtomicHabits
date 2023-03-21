from datetime import datetime, timedelta

from celery import shared_task

from habits.models import Habit
from habits.services import send_message


@shared_task
def check_time_habits():
    """Проверка срабатывает каждую минуту, сравнивает текущее время со временем выполнения привычки
     и отправляет уведомление в Телеграме"""
    time_now = datetime.now()
    habit_queryset = Habit.objects.filter(time=datetime.now().strftime("%H:%M:00"))

    for habit in habit_queryset:
        if habit.last_execution:
            time_send = habit.last_execution + timedelta(days=habit.frequency)
            if time_send == time_now.date():
                send_message(habit)
                habit.last_execution = time_now.date()
                habit.save()
        else:
            send_message(habit)
            habit.last_execution = time_now.date()
            habit.save()
