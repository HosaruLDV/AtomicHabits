from rest_framework import serializers

from habits.models import Habit
from habits.validators import TimeMax2MinValidator, RelatedHabitAwardValidator, PleasantHabitValidator, \
    PeasantHabitAwardValidator, FrequencyValueValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для всех привычек"""
    validators = [
        TimeMax2MinValidator(field='time_to_complete'),
        RelatedHabitAwardValidator(field_1='related_habit', field_2='award'),
        PleasantHabitValidator(field='pleasant_habit'),
        PeasantHabitAwardValidator(field_1= "related_habit", field_2='award', field_3= 'pleasant_habit'),
        FrequencyValueValidator(field='frequency')
    ]

    class Meta:
        model = Habit
        fields = (
            'place',
            'time',
            'action',
            'pleasant_habit',
            'related_habit',
            'frequency',
            'award',
            'time_to_complete',
            'public',
        )


class RelatedHabitSerializer(serializers.ModelSerializer):
    """Сериализатор для полезных привычек"""

    class Meta:
        model = Habit
        fields = ("action",
                  "time_to_complete",
                  "place"
                  )
