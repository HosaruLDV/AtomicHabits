from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}

class Habit(models.Model):
    """Модель привычек"""

    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    place = models.CharField(max_length=30, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=60, verbose_name='действие')
    pleasant_habit = models.BooleanField(verbose_name='приятная привычка')
    related_habit = models.ForeignKey("self", verbose_name='связанная привычка', on_delete=models.SET_NULL, **NULLABLE)
    frequency = models.IntegerField(default=1, verbose_name='периодичность')
    award = models.CharField(max_length=200, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='время на выполнение')
    public = models.BooleanField(default=True, verbose_name='публичная')

    last_execution = models.DateField(verbose_name='последнее выполнение', **NULLABLE)

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def __str__(self):
        return f'{self.action} {self.place}'
