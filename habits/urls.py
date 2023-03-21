from django.urls import path

from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import HabitModelViewSet, PublicHabitAPIViewList

app_name = HabitsConfig.name
router = DefaultRouter()
router.register(r'habit', HabitModelViewSet, basename='habit')

urlpatterns = [
    path('publish/list/', PublicHabitAPIViewList.as_view(), name='publish_list')
              ] + router.urls