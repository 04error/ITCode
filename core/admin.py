from django.contrib import admin
from core import models


@admin.register(models.User)
class User(admin.ModelAdmin):
    pass


@admin.register(models.Recipe)
class Recipes(admin.ModelAdmin):
    pass


@admin.register(models.Component)
class Components(admin.ModelAdmin):
    pass


@admin.register(models.Tool)
class Tools(admin.ModelAdmin):
    pass
