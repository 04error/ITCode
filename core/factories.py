import factory
from faker import Factory
from core import models

factory_ru = Factory.create('ru-Ru')


class Component(factory.django.DjangoModelFactory):
    name = factory_ru.word()
    price = factory_ru.random_digit()

    class Meta:
        model = models.Component


class Tool(factory.django.DjangoModelFactory):
    name = factory_ru.word()
    cost = factory_ru.random_digit()
    usage = factory_ru.random_digit()

    class Meta:
        model = models.Tool


class Recipe(factory.django.DjangoModelFactory):
    name = factory_ru.word()
    description = factory_ru.text()
    count = factory_ru.random_digit()

    class Meta:
        model = models.Recipe
