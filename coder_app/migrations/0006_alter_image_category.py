# Generated by Django 5.0.7 on 2024-07-28 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_app', '0005_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('guantes', 'Guantes'), ('zapatillas', 'Zapatillas'), ('botas', 'Botas'), ('olimpicos_mundiales', 'Olimpicos-mundiales'), ('carteleras', 'Carteleras')], max_length=100),
        ),
    ]
