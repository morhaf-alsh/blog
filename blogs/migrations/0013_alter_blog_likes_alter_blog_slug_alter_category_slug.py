# Generated by Django 4.2.5 on 2023-09-11 10:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0012_alter_blog_likes_alter_blog_slug_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blog_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='edkmgtyuzc'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='hidvnbposw'),
        ),
    ]
