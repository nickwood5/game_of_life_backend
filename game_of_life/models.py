from django.db import models
from uuid import uuid4


class UUIDModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class GameOfLifePattern(UUIDModel):
    name = models.CharField(unique=True, max_length=50)
    pattern = models.JSONField()
