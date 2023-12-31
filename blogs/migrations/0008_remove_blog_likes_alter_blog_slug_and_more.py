# Generated by Django 4.2.5 on 2023-09-07 10:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0007_category_alter_blog_options_alter_blog_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='nbemudtqyj'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='gzqvnphmfx'),
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(related_name='blog_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
