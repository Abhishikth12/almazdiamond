# Generated by Django 5.0.1 on 2025-02-18 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almazdiamondmo_app', '0004_remove_products_images_remove_products_videos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfiles',
            name='image',
        ),
        migrations.RemoveField(
            model_name='productfiles',
            name='video',
        ),
        migrations.AddField(
            model_name='productfiles',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='product_files/'),
        ),
    ]
