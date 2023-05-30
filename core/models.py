from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=255)
    dc = models.DateTimeField(auto_now_add=True)


class UserId(models.Model):
    number = models.CharField(max_length=255, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userid')


class Component(models.Model):
    name = models.CharField('Название', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    count = models.FloatField('Количество', null=True, blank=True)
    unit = models.CharField('Единица измрения', max_length=50, null=True)
    price = models.FloatField('Цена', null=True)
    cost = models.FloatField('Стоимость', null=True, blank=True)
    parent = models.BooleanField(default=True)
    parent_id = models.IntegerField(null=True, blank=True)


class Tool(models.Model):
    name = models.CharField('Название', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cost = models.FloatField('Стоимость', null=True)
    usage = models.IntegerField('Срок использования', null=True)
    time = models.IntegerField('Время применения', null=True, default=0)
    depreciation = models.FloatField('Амортизация', null=True)
    parent = models.BooleanField(default=True)
    parent_id = models.IntegerField(null=True)


class Recipe(models.Model):
    name = models.CharField('Название', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField('Описание', null=True)
    components = models.ManyToManyField(Component, null=True, verbose_name='Ингредиенты', related_name='recipe')
    tools = models.ManyToManyField(Tool, null=True, verbose_name='Инструменты', related_name='recipe')
    count = models.IntegerField('Выход', default=1)
    primecost = models.FloatField('Себестоимость', null=True)
    parent = models.BooleanField(default=True)
    parent_id = models.IntegerField(null=True, default=0)
