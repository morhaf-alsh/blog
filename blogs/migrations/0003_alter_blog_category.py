# Generated by Django 4.2.5 on 2023-09-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('DevOps', 'DevOps'), ('General', 'General'), ('Networking', 'Networking')], default='General', max_length=100),
        ),
    ]
