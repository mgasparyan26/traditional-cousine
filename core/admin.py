from django.contrib import admin

# Register your models here.
from core import models

admin.register(models.Ingredient)
admin.register(models.Location)
admin.register(models.Recipe)
