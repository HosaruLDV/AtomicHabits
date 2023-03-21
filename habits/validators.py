import datetime

from rest_framework import serializers

from habits.models import Habit


class TimeMax2MinValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('time_to_complete') <= datetime.time(minute=2):
            return True
        else:
            raise serializers.ValidationError('Время должно быть не более 2-х минут')


class RelatedHabitAwardValidator:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        if value.get('pleasant_habit') == False:
            if value.get('related_habit') and value.get('award'):
                raise serializers.ValidationError(
                    'Привычка и награда не может быть выбрана одновременно. Выберите что то одно')
            elif value.get('related_habit') is None and value.get('award') is None:
                raise serializers.ValidationError('Вы должны указать награду или выбрать приятную привычку')
            else:
                return True


class PleasantHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('related_habit'):
            a = Habit.objects.get(pk=value.get('related_habit').id)
            if a.pleasant_habit:
                return True
            else:
                raise serializers.ValidationError('Привычка должна быть приятной')


class PeasantHabitAwardValidator:
    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        if value.get('pleasant_habit'):
            if value.get('related_habit') is None and value.get('award') is None:
                return True
            else:
                raise serializers.ValidationError(
                    'У приятной привычки не может быть вознаграждения или связанной привычки')


class FrequencyValueValidator:
    """Валидатор для поля frequency (не реже 1 раза в 7 дней)"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        frequency = value.get('frequency')

        if frequency:
            if frequency > 7:
                raise serializers.ValidationError("Периодичность не может быть более 7 дней")
