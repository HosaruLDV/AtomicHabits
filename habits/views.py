from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from habits.models import Habit
from habits.permissions import OwnerHabit
from habits.serializers import HabitSerializer


class HabitModelViewSet(ModelViewSet):
    """Контроллер для работы с привычками"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [OwnerHabit]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class PublicHabitAPIViewList(ListAPIView):
    """Контроллер для работы с публичными привычками"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Habit.objects.filter(public=True)
        return queryset


