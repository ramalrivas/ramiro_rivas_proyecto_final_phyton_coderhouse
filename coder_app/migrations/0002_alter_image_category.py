# Generated by Django 5.0.7 on 2024-07-23 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('remeras', 'Remeras'), ('hoodies', 'Hoodies'), ('pantalones', 'Pantalones'), ('shorts', 'Shorts'), ('guantes', 'guantes'), ('zapatillas', 'Zapatillas'), ('botas', 'Botas'), ('carteleras', 'Carteleras'), ('olimpicos_mundiales', 'olimpicos_mundiales')], max_length=100),
        ),
    ]
