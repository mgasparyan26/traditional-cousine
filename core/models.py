from django.db import models


class Location(models.Model):
    country = models.CharField(max_length=200)
    region = models.CharField(max_length=200)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    picture = models.ImageField()
    is_vegetarian = models.BooleanField()


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    location = models.ManyToManyField(to=Location)
    ingredients = models.ManyToManyField(to=Ingredient)
    amount = models.CharField(max_length=200)
    minutes = models.PositiveIntegerField()
