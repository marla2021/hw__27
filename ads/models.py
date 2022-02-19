

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)

class Locatoin(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    location_id = models.PositiveIntegerField()

