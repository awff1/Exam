from django.db import models
from core.models import TimeStampedModel
from restaurants.models import Restaurant

class Menu(TimeStampedModel):
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menu",
        verbose_name="Ресторан"
    )

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return f"Меню {self.restaurant.name}"


class Dish(TimeStampedModel):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="dishes",
        verbose_name="Меню"
    )
    name = models.CharField("Название блюда", max_length=255)
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField(
        "Изображение",
        upload_to="dishes/",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.name
