# Generated by Django 4.2.6 on 2023-10-26 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('year_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='time_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 10, 41, 7, 310840), verbose_name='date uploaded'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 10, 41, 7, 310840), verbose_name='date uploaded'),
        ),
        migrations.AlterField(
            model_name='year_book',
            name='time_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 10, 41, 7, 311836), verbose_name='date uploaded'),
        ),
    ]