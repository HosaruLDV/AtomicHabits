from rest_framework import status
from rest_framework.test import APITestCase

from config import settings
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='Hosaru@mail.ru', telegram_id=settings.TELEGRAM_ID, number='8-800-555-35-35')
        self.user.set_password('12345678')
        self.user.save()

        response = self.client.post('/users/api/token/', {"email": 'Hosaru@mail.ru',
                                               "password": "12345678"})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')


    def test_habit_create(self):

        response = self.client.post('/habit/',
                                    {
                                        "place": "Дома",
                                        "time": "12:20:00",
                                        "action": "попить воды",
                                        "pleasant_habit": False,
                                        "frequency": 1,
                                        "time_to_complete": "00:02:00",
                                        "award": "конфетка"
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_list(self):
        self.test_habit_create()
        response = self.client.get('/habit/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "place": "Дома",
                    "time": "12:20:00",
                    "action": "попить воды",
                    "pleasant_habit": False,
                    "related_habit": None,
                    "frequency": 1,
                    "award": "конфетка",
                    "time_to_complete": "00:02:00",
                    "public": False
                }
            ]
        )

    def test_habit_update(self):
        self.test_habit_create()

        response = self.client.put('/habit/1/', {
                                        "place": "У бабули",
                                        "time": "18:00:00",
                                        "action": "полоть клубнику",
                                        "pleasant_habit": False,
                                        "frequency": 1,
                                        "time_to_complete": "00:02:00",
                                        "award": "Поесть клубнику"
                                    })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "place": "У бабули",
                "time": "18:00:00",
                "action": "полоть клубнику",
                "pleasant_habit": False,
                "related_habit": None,
                "frequency": 1,
                "time_to_complete": "00:02:00",
                "award": "Поесть клубнику",
                "public": False
            }
        )

    def test_habit_detail(self):
        self.test_habit_create()
        response = self.client.get('/habit/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "place": "Дома",
                "time": "12:20:00",
                "action": "попить воды",
                "pleasant_habit": False,
                "related_habit": None,
                "frequency": 1,
                "award": "конфетка",
                "time_to_complete": "00:02:00",
                "public": False
            }
        )

    def test_habit_delete(self):
        self.test_habit_create()
        response = self.client.delete('/habit/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicHabitTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='Hosaru@mail.ru', telegram_id=settings.TELEGRAM_ID, number='8-800-555-35-35')
        self.user.set_password('12345678')
        self.user.save()

        response = self.client.post('/users/api/token/', {"email": 'Hosaru@mail.ru',
                                               "password": "12345678"})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.client.post('/habit/',
                         {
                             "place": "На улице",
                             "time": "20:00:00",
                             "action": "поливать огурцы",
                             "pleasant_habit": False,
                             "frequency": 1,
                             "time_to_complete": "00:02:00",
                             "award": "Выпить чай",
                             "public": True
                         }
                         )

    def test_public_habit_list(self):
        response = self.client.get('/publish/list/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "place": "На улице",
                    "time": "20:00:00",
                    "action": "поливать огурцы",
                    "pleasant_habit": False,
                    "related_habit": None,
                    "frequency": 1,
                    "award": "Выпить чай",
                    "time_to_complete": "00:02:00",
                    "public": True
                }
            ]
        )
