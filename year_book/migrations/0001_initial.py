# Generated by Django 4.2.6 on 2023-10-26 09:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='about')),
                ('name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=250)),
                ('blog_image', models.FileField(upload_to='blog')),
                ('blog_post', models.TextField()),
                ('post_writer', models.CharField(default='Anon', max_length=200)),
                ('category', models.CharField(default='Culture', max_length=20)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('time_uploaded', models.DateTimeField(default=datetime.datetime(2023, 10, 26, 10, 36, 26, 302297), verbose_name='date uploaded')),
                ('approve', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subject', models.CharField(default='complaint', max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Year_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_first_name', models.CharField(max_length=200)),
                ('student_last_name', models.CharField(max_length=200)),
                ('student_nick_name', models.CharField(max_length=100)),
                ('student_image', models.FileField(upload_to='student')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=11)),
                ('favorite_course', models.CharField(max_length=100)),
                ('favorite_lecturer', models.CharField(max_length=100)),
                ('most_challenging_course', models.CharField(max_length=100)),
                ('relationship_status', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(auto_now_add=True)),
                ('hobbies', models.CharField(max_length=200)),
                ('fun_fact_about_me', models.TextField()),
                ('favorite_quote', models.TextField()),
                ('twitter_handle', models.URLField()),
                ('facebook_handle', models.URLField()),
                ('github', models.URLField()),
                ('linkedin', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('time_uploaded', models.DateTimeField(default=datetime.datetime(2023, 10, 26, 10, 36, 26, 303296), verbose_name='date uploaded')),
                ('approve', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Class Year Book',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.EmailField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]