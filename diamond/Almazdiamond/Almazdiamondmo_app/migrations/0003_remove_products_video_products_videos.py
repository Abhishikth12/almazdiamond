# Generated by Django 5.0.1 on 2025-02-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almazdiamondmo_app', '0002_remove_products_image_products_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='video',
        ),
        migrations.AddField(
            model_name='products',
            name='videos',
            field=models.JSONField(default=list),
        ),
    ]
