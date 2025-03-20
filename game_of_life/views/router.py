from ninja import Router
from uuid import UUID
from django.shortcuts import get_object_or_404
import game_of_life.models as db
from game_of_life.views.schema import (
    GetPatternsListItemSerializer,
    CreatePatternRequestSchema,
)

game_of_life_router = Router()


@game_of_life_router.get("/pattern/{uuid:pattern_id}/")
def get_pattern(request, pattern_id: UUID):
    game_of_life_pattern = get_object_or_404(db.GameOfLifePattern, id=pattern_id)

    return {"pattern": game_of_life_pattern.pattern}


@game_of_life_router.get("/patterns/")
def get_patterns(request):
    game_of_life_patterns = db.GameOfLifePattern.objects.all().order_by("name")

    game_of_life_patterns_list = GetPatternsListItemSerializer(
        game_of_life_patterns, many=True
    ).data

    return {"patterns": game_of_life_patterns_list}


@game_of_life_router.post("/pattern/")
def create_pattern(request, data: CreatePatternRequestSchema):
    game_of_life_pattern = db.GameOfLifePattern.objects.create(
        name=data.name, pattern=data.pattern
    )

    return {"id": game_of_life_pattern.id}
