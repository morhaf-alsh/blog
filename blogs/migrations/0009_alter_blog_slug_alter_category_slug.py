# Generated by Django 4.2.5 on 2023-09-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_remove_blog_likes_alter_blog_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='vdolbmsxqt'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='ganclthmyr'),
        ),
    ]
