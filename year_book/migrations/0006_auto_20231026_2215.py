# Generated by Django 3.2.3 on 2023-10-26 21:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('year_book', '0005_auto_20231026_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='time_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 22, 15, 40, 805727), verbose_name='date uploaded'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 22, 15, 40, 805727), verbose_name='date uploaded'),
        ),
        migrations.AlterField(
            model_name='year_book',
            name='time_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 22, 15, 40, 821350), verbose_name='date uploaded'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=150, verbose_name='User Name')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment_content', models.TextField(verbose_name='Content')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='year_book.blog')),
            ],
        ),
    ]