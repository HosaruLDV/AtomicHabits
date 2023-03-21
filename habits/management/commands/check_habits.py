from datetime import datetime, timedelta

import pytz
from django.core.management import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from config import settings


class Command(BaseCommand):
    """Создание задачи на отправку уведомлений в ТГ"""

    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=60,
            period=IntervalSchedule.SECONDS,
        )


        PeriodicTask.objects.create(
            interval=schedule,  # we created this above.
            name='Check time habits',  # simply describes this periodic task.
            task='habits.tasks.check_time_habits',  # name of task.
            expires=datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=365)
        )