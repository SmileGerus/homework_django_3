# Generated by Django 5.0.4 on 2024-04-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
