from django.db import models


class Recipe(models.Model):
    name = models.CharField()
    location = models.ManyToManyField(to=Location)
    ingredients = models.ManyToManyField(to=Ingredient)
    amount = models.CharField()
    minutes = models.PositiveIntegerField()


class Location(models.Model):
    country = models.CharField()
    region = models.CharField()


class Ingredient(models.Model):
    name = models.CharField()
    calories = models.PositiveIntegerField()
    picture = models.ImageField()
    is_vegetarian = models.BooleanField()
