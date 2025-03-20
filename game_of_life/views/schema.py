from rest_framework import serializers
import game_of_life.models as db
from ninja import Schema
from pydantic import Field


class GetPatternsListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = db.GameOfLifePattern
        fields = ["id", "name"]


class CreatePatternRequestSchema(Schema):
    name: str = Field(..., min_length=1, max_length=50)
    pattern: list[list[int]]
