from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=255)
    dc = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('name', )

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Component(models.Model):
    name = models.CharField('Название', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    count = models.FloatField('Количество', null=True, blank=True)
    unit = models.CharField('Единица измрения', max_length=50, null=True)
    price = models.FloatField('Цена', null=True)
    cost = models.FloatField('Стоимость', null=True, blank=True)
    parent = models.BooleanField(default=True)
    parent_id = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name', 'price', 'owner',)

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField('Название', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cost = models.FloatField('Стоимость', null=True)
    usage = models.IntegerField('Срок использования', null=True)
    time = models.IntegerField('Время применения', null=True, default=0)
    depreciation = models.FloatField('Амортизация', null=True)
    parent = models.BooleanField(default=True)
    parent_id = models.IntegerField(null=True, default=0)

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'
        ordering = ('name', 'cost', 'owner',)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField('Название', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField('Описание', null=True)
    components = models.ManyToManyField(Component, blank=True, verbose_name='Ингредиенты', related_name='recipe')
    tools = models.ManyToManyField(Tool, blank=True, verbose_name='Инструменты', related_name='recipe')
    count = models.IntegerField('Выход', default=1)
    primecost = models.FloatField('Себестоимость', null=True, default=0)
    parent = models.BooleanField(default=True)
    parent_id = models.IntegerField(null=True, default=0)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('name', 'owner',)

    def __str__(self):
        return self.name
