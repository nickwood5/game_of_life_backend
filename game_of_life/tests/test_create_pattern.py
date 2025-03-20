from django.test import TestCase
from rest_framework import status
import game_of_life.models as db


class TestCreatePattern(TestCase):
    def get_url(self):
        return "/api/pattern/"

    def test_happy_path(self):
        name = "Pattern"
        pattern = [[1, 0], [0, 2]]
        request_data = {"name": name, "pattern": pattern}

        response = self.client.post(
            self.get_url(), data=request_data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()

        new_pattern_id = response_data["id"]

        game_of_life_pattern = db.GameOfLifePattern.objects.get(id=new_pattern_id)

        self.assertEqual(game_of_life_pattern.name, name)
        self.assertEqual(game_of_life_pattern.pattern, pattern)

    def test_empty_name_throws_error(self):
        request_data = {"name": "", "pattern": [[1, 0], [0, 2]]}

        response = self.client.post(
            self.get_url(), data=request_data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
