# Generated by Django 3.2.3 on 2023-10-26 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('year_book', '0006_auto_20231026_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='time_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 22, 57, 47, 656802), verbose_name='date uploaded'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 22, 57, 47, 656802), verbose_name='date uploaded'),
        ),
        migrations.AlterField(
            model_name='year_book',
            name='time_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 22, 57, 47, 669272), verbose_name='date uploaded'),
        ),
    ]
