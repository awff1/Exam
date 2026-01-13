from django.db import models
from core.models import TimeStampedModel
from menu.models import Dish

class Review(TimeStampedModel):
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Блюдо"
    )
    rating = models.PositiveSmallIntegerField(
        "Оценка",
        choices=[(i, i) for i in range(1, 6)]
    )
    comment = models.TextField("Комментарий")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.rating}/5"
