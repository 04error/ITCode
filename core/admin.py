from django.contrib import admin
from core import models


@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ('name',)
