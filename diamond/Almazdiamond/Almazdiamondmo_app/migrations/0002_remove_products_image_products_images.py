# Generated by Django 5.0.1 on 2025-02-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almazdiamondmo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AddField(
            model_name='products',
            name='images',
            field=models.JSONField(default=list),
        ),
    ]
