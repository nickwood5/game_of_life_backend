from django.test import TestCase
from rest_framework import status
from uuid import UUID, uuid4
import game_of_life.models as db


class TestGetPattern(TestCase):
    def get_url(self, pattern_id: UUID):
        return f"/api/pattern/{pattern_id}/"

    def test_happy_path(self):
        game_of_life_pattern = db.GameOfLifePattern.objects.create(
            name="New pattern", pattern=[[1, 0], [2, 0], [3, 0]]
        )

        response = self.client.get(self.get_url(game_of_life_pattern.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        expected_data = {"pattern": game_of_life_pattern.pattern}

        self.assertEqual(response_data, expected_data)

    def test_nonexistent_id_throws_error(self):
        response = self.client.get(self.get_url(uuid4()))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
