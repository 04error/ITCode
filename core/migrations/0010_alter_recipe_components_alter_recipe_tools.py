# Generated by Django 4.2 on 2023-05-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_instance_component_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='components',
            field=models.ManyToManyField(null=True, to='core.component', verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tools',
            field=models.ManyToManyField(null=True, to='core.tool', verbose_name='Инструменты'),
        ),
    ]
