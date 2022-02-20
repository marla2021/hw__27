

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    logo = models.ImageField(upload_to="upload_image/", null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"