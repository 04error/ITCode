# Generated by Django 4.2 on 2023-05-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_component_cost_tool_depreciation'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='time',
            field=models.IntegerField(null=True),
        ),
    ]
