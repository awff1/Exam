from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel

class Restaurant(TimeStampedModel):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец"
    )
    name = models.CharField("Название ресторана", max_length=255)
    address = models.TextField("Адрес")
    contact_info = models.CharField("Контактная информация", max_length=255)
    description = models.TextField("Описание", blank=True)
    logo = models.ImageField(
        "Логотип",
        upload_to='restaurants/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"

    def __str__(self):
        return self.name
