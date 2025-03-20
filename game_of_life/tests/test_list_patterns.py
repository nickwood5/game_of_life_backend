from django.test import TestCase
from rest_framework import status
import game_of_life.models as db


class TestListPatterns(TestCase):
    def get_url(self):
        return "/api/patterns/"

    def test_happy_path(self):
        response_1 = self.client.get(self.get_url())

        self.assertEqual(response_1.status_code, status.HTTP_200_OK)

        response_data_1 = response_1.json()
        expected_data_1 = {"patterns": []}

        self.assertEqual(response_data_1, expected_data_1)

        game_of_life_pattern_1 = db.GameOfLifePattern.objects.create(
            name="Pattern 1", pattern=[[1, 0]]
        )

        game_of_life_pattern_2 = db.GameOfLifePattern.objects.create(
            name="Pattern 2", pattern=[[2, 0]]
        )

        expected_data_2 = {
            "patterns": [
                {
                    "name": game_of_life_pattern_1.name,
                    "id": str(game_of_life_pattern_1.id),
                },
                {
                    "name": game_of_life_pattern_2.name,
                    "id": str(game_of_life_pattern_2.id),
                },
            ]
        }

        response_2 = self.client.get(self.get_url())

        self.assertEqual(response_1.status_code, status.HTTP_200_OK)

        response_data_2 = response_2.json()

        self.assertEqual(response_data_2, expected_data_2)
