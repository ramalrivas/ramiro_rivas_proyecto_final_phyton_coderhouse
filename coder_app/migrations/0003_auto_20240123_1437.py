# Generated by Django 3.0.5 on 2024-01-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_app', '0002_auto_20240123_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegallery',
            name='image',
            field=models.ImageField(upload_to='camisas/'),
        ),
    ]
